---
title: "sudoRunner Portfolio Website"
description: "A professional cybersecurity portfolio built with Hugo, Blowfish, GitHub, Cloudflare Pages, custom DNS, email routing, custom styling, mobile HCI improvements, guided review paths, and security-conscious publishing."
date: 2026-06-04
tags: ["Hugo", "Blowfish", "Cloudflare Pages", "GitHub", "Portfolio", "Web Design", "HCI", "Security", "Static Site", "Technical Writing"]
categories: ["Projects"]
showDate: true
showAuthor: false
showReadingTime: true
showWordCount: false
---

<span class="sr-eyebrow">Live Portfolio Project</span>

<div class="sr-case-hero">

`sudoRunner` is not just where I publish my portfolio. It is also one of the projects.

I built it to turn my resume, academic work, cybersecurity labs, ServiceNow SecOps direction, GRC work, incident response projects, forensics evidence, and technical writing into something a reviewer can actually navigate.

</div>

<div class="sr-case-summary">

<div class="sr-case-item">
  <span class="sr-case-label">Type</span>
  <span class="sr-case-value">Professional Cybersecurity Portfolio</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Stack</span>
  <span class="sr-case-value">Hugo · Blowfish · GitHub · Cloudflare Pages</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Focus</span>
  <span class="sr-case-value">HCI · Security-Conscious Publishing · Technical Writing</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Deployment</span>
  <span class="sr-case-value">Cloudflare Pages + Custom Domain</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Brand</span>
  <span class="sr-case-value">sudoRunner Terminal-Style Identity</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Status</span>
  <span class="sr-case-value">Live / Iterative</span>
</div>

</div>

## Why I Built This

I wanted something better than a static resume.

A resume can list ServiceNow, vulnerability management, cybersecurity labs, incident response, forensics, malware analysis, GRC, cloud, HCI, and software coursework. But it does not show how I think, how I write, how I organize evidence, or how careful I am with sensitive material.

This site is meant to solve that problem.

The goal is simple:

- help a recruiter understand my fit quickly
- help a technical reviewer find the strongest evidence
- keep ServiceNow SecOps and Vulnerability Response easy to find
- show academic work without dumping raw submissions
- show technical depth without publishing sensitive files
- make the site usable on desktop and mobile
- keep the review path obvious

---

## What I Actually Built

This site includes:

- a homepage with a clear Start Here path
- role-based review paths
- a capability-to-evidence map
- a project gallery with course-coded academic evidence
- a public resume page
- a credentials page
- a professional contact page
- a changelog
- a ServiceNow SecOps lab hub
- cybersecurity lab summaries
- Governance, Risk & Privacy analysis summaries
- incident response and forensics summaries
- OT/ICS security notes
- AI-assisted SecOps concept notes
- mobile layout fixes
- custom CSS and layout overrides
- custom favicon and branding
- privacy-conscious public publishing choices

The result is a portfolio that is organized more like a technical product than a folder of assignments.

---

## Architecture

The site uses a static deployment model.

<div class="sr-flow">

<div class="sr-flow-step">
  <span class="sr-flow-number">1</span>

### Local Hugo Site

Content, Markdown pages, layout overrides, partials, custom CSS, and static assets are maintained locally.

<span class="sr-status sr-status-complete">Local Build</span>
</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">2</span>

### GitHub Repository

Changes are committed through Git and pushed to GitHub for version control and deployment tracking.

<span class="sr-status sr-status-complete">Version Control</span>
</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">3</span>

### Cloudflare Pages

Cloudflare Pages builds and deploys the Hugo site from the GitHub repository.

<span class="sr-status sr-status-complete">Static Hosting</span>
</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">4</span>

### Custom Domain

The site is served through a custom domain with Cloudflare DNS.

<span class="sr-status sr-status-complete">DNS</span>
</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">5</span>

### Public Contact Layer

Cloudflare Email Routing and a public-facing contact alias keep personal contact details off the site.

<span class="sr-status sr-status-complete">Contact Privacy</span>
</div>

</div>

---

## HCI Decisions

A lot of the work on this site has been HCI work, not just design polish.

The biggest usability issue was that the site kept growing. As more academic projects were added, the portfolio needed stronger navigation and a clearer hierarchy.

