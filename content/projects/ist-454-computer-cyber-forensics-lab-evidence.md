---

title: "IST 454: Computer & Cyber Forensics Lab Evidence"
description: "A portfolio-safe academic case study focused on computer and cyber forensics, forensic image creation, forensic image mounting, hash verification, registry analysis, data carving, deleted file recovery, IoT forensics, and AI-assisted forensic research."
date: 2026-06-05
tags: ["Digital Forensics", "Computer Forensics", "Cyber Forensics", "FTK Imager", "WinHex", "RegRipper", "Registry Analysis", "Data Carving", "Forensic Imaging", "IoT Forensics", "AI Forensics"]
categories: ["Projects"]
showDate: true
showAuthor: false
showReadingTime: true
showWordCount: false
--------------------

<span class="sr-eyebrow">Computer & Cyber Forensics Case Study</span>

<div class="sr-case-hero">

This portfolio-safe case study summarizes selected IST 454 Computer and Cyber Forensics work focused on forensic image creation, forensic image mounting, hash verification, Windows registry analysis, data carving, deleted file recovery, IoT forensics, and AI-assisted security/forensics research.

</div>

<div class="sr-case-summary">

<div class="sr-case-item">
  <span class="sr-case-label">Course</span>
  <span class="sr-case-value">IST 454</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Project Type</span>
  <span class="sr-case-value">Computer & Cyber Forensics Lab Evidence</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Focus</span>
  <span class="sr-case-value">Forensic Imaging · Registry Analysis · Data Carving · Reporting</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Tools / Platforms</span>
  <span class="sr-case-value">FTK Imager · WinHex · RegRipper · Registry Viewer · Kali Linux · dcfldd</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Research Angle</span>
  <span class="sr-case-value">AI Security Datasets · IoT Forensics · Multi-Source Evidence</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Publishing Level</span>
  <span class="sr-case-value">Portfolio-Safe / Partial Evidence / No Raw Images Published</span>
</div>

</div>

## Overview

IST 454 focused on computer and cyber forensics. The available evidence from this course supports a portfolio-safe summary around digital evidence handling, forensic image creation, forensic image mounting, hash verification, registry analysis, deleted file recovery, data carving, and research into AI/IoT forensics.

I do not currently have every original lab submission from this course. Because of that, this page is intentionally framed as **selected lab evidence**, not a complete course archive.

The strongest evidence available includes:

* Windows forensic image creation and mounting
* Kali Linux disk image creation and hashing
* MD5 and SHA256 hash comparison
* read-only image handling
* Windows registry hive recovery and analysis
* SAM, SYSTEM, and NTUSER registry review concepts
* RegRipper usage
* deleted image recovery
* deleted document recovery
* WinHex data carving
* file recovery by type
* group analysis of recovered documents and encrypted file indicators
* research on AI-based cybersecurity and forensics datasets
* discussion of IoT forensics, proprietary data formats, privacy, and investigation challenges

This page is intentionally written as a sanitized case study. It does not publish raw forensic images, full screenshots, complete lab answers, raw recovered documents, private academic submissions, passwords, case artifacts, or full evidence files.

---

## Why This Project Matters

Digital forensics is one of the clearest bridges between cybersecurity operations and evidence-based investigation.

A useful forensic workflow needs to preserve evidence, maintain integrity, recover relevant artifacts, analyze system state, and communicate findings clearly.

This course supports several cybersecurity capabilities:

* evidence preservation
* forensic acquisition
* image mounting
* hash verification
* read-only analysis discipline
* registry analysis
* user activity review
* deleted file recovery
* data carving
* forensic reporting
* AI/IoT forensic research awareness

This matters for security operations because incidents often require more than alert triage. Analysts may need to understand what happened on a system, what files existed, what was deleted, what devices were connected, what user activity occurred, and whether evidence was handled correctly.

---

## Portfolio-Safe Publishing Approach

<div class="sr-callout">

<strong>Security and privacy note:</strong> This page summarizes forensic lab evidence without publishing raw forensic images, recovered files, complete reports, passwords, full screenshots, private student identifiers, or detailed evidence artifacts.

</div>

This page excludes:

* raw forensic images
* mounted disk image contents
* full recovered files
* recovered images or documents
* registry hive files
* exact lab passwords
* private screenshots
* full group submissions
* raw academic answers
* private course materials
* complete step-by-step instructions

Instead, it presents:

* forensic workflows
* tools used
* evidence categories
* portfolio-safe technical summaries
* professional lessons learned
* relevance to incident response and security operations

