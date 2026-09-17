#!/usr/bin/env python3
"""Protect previously published evidence and deliberate compatibility redirects.

Run after audit_portfolio.py. Unlike a crawl alone, the saved inventory catches a
page that disappears from both its source tree and its navigation at the same time.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import unittest
from audit_portfolio import BASE, TAXONOMIES, Page, normalize, route_for, urljoin, urlsplit


def inventory_errors(report: dict, baseline: dict, reachable: set[str]) -> list[str]:
    rows = {row['route']: row for row in report['inventory']}
    errors = []
    for route in baseline['required_evidence']:
        if route not in rows:
            errors.append(f'Previously published evidence missing: {route}')
    for route, row in rows.items():
        for field in ('linked_from_featured', 'in_sitemap', 'in_search'):
            if not row[field]: errors.append(f'{field} is false: {route}')
        if route not in reachable: errors.append(f'No non-taxonomy navigation path: {route}')
    for route in baseline['required_academic']:
        if route not in rows or not rows[route]['academic']:
            errors.append(f'Academic evidence missing or relabeled: {route}')
    for route in baseline['required_support']:
        if route not in reachable: errors.append(f'Support page not reachable: {route}')
    return errors


class RegressionTests(unittest.TestCase):
    def setUp(self):
        self.row = {'route': '/projects/example/', 'academic': True,
                    'linked_from_featured': True, 'in_sitemap': True, 'in_search': True}
        self.report = {'inventory': [self.row]}
        self.baseline = {'required_evidence': ['/projects/example/'],
                         'required_academic': ['/projects/example/'], 'required_support': ['/security-privacy/']}
        self.reachable = {'/projects/example/', '/security-privacy/'}

    def test_complete_inventory_passes(self):
        self.assertEqual(inventory_errors(self.report, self.baseline, self.reachable), [])

    def test_deleted_or_drafted_page_fails(self):
        self.report['inventory'] = []
        self.assertTrue(inventory_errors(self.report, self.baseline, self.reachable))

    def test_removed_catalog_link_fails(self):
        self.row['linked_from_featured'] = False
        self.assertTrue(inventory_errors(self.report, self.baseline, self.reachable))

    def test_missing_search_or_sitemap_fails(self):
        for field in ('in_search', 'in_sitemap'):
            with self.subTest(field=field):
                self.row[field] = False
                self.assertTrue(inventory_errors(self.report, self.baseline, self.reachable))
                self.row[field] = True

    def test_unreachable_support_fails(self):
        self.reachable.remove('/security-privacy/')
        self.assertTrue(inventory_errors(self.report, self.baseline, self.reachable))

    def test_new_undiscoverable_evidence_fails(self):
        self.report['inventory'].append(dict(self.row, route='/projects/new/', linked_from_featured=False))
        self.assertTrue(inventory_errors(self.report, self.baseline, self.reachable))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RegressionTests))
        return 0 if result.wasSuccessful() else 1
    baseline = json.loads(Path(__file__).with_name('portfolio_inventory.json').read_text())
    report = json.loads(Path('portfolio-audit.json').read_text())
    root = Path('public')
    pages = {route_for(f, root): Page(f.read_text(encoding='utf-8')) for f in root.rglob('*.html')}
    reachable, queue = set(), ['/']
    while queue:
        route = queue.pop()
        if route in reachable or route not in pages or route.startswith(TAXONOMIES): continue
        reachable.add(route)
        page = pages[route]
        for href in page.links + ([page.redirect] if page.redirect else []):
            target = urlsplit(urljoin(BASE + route, href))
            if target.netloc in ('sudorunner.org', 'www.sudorunner.org'):
                queue.append(normalize(target.path))
    errors = inventory_errors(report, baseline, reachable)
    for old, new in baseline['preserved_aliases'].items():
        page = pages.get(old)
        target = normalize(urlsplit(page.redirect).path) if page and page.redirect else ''
        if target != new or new not in pages:
            errors.append(f'Compatibility redirect missing or changed: {old} -> {new}')
    result = {'required_evidence': len(baseline['required_evidence']),
              'required_academic': len(baseline['required_academic']),
              'preserved_aliases': len(baseline['preserved_aliases']),
              'errors': errors}
    Path('portfolio-inventory-check.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