The current structure is built around reviewer intent:

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Problem</div>
  <div>Design Decision</div>
  <div>Result</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Too many possible starting points</div>
  <div class="sr-record-detail">Added a stronger homepage Start Here button and a dedicated Start Here page.</div>
  <div class="sr-record-status"><span class="sr-static-label">Clear Entry</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Different reviewers care about different evidence</div>
  <div class="sr-record-detail">Built role-based review paths for recruiters, ServiceNow reviewers, cybersecurity analysts, IR/forensics reviewers, GRC reviewers, OT/ICS reviewers, cloud reviewers, and HCI/software reviewers.</div>
  <div class="sr-record-status"><span class="sr-static-label">Role-Based Paths</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Project list became too large</div>
  <div class="sr-record-detail">Reorganized Projects by evidence strength and topic instead of treating every course artifact as equal.</div>
  <div class="sr-record-status"><span class="sr-static-label">Hierarchy</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Buttons and labels looked too similar</div>
  <div class="sr-record-detail">Separated clickable CTAs from static badges, honors, credentials, labels, and information panels.</div>
  <div class="sr-record-status"><span class="sr-static-label">Click Clarity</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Mobile layout had visual collisions</div>
  <div class="sr-record-detail">Adjusted card stacking, spacing, button behavior, safe areas, and text wrapping for smaller screens.</div>
  <div class="sr-record-status"><span class="sr-static-label">Mobile HCI</span></div>
</div>

</div>

---

## Security-Conscious Publishing

A cybersecurity portfolio has a different publishing problem than a normal design portfolio.

A lot of my evidence involves malware labs, forensics, incident response, security tools, academic submissions, simulated environments, screenshots, credentials, and sensitive technical details. Publishing everything raw would be careless.

So the site uses a redacted summary approach.

I avoid publishing:

- malware samples
- forensic images
- packet captures
- raw lab screenshots with sensitive details
- full academic answers
- credential IDs
- transcripts
- private student data
- client information
- exact lab environment details
- raw exploit or crackme instructions
- sensitive infrastructure details

Instead, I publish:

- what the work was about
- what tools or methods were used
- what the project shows
- what I learned
- why it matters for the roles I am targeting
- where the limits are

That approach lets the site show real work without becoming a data leak.

---

## Content Strategy

The most important content decision was to stop treating every page as equally important.

The portfolio now has an evidence hierarchy.

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Level</div>
  <div>Examples</div>
  <div>Purpose</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Flagship Evidence</div>
  <div class="sr-record-detail">ServiceNow SecOps Lab Hub, CYBER 440 Capstone, CYBER 366 Malware Analytics, IST 454 Forensics, IST 456 Security & Risk Management.</div>
  <div class="sr-record-status"><span class="sr-static-label">Lead With These</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Strong Supporting Evidence</div>
  <div class="sr-record-detail">CYBER 342W, IST 432, IST 402, IST 331, CYBER 362, CYBER 262, IST 495.</div>
  <div class="sr-record-status"><span class="sr-static-label">Support the Story</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Foundation Evidence</div>
  <div class="sr-record-detail">SRA 221, SRA 231, SRA 311, IST 240, IST 242, IST 250, IST 261, IST 311.</div>
  <div class="sr-record-status"><span class="sr-static-label">Show Progression</span></div>
</div>

</div>

This makes the site more honest. Not every course artifact should be a headline project. Some pages are there to show growth, foundation, and context.

---

## What Changed Over Time

The site started as a simpler portfolio. It became more structured as more evidence was added.

Major improvements included:

<div class="sr-card-grid">

<div class="sr-card">

### Guided Review Flow

The site now has a clearer Start Here path and role-based review paths.

<span class="sr-static-label sr-static-label-complete">Navigation</span>

</div>

<div class="sr-card">

### Mobile Cleanup

Cards, buttons, labels, and content blocks were adjusted so mobile pages feel less cramped and less broken.

<span class="sr-static-label sr-static-label-complete">Mobile</span>

</div>

<div class="sr-card">

### Brand Cleanup

The default Blowfish favicon was replaced with the sudoRunner terminal-style favicon.

<span class="sr-static-label sr-static-label-complete">Branding</span>