---

## Evidence-Based Scope

Because not every lab file is available, this page uses a conservative evidence scope.

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Available Evidence</div>
  <div>What It Supports</div>
  <div>Confidence</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Windows Image Creation and Mounting Lab</div>
  <div class="sr-record-detail">Supports forensic image creation, E01 image output, verification, mounting, and read-only forensic access using FTK Imager.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Strong</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Kali Linux Image Creation and Hashing Lab</div>
  <div class="sr-record-detail">Supports Linux partition identification, dcfldd-based disk imaging, MD5/SHA256 hash generation, read-only image handling, and hash comparison for integrity verification.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Strong</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Windows Registry Analysis Lab</div>
  <div class="sr-record-detail">Supports registry hive recovery and analysis, including SAM, SYSTEM, USBSTOR, NTUSER.DAT, Registry Viewer, and RegRipper-based user activity review.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Strong</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Windows Data Carving Lab</div>
  <div class="sr-record-detail">Supports forensic image mounting, WinHex-based recovery by type, deleted image recovery, deleted document recovery, and output organization.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Strong</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Group Lab 5 Evidence</div>
  <div class="sr-record-detail">Supports applied document recovery, repeated content identification, missing file reasoning, encrypted file observation, and analysis using FTK/WinHex outputs.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Moderate</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">AI / IoT Forensics Research Essay</div>
  <div class="sr-record-detail">Supports research into AI-based security datasets, heterogeneous telemetry sources, IoT forensics, privacy issues, intrusion detection, digital forensics, and AI-assisted security analysis.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Strong</span></div>
</div>

</div>

---

## Forensic Workflow Map

<div class="sr-flow">

<div class="sr-flow-step">
  <span class="sr-flow-number">1</span>

### Identify and Preserve Evidence

Forensic work began with identifying disks, partitions, evidence sources, and target images while avoiding unnecessary alteration of original evidence.

<span class="sr-status sr-status-complete">Preservation</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">2</span>

### Create Forensic Images

Created forensic images using FTK Imager and dcfldd-style workflows, including compressed forensic image formats and disk image output.

<span class="sr-status sr-status-lab">Acquisition</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">3</span>

### Verify Integrity

Used hash generation and hash comparison, including MD5 and SHA256-style validation, to confirm image integrity and support evidence reliability.

<span class="sr-status sr-status-progress">Hash Verification</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">4</span>

### Mount Images Read-Only

Mounted forensic images read-only so analysis could be performed without modifying the evidence source.

<span class="sr-status sr-status-lab">Read-Only Analysis</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">5</span>

### Recover and Analyze Artifacts

Recovered registry hives, reviewed user/system registry data, carved deleted images and documents, and examined recovered artifacts.

<span class="sr-status sr-status-lab">Artifact Recovery</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">6</span>

### Report Findings

Converted forensic observations into portfolio-safe findings, including recovered file categories, registry analysis relevance, and research implications.

<span class="sr-status sr-status-complete">Reporting</span>

</div>

</div>

---

## Forensic Imaging Evidence

The course evidence includes both Windows and Linux imaging workflows.

The Windows imaging lab involved:

* launching FTK Imager
* creating a forensic image
* selecting evidence source type
* choosing an E01-style image output
* entering case/evidence/examiner metadata
* saving the image to a case folder
* verifying the image
* mounting the forensic image
* selecting a drive letter
* confirming read-only mounting
* preparing the mounted image for later analysis

The Kali Linux imaging lab involved:

* identifying partitions
* selecting a target partition
* creating a disk image using `dcfldd`
* generating MD5 and SHA256 hash logs during imaging
* setting the resulting image to read-only
* hashing the original source for comparison
* discussing hash comparison and evidence integrity

The key lesson is that forensic analysis should be performed on an acquired image rather than directly on original evidence, and that hashing supports evidence integrity.

---

## Registry Analysis Evidence

The registry analysis lab supported Windows forensic analysis concepts.

The available evidence includes work around:

* recovering registry hives
* exporting SAM and SYSTEM files
* analyzing SAM with Registry Viewer
* reviewing user account information
* analyzing SYSTEM registry data
* identifying connected USB device artifacts through USBSTOR
* recovering NTUSER.DAT
* using RegRipper to analyze NTUSER data
* searching for recently opened files
* using registry artifacts to infer user or system activity

This is relevant because the Windows registry can contain important evidence about user behavior, connected devices, account information, system configuration, and recent activity.

---

## Data Carving Evidence

The data carving lab focused on recovering deleted files from a mounted forensic image.

