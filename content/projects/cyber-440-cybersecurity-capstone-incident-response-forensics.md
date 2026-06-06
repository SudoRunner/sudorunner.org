---

title: "CYBER 440: Cybersecurity Capstone Incident Response & Forensics"
description: "A portfolio-safe cybersecurity capstone case study focused on incident response, phishing compromise analysis, network forensics, forensic image analysis, memory analysis, log analysis, impact assessment, and remediation planning."
date: 2026-06-05
tags: ["Incident Response", "Digital Forensics", "Network Forensics", "Memory Analysis", "Log Analysis", "Malware Investigation", "Phishing", "Capstone", "Cybersecurity"]
categories: ["Projects"]
showDate: true
showAuthor: false
showReadingTime: true
showWordCount: false
--------------------

<span class="sr-eyebrow">Cybersecurity Capstone</span>

<div class="sr-case-hero">

This portfolio-safe case study summarizes selected CYBER 440 capstone work involving a simulated organizational compromise, phishing-led malware infection, forensic image analysis, network traffic review, memory analysis, log analysis, incident timeline development, impact assessment, and remediation planning.

</div>

<div class="sr-case-summary">

<div class="sr-case-item">
  <span class="sr-case-label">Course</span>
  <span class="sr-case-value">CYBER 440</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Project Type</span>
  <span class="sr-case-value">Cybersecurity Capstone / Incident Response Case Study</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Focus</span>
  <span class="sr-case-value">IR · Digital Forensics · Network Analysis · Memory Analysis · Logs</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Scenario</span>
  <span class="sr-case-value">Simulated Municipal Organization Compromise</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Publishing Level</span>
  <span class="sr-case-value">Portfolio-Safe / Redacted / No Raw Evidence Files</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Professional Angle</span>
  <span class="sr-case-value">Security Operations, Incident Response, and Forensic Reporting</span>
</div>

</div>

## Overview

CYBER 440 was a cybersecurity capstone course focused on investigating a simulated organizational compromise using multiple evidence sources and analyst workflows.

The project required connecting evidence from:

* network captures
* forensic system images
* Windows event logs
* memory artifacts
* suspicious processes
* user activity
* email-based compromise indicators
* ransomware-style artifacts
* malware-related findings
* timeline reconstruction
* business impact analysis
* remediation recommendations

This page presents the work as a portfolio-safe case study. It does not publish raw evidence files, forensic images, full screenshots, private academic submissions, user account details, exact hashes, or sensitive artifacts.

---

## Why This Project Matters

This capstone is valuable because it shows a more complete cybersecurity investigation workflow than a single isolated lab.

A real investigation requires analysts to combine multiple views of the same incident:

* what happened on the network
* what happened on endpoints
* what changed on disk
* what was visible in memory
* what logs support the timeline
* which systems and users were affected
* which attack vector was most likely
* what operational impact occurred
* what should be done next

The project also required communication. Findings had to be converted into a clear status report and final report that could explain the incident, its impact, and recommended remediation steps.

---

## Scenario Summary

The capstone scenario involved a simulated compromise affecting multiple organizational systems.

The investigation identified a phishing-led attack path involving a malicious file disguised as a PDF attachment. The suspected infection chain led to malware execution, suspicious processes, remote-access risk, file deletion, ransom-note artifacts, exposed credentials, failed authentication events, and operational disruption.

The strongest working theory was that a phishing email introduced malware into the environment, after which the compromise affected multiple systems and required coordinated incident response.

---

## Portfolio-Safe Redaction Approach

<div class="sr-callout">

<strong>Security note:</strong> This case study intentionally avoids publishing raw forensic images, packet captures, screenshots, hashes, complete usernames, full email artifacts, private academic files, or step-by-step evidence extraction details.

</div>

This page excludes:

* raw forensic images
* packet capture files
* memory dumps
* full screenshots
* complete raw logs
* exact hashes
* private student identifiers
* full team submissions
* complete academic answers
* sensitive simulated evidence artifacts
* step-by-step replication instructions

Instead, it summarizes:

* investigation workflow
* evidence categories
* technical themes
* analyst reasoning
* incident timeline concepts
* impact assessment
* remediation thinking
* professional lessons learned

---

## Investigation Workflow

<div class="sr-flow">

<div class="sr-flow-step">
  <span class="sr-flow-number">1</span>

### Initial Scope and Evidence Review

Reviewed available evidence sources and identified major analysis tracks: network traffic, forensic images, memory artifacts, and Windows/event log data.

<span class="sr-status sr-status-complete">Scope</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">2</span>

### Network Analysis

Reviewed network captures to identify communication timelines, suspicious email activity, credential exposure concerns, affected systems, and event sequencing.

<span class="sr-status sr-status-lab">Network Forensics</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">3</span>

### Forensic Image Analysis

Analyzed Windows system images, reviewed user directories, downloads, desktop artifacts, application history, suspicious files, and system folders relevant to compromise investigation.