</div>

<div class="sr-card">

### Credential Cleanup

Education, certifications, honor societies, and credentials were rebuilt into clearer static records.

<span class="sr-static-label sr-static-label-complete">Credentials</span>

</div>

<div class="sr-card">

### Project Expansion

Academic work was reviewed course by course, then converted into portfolio-safe case summaries.

<span class="sr-static-label sr-static-label-complete">Evidence</span>

</div>

<div class="sr-card">

### Voice Cleanup

The core pages were rewritten to sound more direct and less generic.

<span class="sr-static-label sr-static-label-complete">Writing</span>

</div>

</div>

---

## Pages I Built or Reworked

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Page Type</div>
  <div>Examples</div>
  <div>Why It Matters</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Core Reviewer Pages</div>
  <div class="sr-record-detail"><a href="/start-here/">Start Here</a>, <a href="/review-paths/">Review Paths</a>, <a href="/capabilities/">Capabilities</a>, <a href="/opportunity-fit/">Opportunity Fit</a></div>
  <div class="sr-record-status"><span class="sr-static-label">Navigation</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Professional Pages</div>
  <div class="sr-record-detail"><a href="/resume/">Resume</a>, <a href="/about/">About</a>, <a href="/credentials/">Credentials</a>, <a href="/contact/">Contact</a></div>
  <div class="sr-record-status"><span class="sr-static-label">Identity</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Evidence Pages</div>
  <div class="sr-record-detail"><a href="/projects/">Projects</a>, <a href="/research-labs/">Research & Labs</a>, <a href="/ot-ics-security/">OT/ICS Security</a>, <a href="/ai-security/">AI & Security</a></div>
  <div class="sr-record-status"><span class="sr-static-label">Proof of Work</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Site Maintenance Pages</div>
  <div class="sr-record-detail"><a href="/changelog/">Portfolio Changelog</a>, security metadata, contact routing, privacy-conscious public publishing choices.</div>
  <div class="sr-record-status"><span class="sr-static-label">Product Thinking</span></div>
</div>

</div>

---

## What This Project Shows

This project shows a mix of technical and communication skills:

- Hugo static site development
- Blowfish customization
- Markdown content architecture
- custom CSS
- Git workflow
- Cloudflare Pages deployment
- custom DNS
- email routing
- responsive layout cleanup
- mobile usability testing
- HCI-focused navigation design
- security-conscious publishing
- technical writing
- content hierarchy
- project organization
- public professional branding

The most important part is not that I can make a website.

The important part is that I can organize a large amount of technical evidence into something understandable, safe to publish, and usable by different audiences.

---

## What Was Harder Than Expected

A few things took more debugging than expected:

- favicon replacement because browser and theme fallback caching were stubborn
- mobile layout collisions
- making buttons and labels visually distinct
- avoiding repeated content as more projects were added
- keeping course-coded project names consistent
- deciding what should be a flagship page versus supporting evidence
- writing about cybersecurity work without exposing too much detail
- making the site sound like a person wrote it, not a brochure

Those were useful problems to solve because they are the same kind of problems that appear in real technical communication: structure, clarity, user flow, and safe disclosure.

---

## Limits

This site is not meant to be a raw evidence repository.

It does not prove every detail by publishing every file. That is intentional. A public cybersecurity portfolio should not expose everything.

The better goal is to show enough evidence for a reviewer to understand the work, then keep private materials available only for appropriate verification.

---

## Next Improvements

Things I may add later:

- professional headshot on the About page
- short Security Notes / Field Notes section
- better social preview metadata
- protected contact form with spam protection
- project-page "How to read this page" blocks for flagship projects
- cleaner diagrams for selected workflows
- accessibility audit
- more ServiceNow SecOps lab detail
- ServiceNow IRM/GRC learning path notes
- OT/ICS security reading notes

---

## Related Pages

<div class="sr-cta-row">
  <a class="sr-button" href="/start-here/">Start Here</a>
  <a class="sr-button-secondary sr-button" href="/projects/">Projects</a>
  <a class="sr-button-secondary sr-button" href="/capabilities/">Capabilities</a>
  <a class="sr-button-secondary sr-button" href="/changelog/">Changelog</a>
</div>