The available evidence includes:

* mounting an image with FTK Imager
* opening the physical storage device in WinHex
* recovering deleted images by file type
* creating output folders for carved pictures
* recovering deleted documents by file type
* using free cluster and sector boundary search settings
* reviewing recovered output
* organizing recovery results

This supports a practical understanding of deleted file recovery and forensic artifact extraction.

---

## Data recovery from a mounted forensic image

The data recovery lab focused on a "Company Secrets" case involving recovered documents and file artifacts which needed to be investigated, and certain information had to be extracted.

The available evidence supports:

* recovered document review
* identifying repeated content
* recognizing missing file numbers
* identifying a file with mRNA-related content
* observing encrypted file indicators
* noting an OLE2 encrypted file type
* connecting recovered artifacts to FTK and WinHex outputs

---

## AI and IoT Forensics Research

The research essay focused on AI as it relates to cybersecurity and forensics.

The essay discussed:

* AI-based security applications
* TON_IoT Windows datasets
* heterogeneous telemetry
* Windows and Linux operating system data
* network traffic data
* IoT service data
* intrusion detection
* threat intelligence
* privacy preservation
* digital forensics
* limitations of homogeneous datasets
* multi-faceted attacks
* overfitting and incomplete feature sets
* labeled datasets with ground truth
* correlation analysis
* energy and scalability considerations for AI systems

This research angle matters because modern forensics increasingly depends on large-scale, multi-source evidence. IoT, cloud, endpoint, and network telemetry create both opportunities and challenges for investigators.

---

## IoT Forensics Discussion Evidence

The available discussion work addressed IoT forensics and the difficulty of investigating connected devices.

Themes included:

* IoT devices generating large volumes of data
* cloud-based device data
* proprietary vendor formats
* multi-tenant cloud infrastructure
* multi-jurisdictional evidence concerns
* end-to-end encryption
* privacy of smart car occupants
* insecure or poorly secured connected devices
* use of tools such as Splunk to aggregate different evidence sources
* need for broader visibility across logs, APIs, files, directories, and network events

This supports the broader forensic theme that modern investigations often require multi-source evidence handling and privacy-aware analysis.

---

## Tools and Techniques Referenced

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Tool / Technique</div>
  <div>Forensic Purpose</div>
  <div>Evidence Type</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">FTK Imager</div>
  <div class="sr-record-detail">Forensic image creation, evidence source selection, E01-style output, verification, image mounting, and read-only access.</div>
  <div class="sr-record-status"><span class="sr-static-label">Imaging</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">dcfldd</div>
  <div class="sr-record-detail">Linux disk image creation with hash generation and error-handling options during acquisition.</div>
  <div class="sr-record-status"><span class="sr-static-label">Acquisition</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">MD5 / SHA256 Hashing</div>
  <div class="sr-record-detail">Evidence integrity validation through hash generation and comparison.</div>
  <div class="sr-record-status"><span class="sr-static-label">Integrity</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Registry Viewer</div>
  <div class="sr-record-detail">SAM and SYSTEM registry hive analysis for account and system artifact review.</div>
  <div class="sr-record-status"><span class="sr-static-label">Registry</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">RegRipper</div>
  <div class="sr-record-detail">NTUSER.DAT analysis and user activity artifact extraction.</div>
  <div class="sr-record-status"><span class="sr-static-label">User Activity</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">WinHex</div>
  <div class="sr-record-detail">Opening mounted forensic images, recovering deleted images and documents, and carving files by type.</div>
  <div class="sr-record-status"><span class="sr-static-label">Data Carving</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Splunk / Multi-Source Telemetry Concepts</div>
  <div class="sr-record-detail">Discussion of aggregating logs, files, directories, network events, and APIs for broader forensic and security visibility.</div>
  <div class="sr-record-status"><span class="sr-static-label">Telemetry</span></div>
</div>

</div>

---

