---
title: "Security & Privacy"
description: "Security and privacy practices used for the sudoRunner portfolio."
showDate: false
showAuthor: false
showReadingTime: false
---

<span class="sr-eyebrow">Security-Conscious Publishing</span>

This page explains how `sudoRunner` is designed as a public cybersecurity portfolio while limiting unnecessary exposure of personal, academic, client, or sensitive information.

<div class="sr-callout">

<strong>Principle:</strong> This site is meant to show proof of work, technical depth, and professional thinking without publishing raw submissions, private identifiers, confidential data, or unnecessary sensitive details.

</div>

---

## Privacy-Conscious Public Resume

The public resume available on this site is intentionally different from a direct job-application resume.

It uses:

- `Vlad K.` as the public display name
- a professional contact alias
- broad location only
- no private phone number
- no private personal email address

<div class="sr-project-meta">
  <span class="sr-status sr-status-complete">Public Resume</span>
  <span class="sr-status sr-status-progress">Privacy-Aware</span>
</div>

---

## Professional Contact Alias

This site uses:

[contact@sudorunner.org](mailto:contact@sudorunner.org)

as the public-facing contact email.

The address is configured as a professional forwarding alias through Cloudflare Email Routing. This allows professional contacts to reach me without requiring my private inbox address to be posted directly on the website.

<div class="sr-project-meta">
  <span class="sr-status sr-status-complete">Professional Alias</span>
  <span class="sr-status sr-status-lab">Cloudflare Email Routing</span>
</div>

---

## Redacted Project Publishing

Projects and labs are rewritten into sanitized case studies.

Raw academic files, full solution files, sensitive screenshots, lab credentials, private identifiers, and unnecessary procedural details are not published.

Before publishing project content, I review for:

- full names of classmates, professors, or unrelated individuals
- private email addresses
- phone numbers
- student IDs
- raw screenshots with identifying details
- credentials, secrets, tokens, or keys
- lab-specific IP addresses when not needed
- full exploit instructions or unnecessary offensive detail
- client names or proprietary implementation details
- anything that could violate academic, employer, or client confidentiality

<div class="sr-project-meta">
  <span class="sr-status sr-status-complete">Redacted</span>
  <span class="sr-status sr-status-progress">Portfolio-Safe</span>
</div>

---
## Security Contact Standard

This site includes a public `security.txt` file at:

[/.well-known/security.txt](/.well-known/security.txt)

This provides a standard location for security contact and policy information related to the site.

<div class="sr-project-meta">
  <span class="sr-status sr-status-lab">security.txt</span>
  <span class="sr-status sr-status-complete">Configured</span>
</div>

## Security Headers

This site includes basic security headers through Cloudflare Pages static header configuration.

Configured headers include:

- `X-Frame-Options`
- `X-Content-Type-Options`
- `Referrer-Policy`
- `Permissions-Policy`
- `Cross-Origin-Opener-Policy`

These headers help reduce common browser-side risks such as clickjacking, unnecessary permission exposure, MIME sniffing, and excessive referrer leakage.

<div class="sr-project-meta">
  <span class="sr-status sr-status-lab">Security Headers</span>
  <span class="sr-status sr-status-complete">Configured</span>
</div>

---

## Static Site Deployment

`sudoRunner` is deployed as a static website using Hugo, GitHub, and Cloudflare Pages.

This approach has several security and maintenance advantages:

- no traditional database exposed to the public
- no WordPress-style admin panel
- no server-side login portal
- version-controlled content changes
- automated deployment through Git
- simple rollback through repository history
- fast static hosting through Cloudflare

<div class="sr-project-meta">
  <span class="sr-status sr-status-concept">Static Site</span>
  <span class="sr-status sr-status-complete">Cloudflare Pages</span>
</div>

---

## Content Boundaries

This website does not publish:

- client data
- private employer documents
- internal implementation screenshots
- raw academic submissions
- private contact details
- credentials or secrets
- full exploit walkthroughs
- sensitive infrastructure details

The goal is to demonstrate cybersecurity knowledge, project experience, and technical communication while respecting privacy, confidentiality, and professional boundaries.

---

## Related Pages

<div class="sr-cta-row">
  <a class="sr-button" href="/projects/">Projects</a>
  <a class="sr-button" href="/resume/">Resume</a>
  <a class="sr-button" href="/contact/">Contact</a>
  <a class="sr-button-secondary sr-button" href="/projects/sudorunner-portfolio-website/">sudoRunner Project</a>
</div>