<span class="sr-status sr-status-lab">Disk Forensics</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">4</span>

### Memory Analysis

Reviewed memory-related findings to identify suspicious processes, unknown parent-child process relationships, possible hands-on-keyboard activity, and incomplete or obfuscated process metadata.

<span class="sr-status sr-status-progress">Memory Analysis</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">5</span>

### Log Analysis

Analyzed Windows and server log evidence for failed authentication, anonymous access attempts, service state changes, PTR registration issues, audit failures, and access-related anomalies.

<span class="sr-status sr-status-lab">Log Analysis</span>

</div>

<div class="sr-flow-step">
  <span class="sr-flow-number">6</span>

### Impact and Remediation

Translated technical findings into operational impact, risk exposure, containment priorities, restoration recommendations, and future prevention steps.

<span class="sr-status sr-status-complete">Remediation</span>

</div>

</div>

---

## Evidence Areas

<div class="sr-card-grid">

<div class="sr-card">

### Phishing-Led Compromise

The investigation identified a phishing-style email with a malicious attachment disguised as a PDF as the likely initial compromise path.

<span class="sr-static-label sr-static-label-complete">Initial Access</span>

</div>

<div class="sr-card">

### Malware Execution

The analysis connected the suspicious file activity to malware execution and remote-access risk, including backdoor-style behavior and potential credential exposure.

<span class="sr-static-label sr-static-label-complete">Malware Investigation</span>

</div>

<div class="sr-card">

### Forensic Image Review

Forensic images were reviewed for user directories, desktop artifacts, suspicious downloads, temp folders, application history, event logs, and evidence of encrypted or suspicious files.

<span class="sr-static-label sr-static-label-complete">Disk Forensics</span>

</div>

<div class="sr-card">

### Memory Artifacts

Memory analysis identified suspicious processes, unusual process relationships, missing or incomplete metadata, and indicators that required further investigation.

<span class="sr-static-label sr-static-label-complete">Memory Analysis</span>

</div>

<div class="sr-card">

### Windows and Server Logs

Log review focused on authentication failures, service state changes, PTR registration issues, anonymous access attempts, and server-management anomalies.

<span class="sr-static-label sr-static-label-complete">Log Analysis</span>

</div>

<div class="sr-card">

### Incident Reporting

Findings were summarized into status reports and a final incident report with executive summary, attack vector analysis, impact assessment, and remediation recommendations.

<span class="sr-static-label sr-static-label-complete">Reporting</span>

</div>

</div>

---

## Network Analysis Themes

Network analysis focused on understanding communication patterns and timeline evidence.

Key activities included:

* reviewing network capture time ranges
* identifying email-related activity
* supporting the incident timeline
* looking for suspicious communication patterns
* connecting network evidence to endpoint findings
* identifying potential credential exposure concerns
* mapping communications between affected users and systems

The network evidence helped support the conclusion that the incident was connected to a malicious file delivered through email rather than a simple port manipulation issue.

---

## Forensic Image Analysis Themes

Forensic image analysis focused on endpoint artifacts.

Areas reviewed included:

* user profile directories
* Documents, Downloads, Desktop, and Pictures folders
* Windows system folders
* temporary files
* suspicious executables
* browser and application history
* encrypted or suspicious files
* Windows event log artifacts
* hash verification to confirm image integrity

This portion of the work helped connect user activity, suspicious files, ransomware-style artifacts, and endpoint-level evidence to the broader incident timeline.

---

## Memory Analysis Themes

Memory analysis focused on volatile artifacts and running processes.

The investigation considered:

* suspicious process names
* unknown or missing process metadata
* suspicious parent-child process relationships
* command-line visibility
* process timing
* possible hands-on-keyboard indicators
* potential process obfuscation
* malicious or unknown executable behavior

This reinforced the importance of memory analysis in incident response because disk evidence alone may not fully explain what was happening at runtime.

---

## Log Analysis Themes

Log analysis focused on Windows and server events.

The work included review of:

* failed authentication
* anonymous access attempts
* service start/stop behavior
* PTR registration errors
* audit failures
* network share access attempts
* server-management errors
* suspicious timing correlations
* affected Windows and Windows Server systems

Log evidence helped translate individual artifacts into a broader operational picture.

---

## Impact Assessment

The incident created risk across several dimensions:

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Impact Area</div>
  <div>Observed or Inferred Risk</div>
  <div>Severity</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Confidentiality</div>
  <div class="sr-record-detail">Potential credential exposure, sensitive data access, and remote-access malware risk.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-achievement">High</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Integrity</div>
  <div class="sr-record-detail">Suspicious file changes, ransom-note artifacts, deleted files, and concerns around audit failures or altered system behavior.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-achievement">High</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Availability</div>
  <div class="sr-record-detail">Service disruptions, system instability, file loss, and operational delays affecting IT and business processes.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-achievement">High</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Reputation and Governance</div>
  <div class="sr-record-detail">Potential stakeholder confidence issues, policy concerns, incident response maturity concerns, and possible regulatory or compliance exposure.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-achievement">High</span></div>