## Capability-to-Evidence Map

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Capability</div>
  <div>Evidence from IST 454</div>
  <div>Status</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Forensic Acquisition</div>
  <div class="sr-record-detail">Created Windows and Linux forensic images, used FTK Imager and dcfldd-style workflows, and reviewed image output and read-only handling.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Evidence Available</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Evidence Integrity</div>
  <div class="sr-record-detail">Generated and compared MD5 and SHA256 hashes to validate forensic image integrity.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Evidence Available</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Registry Analysis</div>
  <div class="sr-record-detail">Recovered and analyzed SAM, SYSTEM, and NTUSER registry hives using Registry Viewer and RegRipper-style workflows.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Evidence Available</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Data Carving</div>
  <div class="sr-record-detail">Recovered deleted images and documents from a mounted forensic image using WinHex and file recovery by type.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Evidence Available</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Artifact Review</div>
  <div class="sr-record-detail">Reviewed recovered document content, repeated files, missing file references, encrypted file indicators, and file-type observations.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Supporting Evidence</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">AI / IoT Forensics Research</div>
  <div class="sr-record-detail">Researched AI-based security datasets, IoT telemetry, heterogeneous data sources, privacy preservation, IDS, threat intelligence, and forensic investigation challenges.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Research Evidence</span></div>
</div>

</div>

---

## Professional Lessons Learned

This course reinforced several lessons that matter for cybersecurity and incident response:

* evidence should be acquired and analyzed carefully, not altered directly
* forensic images should be mounted read-only when possible
* hashing supports evidence integrity and repeatability
* deleted files may still be recoverable through data carving
* registry artifacts can reveal user activity, connected devices, and system state
* forensic investigation often requires multiple tools
* modern investigations increasingly involve IoT, cloud, and large-scale telemetry
* proprietary data formats and encryption can complicate analysis
* AI datasets may help security teams, but data quality and feature completeness matter
* forensic reporting should clearly separate evidence, inference, and uncertainty

---

## Professional Relevance

This project supports roles involving:

* cybersecurity analysis
* digital forensics
* incident response
* security operations
* malware investigation
* endpoint investigation
* GRC-aware evidence handling
* forensic reporting
* IoT security awareness
* AI-assisted security research

It also complements my CYBER 440 capstone work. CYBER 440 demonstrates a broader simulated incident investigation; IST 454 adds dedicated computer and cyber forensics evidence around image acquisition, registry analysis, deleted file recovery, and forensic research.

---

## Difference from CYBER 440

IST 454 and CYBER 440 overlap, but they show different strengths.

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Course</div>
  <div>Main Portfolio Angle</div>
  <div>Best Evidence Type</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">IST 454</div>
  <div class="sr-record-detail">Forensic imaging, hash verification, registry analysis, deleted file recovery, data carving, IoT forensics, and AI-assisted forensic research.</div>
  <div class="sr-record-status"><span class="sr-static-label">Digital Forensics</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">CYBER 440</div>
  <div class="sr-record-detail">Simulated incident response capstone involving network evidence, forensic images, memory artifacts, logs, timeline development, and remediation planning.</div>
  <div class="sr-record-status"><span class="sr-static-label">IR Capstone</span></div>
</div>

</div>

Together, they show both focused forensic technique exposure and broader incident investigation workflow.

---

## Portfolio-Safe Redaction Notes

This case study intentionally excludes:

* raw forensic images
* mounted image contents
* recovered documents and images
* registry hive files
* exact passwords
* full screenshots
* full lab submissions
* complete group reports
* private academic records
* step-by-step lab procedures
* complete source evidence

The purpose is to show digital forensics knowledge and investigation workflow without exposing raw evidence or academic materials.

---

## Related Portfolio Areas

<div class="sr-card-grid">

<div class="sr-card">

### Digital Forensics

This work supports forensic acquisition, evidence integrity, image mounting, registry analysis, deleted file recovery, and artifact review.

<span class="sr-static-label sr-static-label-complete">Forensics</span>

</div>

<div class="sr-card">

### Incident Response

Forensic evidence handling supports incident triage, root-cause analysis, timeline reconstruction, and evidence-based reporting.

<span class="sr-static-label sr-static-label-complete">IR-Relevant</span>

</div>

<div class="sr-card">

### Security Operations

Security analysts benefit from understanding file recovery, registry artifacts, logs, telemetry, and endpoint evidence.

<span class="sr-static-label sr-static-label-complete">SOC-Relevant</span>

</div>

<div class="sr-card">

### AI and IoT Forensics

The research work connects forensic thinking to AI datasets, IoT telemetry, privacy, data volume, and multi-source investigation challenges.

<span class="sr-static-label sr-static-label-complete">Emerging Forensics</span>

</div>

</div>

---

## Next Steps

This project can later be connected to:

* the cybersecurity analyst review path
* the digital forensics capability section
* the CYBER 440 capstone page
* an incident-response evidence lifecycle diagram
* a forensic imaging checklist
* a registry analysis concept note
* a data carving concept note
* an AI/IoT forensics research section

For now, this page serves as the main portfolio-safe summary of my IST 454 computer and cyber forensics evidence.

