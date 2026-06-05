---

title: "sudoRunner Portfolio Website"
description: "A professional cybersecurity portfolio built with Hugo, Blowfish, GitHub, Cloudflare Pages, custom DNS, email routing, custom styling, guided navigation, mobile HCI improvements, and security-conscious publishing."
date: 2026-06-04
tags: ["Hugo", "Blowfish", "Cloudflare Pages", "GitHub", "Portfolio", "Web Design", "HCI", "Security", "Static Site"]
categories: ["Projects"]
showDate: true
showAuthor: false
showReadingTime: true
showWordCount: false
--------------------

<span class="sr-eyebrow">Web Portfolio Project</span>

<div class="sr-case-hero">

`sudoRunner` is a professional cybersecurity portfolio designed to showcase ServiceNow SecOps, Vulnerability Response, cybersecurity operations, OT/ICS security interests, AI-assisted SecOps concepts, academic work, and technical projects in a security-conscious, recruiter-friendly format.

</div>

<div class="sr-case-summary">

<div class="sr-case-item">
  <span class="sr-case-label">Type</span>
  <span class="sr-case-value">Professional Portfolio Website</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Stack</span>
  <span class="sr-case-value">Hugo · Blowfish · GitHub · Cloudflare Pages</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Focus</span>
  <span class="sr-case-value">Cybersecurity Portfolio + HCI + Security-Conscious Publishing</span>
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
  <span class="sr-case-label">Privacy Level</span>
  <span class="sr-case-value">Public Portfolio / Redacted Content</span>
</div>

</div>

# sudoRunner Portfolio Website

## Overview

`sudoRunner` is a professional portfolio website built to show proof of work beyond a resume.

The site is designed around a specific professional goal: helping recruiters, hiring managers, cybersecurity reviewers, ServiceNow reviewers, and technical reviewers quickly understand my background, technical focus, portfolio evidence, and best-fit opportunities.

The site focuses on:

* ServiceNow SecOps and Vulnerability Response
* vulnerability management and security operations
* cybersecurity lab work and academic projects
* OT/ICS security interest and cyber-physical risk
* AI-assisted SecOps workflow ideas
* redacted case studies and portfolio-safe publishing
* public resume and credential review
* HCI-friendly navigation and guided reviewer flow

---

## Why I Built It

A traditional resume is limited. It can list skills, tools, projects, and roles, but it does not always show how someone thinks through technical work.

This portfolio was created to demonstrate:

* technical depth
* security workflow thinking
* ServiceNow SecOps interest
* cybersecurity analyst foundations
* OT/ICS security curiosity
* AI-assisted security workflow ideas
* communication ability
* project organization
* security-conscious publishing judgment

The site is also meant to demonstrate that I can design and maintain a professional public technical presence while protecting sensitive information.

---

## Architecture

`sudoRunner` follows a static-site deployment architecture.

<div class="sr-flow">

<div class="sr-flow-step">
  <span class="sr-flow-number">1</span>

### Local Hugo Project

Content, layout overrides, Markdown pages, custom CSS, static assets, and portfolio structure are maintained locally.

<span class="sr-static-label sr-static-label-complete">Local Build</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">2</span>

### GitHub Repository

Changes are committed through Git and pushed to GitHub for version control and deployment tracking.

<span class="sr-static-label sr-static-label-complete">Version Control</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">3</span>

### Cloudflare Pages

Cloudflare Pages builds and deploys the Hugo site automatically from the GitHub repository.

<span class="sr-static-label sr-static-label-complete">Static Deployment</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">4</span>

### Custom Domain

The site is served through `sudorunner.org` with Cloudflare DNS managing the domain configuration.

<span class="sr-static-label sr-static-label-complete">Custom DNS</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">5</span>

### Security and Contact Layer

Cloudflare Email Routing, security headers, security.txt, robots.txt, humans.txt, public resume handling, and privacy-conscious content support the professional deployment.

<span class="sr-static-label sr-static-label-complete">Security-Aware</span>

</div>

</div>

The deployment flow is:

Local Hugo Project → GitHub Repository → Cloudflare Pages Build → sudorunner.org Custom Domain → Email Routing + Security Metadata

---

## Design Features

This project includes:

* custom SVG terminal-style logo
* sudoRunner favicon and browser tab branding
* favicon override for Blowfish default assets
* Apple-style desktop dropdown navigation
* mobile-friendly navigation refinements
* custom section and single-page layouts
* Start Here portfolio review workflow
* guided 60-second review path navigation
* role-based Review Paths page
* Opportunity Fit page
* Capabilities Matrix page
* Badge Legend page
* Portfolio Changelog page
* custom branded 404 page
* card-based project galleries
* static credential record layout
* non-clickable metadata labels
* distinct clickable CTA buttons
* color-coded status labels
* bright academic honor styling for Cum Laude
* dark-mode badge contrast tuning
* reusable callout boxes
* mobile HCI stabilization
* security headers
* security.txt contact standard
* robots.txt and humans.txt metadata files
* privacy-conscious public resume workflow
* professional email alias through Cloudflare Email Routing

---

## HCI and Usability Improvements

A major design goal was to make the site easier to use for people who do not have time to explore randomly.

Recent HCI improvements include:

<div class="sr-card-grid">

<div class="sr-card">

### Guided Review Flow

The site now supports a clear reviewer path:

