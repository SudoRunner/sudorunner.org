---

title: "sudoRunner Portfolio Website"
description: "A professional cybersecurity portfolio website built with Hugo, Blowfish, GitHub, Cloudflare Pages, custom DNS, email routing, and a custom design layer."
date: 2026-06-04
tags: ["Hugo", "Cloudflare Pages", "GitHub", "Web Design", "Portfolio", "Static Site", "DNS", "Cybersecurity"]
categories: ["Projects"]
showDate: true
showAuthor: false
showReadingTime: true
---------------------

<span class="sr-eyebrow">Portfolio Case Study</span>

<div class="sr-case-hero">

This case study documents the design, build, deployment, and security-conscious publishing decisions behind `sudoRunner`, a professional cybersecurity portfolio built with Hugo, Blowfish, GitHub, Cloudflare Pages, custom DNS, Email Routing, custom CSS, and portfolio-safe content architecture.

</div>

<div class="sr-case-summary">

<div class="sr-case-item">
  <span class="sr-case-label">Type</span>
  <span class="sr-case-value">Personal Web Project</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Focus</span>
  <span class="sr-case-value">Cybersecurity Portfolio Infrastructure</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Role</span>
  <span class="sr-case-value">Site Builder / Content Architect</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Stack</span>
  <span class="sr-case-value">Hugo · Blowfish · GitHub · Cloudflare</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Outcome</span>
  <span class="sr-case-value">Live Professional Portfolio</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Security Focus</span>
  <span class="sr-case-value">Privacy-Aware Public Publishing</span>
</div>

</div>

# sudoRunner Portfolio Website

> **Content Type:** Personal Web Project / Portfolio Infrastructure
>
> This project documents the design and build process behind `sudoRunner`, my professional cybersecurity portfolio website.

## Overview

`sudoRunner` is a professional portfolio website built to showcase cybersecurity projects, ServiceNow SecOps labs, AI security concept notes, OT/ICS security interests, credentials, resume access, and redacted academic case studies.

The site was built as a static website using Hugo and the Blowfish theme, with deployment through GitHub and Cloudflare Pages.

## Project Goals

The goal was to create a clean, employer-facing portfolio that could:

* present selected cybersecurity projects
* organize hands-on labs and technical notes
* showcase ServiceNow SecOps and Vulnerability Response knowledge
* highlight OT/ICS security interests
* host a public resume safely
* provide a professional contact email
* avoid exposing private personal information
* demonstrate technical depth beyond a traditional resume

## Technologies Used

This project used:

* Hugo static site generator
* Blowfish Hugo theme
* Git and GitHub
* GitHub Desktop
* Cloudflare Pages
* Cloudflare DNS
* Cloudflare Email Routing
* Custom domain configuration
* Markdown content structure
* Custom CSS
* Responsive card layouts
* Status badges
* Hover effects
* Portfolio-safe content redaction

## Architecture

The site follows a simple static deployment model:

```text
Local Hugo project
→ GitHub repository
→ Cloudflare Pages build
→ sudorunner.org custom domain
```

Content is written locally in Markdown, committed to GitHub, and automatically deployed through Cloudflare Pages.

## Design Features

The site includes a custom design layer built on top of the Blowfish theme.

Custom features include:

* compact homepage landing page
* custom SVG terminal-style logo
* button-style call-to-action links
* Start Here portfolio review workflow
* vertical guided review path with directional arrows
* card-based project galleries
* color-coded status badges
* bright academic honor styling for Cum Laude
* dark-mode badge contrast tuning
* hover effects on cards and buttons
* subtle entrance animation
* reusable callout boxes
* consistent visual styling across sections
* privacy-conscious public resume workflow
* professional email alias through Cloudflare Email Routing
* apple-style desktop dropdown navigation
* custom section and single-page layouts
* software foundations project integration



## Privacy-Conscious Design

A major part of this project was designing the site to be public while reducing unnecessary personal exposure.

Privacy decisions included:

* using `Vlad K.` as the public display name
* omitting private phone number from the public resume
* omitting private email from the public resume
* using `contact@sudorunner.org` as a professional forwarding address
* avoiding raw publication of academic files
* rewriting projects as sanitized case studies
* excluding student names, professor names, screenshots, credentials, lab IPs, and full solution files
* publishing a dedicated [Security & Privacy](/security-privacy/) statement explaining public resume, contact alias, redaction, and security header practices

## Content Structure

The website is organized around several major sections:

- About
- Start Here workflow
- Projects
- Research & Labs
- AI & Security
- OT/ICS Security
- Software Foundations
- Credentials
- Resume
- Contact
- Security & Privacy

This structure was chosen to make the site easy for employers, recruiters, and technical reviewers to navigate. The site leads with ServiceNow SecOps and cybersecurity work while also showing supporting technical foundations such as Java, object-oriented programming, data structures, Git workflow, and web design.

## What This Project Demonstrates

This project demonstrates practical experience with:

* static website development
* Git-based publishing workflow
* Cloudflare Pages deployment
* custom domain and DNS setup
* Cloudflare Email Routing
* Hugo and Blowfish configuration
* Markdown-based content management
* custom CSS design system
* SVG logo integration
* card-based UI layout
* reusable badge components
* responsive workflow design
* privacy-conscious web publishing
* public resume hosting
* content architecture
* technical writing
* project documentation
* employer-facing portfolio design


## Lessons Learned

Building this site reinforced the importance of structure, clarity, and privacy.

A portfolio is not just a place to upload files. It needs to guide the reader, explain the work, protect sensitive details, and show technical depth without overwhelming the visitor.

This project also reinforced how useful static websites can be for cybersecurity professionals. A fast, simple, version-controlled site is easier to maintain, easier to secure, and easier to customize than many heavier website platforms.

## What I Would Improve Next

Future improvements may include:

* adding a real scheduling link for intro calls
* adding a protected contact form
* improving mobile spacing
* adding diagrams for selected projects
* adding sanitized screenshots where appropriate
* adding more ServiceNow SecOps lab content
* adding more OT/ICS security notes
* adding a changelog-style page for site improvements
* improving accessibility and metadata
* maintaining a public [Changelog](/changelog/) to document portfolio improvements over time

## Portfolio Note

This project is included because the website itself demonstrates practical technical work: site generation, deployment, DNS, email routing, content structure, design customization, privacy decisions, and technical writing.
