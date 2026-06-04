---

title: "ICS IT/OT Application-Level DoS Attack Lab"
description: "A redacted academic lab case study focused on investigating and recovering from an application-level denial-of-service attack affecting an ICS/OT environment."
date: 2026-06-04
tags: ["OT/ICS", "SCADA", "Modbus", "Cybersecurity", "Incident Response", "DoS", "Wireshark"]
categories: ["OT/ICS Security"]
showDate: true
showAuthor: false
showReadingTime: true
---------------------

<span class="sr-eyebrow">OT/ICS Case Study</span>

<div class="sr-case-hero">

This case study summarizes a redacted Penn State OT/ICS lab focused on investigating an application-level denial-of-service condition affecting SCADA visibility, identifying the source of disruptive activity, stopping the responsible process, and validating operational recovery.

</div>

<div class="sr-case-summary">

<div class="sr-case-item">
  <span class="sr-case-label">Type</span>
  <span class="sr-case-value">OT/ICS Academic Lab</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Focus</span>
  <span class="sr-case-value">SCADA Visibility Disruption</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Concepts</span>
  <span class="sr-case-value">PLC · Modbus · HMI · DoS</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Role</span>
  <span class="sr-case-value">Incident Investigator</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Outcome</span>
  <span class="sr-case-value">Attack Stopped + Measurements Restored</span>
</div>

<div class="sr-case-item">
  <span class="sr-case-label">Privacy Level</span>
  <span class="sr-case-value">Redacted / No Raw Lab Details Published</span>
</div>

</div>
# ICS IT/OT Application-Level DoS Attack Lab

> **Content Type:** Redacted Academic Lab / OT/ICS Security Case Study
>
> This case study is based on academic lab work completed at Penn State. It has been rewritten and sanitized for portfolio use. It does not include raw screenshots, lab instructions, internal IP details, student identifiers, or step-by-step attack instructions.

## Overview

This lab focused on investigating an application-level denial-of-service condition affecting an ICS/OT environment.

The scenario involved a SCADA-facing environment where normal measured values were disrupted during an attack. The objective was to investigate the source of the disruption, identify the system and process responsible, stop the attack, and confirm that operational measurements returned to normal.

## Why This Lab Matters

OT and ICS environments are different from traditional IT systems because cybersecurity events can affect visibility, uptime, process continuity, and operational decision-making.

In this lab, the issue was not just that network traffic was suspicious. The more important concern was that the SCADA environment stopped displaying expected values during the attack condition. That makes the incident operationally meaningful, not just technically interesting.

## Environment and Concepts

This lab involved concepts related to:

* SCADA monitoring
* HMI client visibility
* PLC communication
* Modbus server connections
* Application-level denial-of-service behavior
* Network connection analysis
* Workstation investigation
* Process identification
* Operational recovery validation

## My Role

For this lab, I acted as the analyst investigating the OT/ICS disruption.

The work involved:

* Observing normal measured values in the SCADA interface
* Identifying the point where measurements stopped displaying correctly
* Reviewing network connections related to the affected PLC
* Determining which workstation generated suspicious connections
* Investigating processes responsible for the connections
* Stopping the malicious activity in the lab environment
* Confirming that measured values returned to normal after remediation

## Investigation Summary

### 1. Establishing Normal Conditions

The lab began by observing normal measured values in the SCADA interface.

This step was important because the analyst needed a baseline before determining whether the environment was degraded or disrupted.

### 2. Observing the Disruption

After the attack condition began, the SCADA interface stopped displaying the expected values.

From an OT perspective, this is significant because loss of visibility can interfere with operator awareness, monitoring, and operational confidence.

### 3. Reviewing Network Connections

The next phase focused on examining active network connections involving the affected PLC and Modbus communication.

The investigation showed that additional connections were interfering with normal communication behavior.

### 4. Identifying the Suspect Workstation

The lab required tracing the suspicious connections back to the system responsible for generating the traffic.

This step demonstrated the importance of moving from symptom-level observation to source identification.

### 5. Identifying the Responsible Process

After identifying the suspect system, the next step was to determine which running process was responsible for the network activity.

This reinforced an important incident response principle: identifying the host is not enough. The analyst also needs to understand what process or program is causing the behavior.

### 6. Stopping the Attack and Validating Recovery

After stopping the responsible activity in the lab environment, the SCADA interface was checked again to confirm that measured values returned to normal.

This validation step matters because remediation should not stop at “the suspicious process was killed.” In an OT/ICS context, the analyst must confirm that operational visibility and expected behavior have been restored.

## What This Lab Demonstrates

This lab demonstrates hands-on academic exposure to:

* OT/ICS incident investigation
* SCADA visibility concerns
* PLC and Modbus communication concepts
* Application-level denial-of-service impact
* Network connection review
* Suspect workstation identification
* Malicious process investigation
* Recovery validation
* Translating technical evidence into operational impact

## Lessons Learned

The most important lesson from this lab is that OT/ICS security requires both technical investigation and operational awareness.

In a traditional IT environment, a denial-of-service event may be discussed primarily in terms of service availability. In an OT/ICS environment, the same kind of disruption can affect operator visibility, monitoring confidence, and process awareness.

This lab also reinforced the importance of validating recovery. Stopping suspicious activity is only one part of incident response. Analysts also need to confirm that the affected system or process has returned to expected behavior.

## What I Would Improve

If I expanded this lab into a larger portfolio project, I would add:

* A simplified network diagram
* A defensive detection summary
* A short incident response timeline
* A mapping of observed behavior to OT/ICS risk
* A high-level detection logic concept
* A recovery checklist for similar SCADA visibility issues
* A comparison between IT-style DoS impact and OT/ICS operational impact

## Portfolio Note

This page is intentionally written as a sanitized case study. The original lab report is not published because it contains course metadata, screenshots, lab-specific details, and raw procedural content that is not necessary for employer review.

The goal is to demonstrate understanding of OT/ICS security investigation, operational impact, and recovery validation without exposing unnecessary technical or academic details.