</div>

</div>

---

## Remediation Recommendations

The capstone response emphasized both immediate containment and long-term security improvement.

Recommended actions included:

* isolate affected systems
* preserve evidence for forensic review
* conduct complete forensic analysis
* identify all compromised accounts and processes
* remove malware and unauthorized processes
* reset affected passwords
* strengthen authentication
* improve network monitoring
* update security policies
* conduct security awareness training
* perform recurring vulnerability assessments
* update the incident response plan
* document lessons learned
* communicate clearly with stakeholders during recovery

These recommendations are useful because they connect technical findings to operational decision-making.

---

## Capability-to-Evidence Map

<div class="sr-record-list">

<div class="sr-record-row sr-record-head">
  <div>Capability</div>
  <div>Evidence from CYBER 440</div>
  <div>Status</div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Incident Response</div>
  <div class="sr-record-detail">Investigated phishing-led compromise, identified affected systems, built incident timeline, summarized impact, and recommended containment and recovery actions.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Completed</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Network Forensics</div>
  <div class="sr-record-detail">Reviewed network captures, communication timeline, email activity, packet-scale evidence, and suspicious access concerns.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Completed</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Digital Forensics</div>
  <div class="sr-record-detail">Analyzed Windows forensic images, user directories, suspicious files, downloads, desktop artifacts, temp folders, application history, and event logs.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Completed</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Memory Analysis</div>
  <div class="sr-record-detail">Reviewed suspicious processes, process metadata gaps, process relationships, and possible runtime indicators of compromise.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Completed</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Log Analysis</div>
  <div class="sr-record-detail">Reviewed authentication failures, anonymous access attempts, service state changes, PTR issues, audit failures, and server-side anomalies.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Completed</span></div>
</div>

<div class="sr-record-row">
  <div class="sr-record-title">Executive Reporting</div>
  <div class="sr-record-detail">Converted technical findings into executive summary, attack vector analysis, impact analysis, remediation planning, and final incident reporting.</div>
  <div class="sr-record-status"><span class="sr-static-label sr-static-label-complete">Completed</span></div>
</div>

</div>

---

## What I Learned

This capstone reinforced several important cybersecurity lessons:

* incident response requires multiple evidence sources
* phishing remains one of the most effective initial access vectors
* endpoint evidence and network evidence must be correlated
* forensic image analysis helps preserve and reconstruct user/system behavior
* memory analysis can expose runtime artifacts that disk analysis may miss
* logs are essential for timeline reconstruction and access review
* suspicious processes need context from disk, memory, logs, and network data
* impact analysis should include confidentiality, integrity, availability, operations, reputation, and governance
* remediation must include both immediate containment and long-term prevention
* final reporting matters because technical findings must be understandable to decision-makers

---

## Professional Relevance

This project supports roles involving:

* cybersecurity analysis
* security operations
* incident response
* digital forensics
* vulnerability management
* malware investigation
* threat analysis
* security consulting
* governance-aware security reporting

It also supports my ServiceNow SecOps direction because incident response and Vulnerability Response both require structured triage, ownership, remediation tracking, validation, documentation, and stakeholder communication.

---

## Portfolio-Safe Redaction Notes

This case study intentionally excludes:

* raw forensic images
* raw packet captures
* memory dumps
* private screenshots
* complete raw logs
* exact hashes
* private user details
* full academic submissions
* full team report content
* step-by-step evidence extraction details

The goal is to show investigation workflow, reasoning, and security communication without exposing raw evidence or sensitive academic materials.

---

## Related Portfolio Areas

<div class="sr-card-grid">

<div class="sr-card">

### Security Operations

This capstone supports SOC-style work through triage, evidence review, timeline reconstruction, and escalation-oriented reporting.

<span class="sr-static-label sr-static-label-complete">SOC-Relevant</span>

</div>

<div class="sr-card">

### Digital Forensics

The project included forensic image review, endpoint artifact analysis, application history review, suspicious files, and event log review.

<span class="sr-static-label sr-static-label-complete">Forensics</span>

</div>

<div class="sr-card">

### Incident Response

The project required identifying compromise mechanism, affected systems, impact, and immediate/long-term remediation steps.

<span class="sr-static-label sr-static-label-complete">Incident Response</span>

</div>

<div class="sr-card">

### ServiceNow SecOps

The workflow maps naturally to SecOps concepts such as incident triage, ownership, remediation tracking, documentation, and validation.

<span class="sr-static-label sr-static-label-complete">SecOps-Relevant</span>

</div>

</div>

---

## Next Steps

This capstone could later be expanded with:

* a sanitized incident timeline diagram
* a portfolio-safe IR lifecycle diagram
* a detection-to-remediation workflow map
* a ServiceNow Security Incident Response mapping concept
* a lessons-learned table
* a mock executive incident report template

For now, this page serves as the main portfolio-safe summary of my CYBER 440 cybersecurity capstone work.