Resume → ServiceNow SecOps → Projects → OT/ICS Security → AI & Security → Contact.

<span class="sr-static-label sr-static-label-complete">Navigation</span>

</div>

<div class="sr-card">

### Mobile Usability

Mobile layout was tuned for spacing, stacked buttons, workflow cards, Safari safe areas, card clipping, and readable text hierarchy.

<span class="sr-static-label sr-static-label-complete">Mobile HCI</span>

</div>

<div class="sr-card">

### Clickability Distinction

Clickable buttons were visually separated from non-clickable badges, labels, honors, and status markers.

<span class="sr-static-label sr-static-label-complete">Visual Hierarchy</span>

</div>

<div class="sr-card">

### Credential Clarity

Education and credentials were redesigned into static information panels and structured credential records.

<span class="sr-static-label sr-static-label-complete">Content Design</span>

</div>

</div>

---

## Security and Privacy Approach

This portfolio is intentionally designed with security-conscious publishing in mind.

The site avoids publishing:

* raw academic submissions
* full solution files
* sensitive screenshots
* credentials or secrets
* private contact details
* client names or private client data
* internal infrastructure details
* implementation details that should not be public

Instead, projects are converted into:

* redacted case studies
* sanitized summaries
* workflow descriptions
* lessons learned
* portfolio-safe evidence
* technical concept notes

This allows the site to demonstrate technical depth without creating unnecessary privacy, academic, employer, client, or operational security risk.

---

## What This Project Demonstrates

This project demonstrates:

* static site deployment
* Hugo site structure
* Blowfish theme customization
* custom Hugo layout overrides
* theme partial customization
* dropdown navigation customization
* reusable content components
* mobile responsive styling
* HCI-aware reviewer flow
* visual hierarchy decisions
* security-conscious static site deployment
* public metadata configuration
* structured portfolio navigation
* role-based content routing
* capability-to-evidence mapping
* privacy-conscious resume publishing
* Cloudflare DNS and Pages workflow
* Cloudflare Email Routing use
* Git-based version control and deployment

---

## Key Pages Created

Major portfolio pages include:

<div class="sr-card-grid">

<div class="sr-card sr-project-card">

<div>

### [Start Here](/start-here/)

Recommended review starting point with a 60-second workflow.

</div>

<span class="sr-static-label sr-static-label-complete">Reviewer Flow</span>

</div>

<div class="sr-card sr-project-card">

<div>

### [Opportunity Fit](/opportunity-fit/)

Recruiter-friendly role alignment and best-fit opportunities.

</div>

<span class="sr-static-label sr-static-label-complete">Hiring Fit</span>

</div>

<div class="sr-card sr-project-card">

<div>

### [Review Paths](/review-paths/)

Role-based review paths for ServiceNow, cybersecurity, OT/ICS, AI, software, web, and recruiters.

</div>

<span class="sr-static-label sr-static-label-complete">Navigation</span>

</div>

<div class="sr-card sr-project-card">

<div>

### [Capabilities](/capabilities/)

Capability-to-evidence map linking skill areas to proof of work.

</div>

<span class="sr-static-label sr-static-label-complete">Evidence Map</span>

</div>

<div class="sr-card sr-project-card">

<div>

### [Projects](/projects/)

Portfolio gallery of selected redacted projects and technical work.

</div>

<span class="sr-static-label sr-static-label-complete">Project Gallery</span>

</div>

<div class="sr-card sr-project-card">

<div>

### [Portfolio Changelog](/changelog/)

Documented improvements to the site as a technical product.

</div>

<span class="sr-static-label sr-static-label-complete">Product Tracking</span>

</div>

</div>

---

## Implementation Notes

The implementation required working across:

* Hugo content files
* Blowfish theme layout overrides
* custom partials
* custom CSS
* static assets
* navigation menus
* Cloudflare Pages deployment behavior
* browser caching behavior
* favicon override behavior
* mobile layout testing
* live site validation

Several issues required debugging, including theme fallback favicon behavior, Hugo local server port changes, mobile layout collisions, and ensuring that guided review navigation appeared on both list and single content pages.

---

## Lessons Learned

This project reinforced several practical lessons:

* HCI is not just visual design; it affects whether reviewers know where to go next.
* Mobile testing matters because desktop polish does not guarantee mobile usability.
* Static labels and clickable buttons need different visual language.
* Browser favicon caching can make simple branding changes harder to validate than expected.
* Theme overrides should be implemented carefully to avoid editing theme files directly.
* A technical portfolio should protect sensitive information while still showing meaningful evidence.
* A changelog helps turn portfolio improvements into visible product-thinking evidence.

---

## What I Would Improve Next

Future improvements may include:

* adding a real scheduling link for intro calls
* adding a protected contact form with Cloudflare Turnstile
* improving mobile navigation behavior further
* auditing all pages for text-box versus button consistency
* improving accessibility and keyboard navigation
* adding sanitized screenshots where appropriate
* adding diagrams for selected technical workflows
* expanding ServiceNow SecOps lab content
* adding more OT/ICS security notes
* adding more AI-assisted SecOps workflow concepts
* continuing to review academic work and convert the strongest items into redacted case studies
* improving metadata and social preview behavior over time

---

## Portfolio Note

This project is both the container for the portfolio and a portfolio project itself.

It demonstrates technical implementation, public-site architecture, HCI refinement, security-conscious publishing, branding, and iterative improvement over time.
