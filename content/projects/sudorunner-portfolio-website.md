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
* button-style call-to-action links
* card-based project galleries
* color-coded status badges
* hover effects
* subtle entrance animation
* reusable callout boxes
* consistent visual styling across sections
* custom SVG logo integration
* dark-mode badge contrast tuning
* reusable card and badge design system
* homepage hero customization
* privacy-conscious public resume workflow
* Cloudflare Email Routing for professional contact alias

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

## Content Structure

The website is organized around several major sections:

* About
* Projects
* Research & Labs
* AI & Security
* OT/ICS Security
* Credentials
* Resume
* Contact

This structure was chosen to make the site easy for employers, recruiters, and technical reviewers to navigate.

## What This Project Demonstrates

This project demonstrates practical experience with:

* static website development
* Git-based publishing workflow
* Cloudflare Pages deployment
* custom domain and DNS setup
* privacy-conscious web publishing
* content architecture
* Markdown-based technical writing
* custom CSS design
* project documentation
* employer-facing technical communication

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

## Portfolio Note

This project is included because the website itself demonstrates practical technical work: site generation, deployment, DNS, email routing, content structure, design customization, privacy decisions, and technical writing.
