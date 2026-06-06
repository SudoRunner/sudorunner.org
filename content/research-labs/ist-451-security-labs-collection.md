---
title: "IST 451: Security Labs Collection"
description: "A portfolio-safe academic security lab collection covering defensive analysis, secure configuration, vulnerability assessment, incident investigation, network security, OT/ICS security, and controlled lab-based security testing."
showDate: false
showAuthor: false
showReadingTime: true
showWordCount: false
---
> **Content Type:** Redacted Academic Lab Collection
>
> This collection is based on academic cybersecurity lab work completed at Penn State. It has been rewritten and sanitized for portfolio use. It does not include raw screenshots, student identifiers, lab IP addresses, credentials, full commands, exploit steps, or procedural offensive details.

## Overview

This lab collection represents hands-on cybersecurity coursework focused on defensive analysis, secure configuration, vulnerability assessment, incident investigation, network security, OT/ICS security, and controlled lab-based security testing.

The goal of this page is to summarize the technical breadth of the lab work without publishing raw submissions or step-by-step attack instructions.

## Lab Coverage

### Service Identification

This lab focused on identifying services and host characteristics in a controlled network environment.

Key concepts included:

* TCP scanning
* UDP scanning
* NetBIOS information gathering
* operating system identification
* interpreting network service exposure

### Secure Apache Web Server Configuration

This lab focused on web server hardening concepts using Apache.

Key concepts included:

* secure configuration review
* reducing unnecessary exposure
* web server security controls
* configuration validation
* defensive system administration

### Vulnerability Scanning with OpenVAS

This lab focused on vulnerability assessment using OpenVAS.

Key concepts included:

* vulnerability scanning
* interpreting scanner results
* identifying exposed services
* reviewing severity and remediation context
* understanding how vulnerability findings support risk reduction

### SQL Injection Detection and Exploitation Concepts

This lab focused on understanding SQL injection risk in a controlled academic environment.

Key concepts included:

* input validation weaknesses
* database-backed web application risk
* identifying injection behavior
* understanding impact
* defensive lessons for secure application design

This lab is summarized at a high level only. The purpose is to demonstrate application security awareness, not to publish exploit instructions.

### Malware-Based Attack Investigation

This lab focused on investigating and neutralizing suspicious traffic caused by a malware-based attack in a controlled environment.

Key concepts included:

* firewall log review
* suspicious traffic blocking
* host investigation
* packet capture review
* source spoofing indicators
* malicious process identification
* ARP scan behavior
* containment and validation

A dedicated sanitized case study is available here:

[Malware-Based Attack Investigation and Neutralization Lab](/projects/malware-based-attack-investigation-lab/)

### ICS IT/OT Application-Level DoS Investigation

This lab focused on an application-level denial-of-service condition affecting a SCADA/OT environment.

Key concepts included:

* RapidSCADA visibility
* HMI monitoring
* PLC communication
* Modbus server connections
* identifying the suspect workstation
* process investigation
* stopping disruptive activity
* validating that measured values returned to normal

A dedicated sanitized case study is available here:

[ICS IT/OT Application-Level DoS Attack Lab](/ot-ics-security/ics-it-ot-application-level-dos-lab/)

### Intro IDS Configuration with Snort

This lab focused on introductory intrusion detection system configuration using Snort.

Key concepts included:

* IDS configuration
* rule-based detection concepts
* alerting logic
* network monitoring
* understanding how detection supports security operations

### Firewall Configuration with iptables

This lab focused on firewall rule configuration using iptables.

Key concepts included:

* packet filtering
* traffic allow/block decisions
* rule ordering
* host-based firewall logic
* basic Linux network security controls

### Wireless Security and 4-Way Handshake Concepts

This lab focused on wireless security concepts in a controlled academic environment.

Key concepts included:

* wireless authentication
* EAPOL traffic review
* 4-way handshake analysis
* Wireshark packet inspection
* password security considerations
* wireless defensive lessons

This lab is summarized at a high level only. The goal is to demonstrate understanding of wireless security mechanics and defensive implications.

### Controlled Capture-the-Flag Scenario

This lab involved a controlled CTF-style environment used to practice security testing methodology.

Key concepts included:

* network discovery
* service enumeration
* web path discovery
* credential risk awareness
* post-compromise impact understanding
* privilege escalation concepts
* security testing documentation

This lab is intentionally summarized without procedural details, commands, payloads, or exploitation steps. The purpose is to show controlled lab exposure and security testing awareness, not to provide instructions.

## Skills Demonstrated

Across the lab collection, these exercises demonstrate hands-on exposure to:

* network reconnaissance
* service identification
* vulnerability scanning
* web application security
* malware investigation
* packet analysis
* firewall rule configuration
* IDS concepts
* OT/ICS security investigation
* wireless security fundamentals
* incident response thinking
* security testing methodology
* defensive validation and documentation

## Defensive Takeaways

Several important cybersecurity lessons stood out across the labs.

First, visibility matters. Tools such as packet captures, firewall logs, IDS alerts, vulnerability scans, and host-level process review each provide a different view of security activity.

Second, findings need context. A scanner result, open service, suspicious packet, or unusual process is only useful when an analyst can connect it to risk, ownership, and next steps.

Third, controlled offensive labs can strengthen defensive understanding. Learning how attacks work in a safe lab environment helps security professionals better understand prevention, detection, containment, and recovery.

Fourth, OT/ICS environments require operational awareness. Security events in industrial or cyber-physical environments can affect visibility, uptime, process continuity, and operator confidence.

## Portfolio Note

This page is intentionally written as a sanitized academic lab collection. The original lab reports are not published because they contain course metadata, screenshots, lab-specific infrastructure details, and procedural content that is not necessary for employer review.

The purpose of this collection is to show technical breadth, hands-on cybersecurity exposure, and the ability to translate lab work into professional security lessons.


