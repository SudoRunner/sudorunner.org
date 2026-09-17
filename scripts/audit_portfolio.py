#!/usr/bin/env python3
"""Audit a Hugo build without changing the site or contacting external domains.

Usage: python3 scripts/audit_portfolio.py [--live] [--strict-catalog]
Requires only Python's standard library and a completed Hugo build in public/.
"""
from __future__ import annotations
import argparse
import concurrent.futures
import json
import re
import subprocess
import sys
from collections import deque
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

BASE = 'https://sudorunner.org'
SECTIONS = ('/projects/', '/research-labs/', '/ot-ics-security/', '/ai-security/', '/professional-experience/')
TAXONOMIES = ('/tags/', '/categories/', '/series/', '/authors/')

class Page(HTMLParser):
    def __init__(self, text: str):
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.assets: list[str] = []
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.title = ''
        self.in_title = False
        self.redirect = ''
        self.canonical = ''
        self.text: list[str] = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        ident = a.get('id') or (a.get('name') if tag == 'a' else '')
        if ident:
            if ident in self.ids: self.duplicate_ids.add(ident)
            self.ids.add(ident)
        if tag == 'title': self.in_title = True
        if tag == 'a' and a.get('href'): self.links.append(a['href'])
        if tag in ('img', 'script', 'iframe', 'source', 'video', 'audio') and a.get('src'):
            self.assets.append(a['src'])
        if tag == 'link' and a.get('rel') in ('stylesheet', 'icon', 'manifest', 'apple-touch-icon') and a.get('href'):
            self.assets.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href', '')
        if tag == 'meta' and a.get('http-equiv', '').lower() == 'refresh':
            match = re.search(r'url\s*=\s*(.+)', a.get('content', ''), re.I)
            if match: self.redirect = match.group(1).strip(' \"\'')

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_title: self.title += data
        self.text.append(data)


def route_for(file: Path, root: Path) -> str:
    relative = file.relative_to(root).as_posix()
    return '/' + relative[:-10] if relative.endswith('index.html') else '/' + relative


def normalize(path: str) -> str:
    path = unquote(path)
    if path.endswith('/index.html'): path = path[:-10]
    if not Path(path).suffix and not path.endswith('/'): path += '/'
    return path or '/'


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], text=True, stderr=subprocess.DEVNULL)


def source_history() -> dict:
    current = set(git('ls-tree', '-r', '--name-only', 'HEAD', '--', 'content').splitlines())
    ever = set(git('log', '--all', '--format=', '--name-only', '--', 'content').splitlines()) - {''}
    history = []
    previous: set[str] = set()
    path = 'content/projects/_index.md'
    for commit in git('log', '--reverse', '--format=%H', 'origin/main', '--', path).splitlines():
        try: text = git('show', f'{commit}:{path}')
        except subprocess.CalledProcessError: continue
        links = set(re.findall(r'(?:href=[\"\']|\]\()(/[^\s\"\'\)<>]+)', text))
        removed = sorted(previous - links)
        if removed:
            history.append({'commit': commit, 'change': git('show', '-s', '--format=%cs %s', commit).strip(), 'removed_links': removed})
        previous = links
    return {'historical_source_paths': len(ever), 'current_source_paths': len(current),
            'paths_not_in_current_tree': sorted(ever-current), 'catalog_link_removals': history}


def check_live(route: str) -> dict:
    try:
        request = Request(BASE + route, headers={'User-Agent': 'sudoRunner-Portfolio-Audit/1.0'})
        with urlopen(request, timeout=20) as response:
            raw = response.read(4_000_000)
            text = raw.decode('utf-8', errors='replace')
            page = Page(text) if 'text/html' in response.headers.get('Content-Type', '') else None
            return {'route': route, 'status': response.status, 'final_url': response.url,
                    'title': page.title if page else '',
                    'links': sorted(set(page.links)) if page else [],
                    'is_404_page': bool(page and re.search(r'\b404\b|page not found', page.title, re.I))}
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return {'route': route, 'error': str(exc)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true', help='Also GET the public site routes, with at most four requests in parallel.')
    parser.add_argument('--strict-catalog', action='store_true', help='Require every academic page to be linked from Featured Work.')
    args = parser.parse_args()
    root = Path('public')
    pages = {route_for(f, root): Page(f.read_text(encoding='utf-8')) for f in root.rglob('*.html')}
    if '/' not in pages: raise SystemExit('No completed Hugo build found in public/.')
    graph = {route: set() for route in pages}
    broken = set()
    anchors = set()
    assets = set()
    for route, page in pages.items():
        for href in page.links + ([page.redirect] if page.redirect else []):
            url = urlsplit(urljoin(BASE + route, href))
            if url.scheme not in ('http', 'https') or url.netloc not in ('sudorunner.org', 'www.sudorunner.org'): continue
            target = normalize(url.path)
            if target in pages:
                graph[route].add(target)
                if url.fragment and not pages[target].redirect and unquote(url.fragment) not in pages[target].ids:
                    anchors.add((route, href))
            elif not (root / unquote(url.path).lstrip('/')).is_file(): broken.add((route, href))
        for src in page.assets:
            url = urlsplit(urljoin(BASE + route, src))
            if url.scheme not in ('http', 'https') or url.netloc not in ('sudorunner.org', 'www.sudorunner.org'): continue
            if not (root / unquote(url.path).lstrip('/')).is_file() and normalize(url.path) not in pages:
                assets.add((route, src))
    evidence = sorted(route for route, page in pages.items() if route.startswith(SECTIONS) and route not in SECTIONS and not page.redirect and '/page/' not in route)
    academic = [route for route in evidence if re.match(r'^(IST|CYBER|SRA)\s+\d', pages[route].title)]
    editorial_graph = {route: {p for p in targets if not p.startswith(TAXONOMIES)} for route, targets in graph.items() if not route.startswith(TAXONOMIES)}
    seen = set()
    queue = deque(['/'])
    while queue:
        route = queue.popleft()
        if route in seen: continue
        seen.add(route)
        queue.extend(editorial_graph.get(route, set()) - seen)
    featured = graph.get('/projects/', set())
    missing_academic = [p for p in academic if p not in featured]
    missing_evidence = [p for p in evidence if p not in featured]
    sitemap = set()
    if (root / 'sitemap.xml').exists():
        xml = ET.parse(root / 'sitemap.xml')
        sitemap = {normalize(urlsplit(element.text or '').path) for element in xml.findall('.//{*}loc')}
    search_urls = set()
    if (root / 'index.json').exists():
        def walk(value):
            if isinstance(value, dict):
                for key, item in value.items():
                    if key.lower() in ('uri', 'url', 'permalink', 'relpermalink') and isinstance(item, str): search_urls.add(normalize(urlsplit(item).path))
                    else: walk(item)
            elif isinstance(value, list):
                for item in value: walk(item)
        walk(json.loads((root / 'index.json').read_text()))
    inventory = [{'route': route, 'title': pages[route].title, 'academic': route in academic,
                  'linked_from_featured': route in featured,
                  'incoming_editorial_pages': sorted(p for p, links in editorial_graph.items() if route in links and p != route),
                  'in_sitemap': route in sitemap, 'in_search': route in search_urls}
                 for route in evidence]
    report = {'commit': git('rev-parse', 'HEAD').strip(), 'html_pages': len(pages),
              'evidence_pages': len(evidence), 'academic_pages': len(academic), 'inventory': inventory,
              'missing_academic_from_featured': missing_academic, 'missing_evidence_from_featured': missing_evidence,
              'unreachable_evidence': [p for p in evidence if p not in seen],
              'missing_evidence_from_sitemap': [p for p in evidence if p not in sitemap],
              'missing_evidence_from_search': [p for p in evidence if p not in search_urls],
              'broken_internal_links': sorted(broken), 'broken_anchors': sorted(anchors),
              'missing_assets': sorted(assets),
              'duplicate_html_ids': {p: sorted(page.duplicate_ids) for p, page in pages.items() if page.duplicate_ids},
              'history': source_history()}
    if args.live:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            report['live'] = list(executor.map(check_live, sorted(set(evidence + list(SECTIONS) + ['/', '/servicenow-secops/', '/about/', '/start-here/', '/resume/', '/credentials/', '/contact/', '/security-privacy/']))))
    output = Path('portfolio-audit.json')
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    brief = {k: v for k, v in report.items() if k not in ('inventory', 'live', 'duplicate_html_ids')}
    if args.live:
        brief['live_failures'] = [r for r in report['live'] if 'error' in r or r.get('is_404_page')]
        brief['live_routes_checked'] = len(report['live'])
    print(json.dumps(brief, indent=2))
    print('\nFULL EVIDENCE INVENTORY')
    for row in inventory: print(json.dumps(row, ensure_ascii=False))
    failed = broken or assets or report['unreachable_evidence'] or report['missing_evidence_from_sitemap'] or report['missing_evidence_from_search']
    if args.strict_catalog: failed = failed or missing_academic or anchors
    return 1 if failed else 0

if __name__ == '__main__':
    sys.exit(main())
