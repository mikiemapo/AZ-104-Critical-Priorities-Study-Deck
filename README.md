# AZ-104 Critical Priorities Study Deck

## 📂 Repository Structure

```
AZ-104-Critical-Priorities-Study-Deck/
├── Topic-Based-Decks/           # Comprehensive topic deep-dive CSV decks
│   ├── AZ104_Golden_Rule_Enriched_Part1_FULL.csv
│   ├── AZ104_Golden_Rule_Enriched_Part2_FULL.csv
│   ├── AZ104_VMSS_DeepDive.csv
│   ├── AZ104_App_Service_DeepDive.csv
│   ├── AZ104_Resilience_DR_DeepDive.csv
│   ├── AZ104_Hybrid_Azure_Mastery_DeepDive.csv
│   ├── AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv
│   └── AZ104_VABRF_Operational_Resilience_DeepDive.csv
│
├── Personalized-Review-Decks/   # Custom decks from quiz weak spots
│   └── Microsoft_Entra_ID_Cheat_Sheet.csv (48 cards - Tutorials Dojo)
│
├── Study-Calendars/             # ICS calendar files for study scheduling
│   ├── AZ104_Integrated_Study_Schedule.ics (Tutorials Dojo + Anki + Whizlabs)
│   ├── AZ104_Study_Schedule.ics
│   └── AZ104_Study_Schedule_DETAILED.ics
│
├── AZ-104-Master-Questions.csv  # Master deck database (465 cards)
└── AZ-104-Master-Study-Deck.apkg # Compiled hierarchical Anki deck

```

## 🎴 Deck Types

### 1. **Master Study Deck** (465 cards - Hierarchical)
- **File**: `AZ-104-Master-Study-Deck.apkg`
- **Purpose**: Comprehensive AZ-104 coverage with subdeck organization
- **Import**: Import once, all batches included as subdecks
- **Use Case**: Full exam preparation, topic-by-topic study

### 2. **Topic-Based Decks** (Standalone CSV files)
- **Location**: `Topic-Based-Decks/`
- **Purpose**: Deep-dive study on specific topics (Golden Rules, VMSS, App Service, etc.)
- **Import**: Import individually as separate Anki decks
- **Use Case**: Targeted review when weak on specific topics

### 3. **Personalized Review Decks** (From quiz weak spots)
- **Location**: `Personalized-Review-Decks/`
- **Purpose**: Custom flashcards generated from quiz results
- **Import**: Import as separate decks for spaced repetition
- **Current Decks**:
  - **Microsoft Entra ID Cheat Sheet** (48 cards from Tutorials Dojo cheat sheet)
- **Use Case**: Targeted weak spot review with spaced repetition

### 4. **Study Calendars**
- **Location**: `Study-Calendars/`
- **Purpose**: Integrated study schedules combining quizzes, Anki, and labs
- **Use**: Import into Calendar app (macOS, Google Calendar, Outlook)
- **Current Calendars**:
  - **AZ104_Integrated_Study_Schedule.ics** - Tutorials Dojo quizzes + Anki reviews + Whizlabs CLI labs (6-week timeline)

---

## ⚠️ CRITICAL WORKFLOW FOR AI ASSISTANT

**BEFORE adding new questions, ALWAYS:**

1. **Verify question content** - Confirm topic matches user's request (e.g., Container Security vs FD-UD)
2. **Check for duplicates** - Run `grep -n "keyword" AZ-104-Master-Questions.csv` to avoid duplicates
3. **Append to CSV** - Add to END of AZ-104-Master-Questions.csv (never replace entire file)
4. **Keep explanations to 2 sentences MAXIMUM** - Critical for maintaining study flow and preventing cognitive overload
5. **Cross-reference MS Learn** - Add MS Learn source link to the MS Learn References section at bottom of README
6. **Regenerate deck** - Run `python3 create_master_deck.py` after CSV changes
7. **Update README** - Update card count and batch list in this file
8. **Commit with details** - Use descriptive commit message with topic and count

**For Personalized Review Decks (from quiz weak spots):**
- Save to `Personalized-Review-Decks/` folder
- Name format: `[Topic]_[Source]_[Date].csv` (e.g., `Identities_TutorialsDojo_Nov29.csv`)
- DO NOT merge into Master Deck - keep as separate deck for spaced repetition
- Tag with source: "Tutorials-Dojo-Quiz", "Whizlabs-Weak-Spots", etc.

**NEVER:**

- ❌ Add duplicate questions from previous batches
- ❌ Mix up question topics (e.g., adding FD-UD when user asked for Container Security)
- ❌ Write explanations longer than 2 sentences (breaks study flow)
- ❌ Forget to regenerate the .apkg file after CSV changes
- ❌ Commit without updating README card counts and MS Learn references
- ❌ Merge personalized review decks into Master Deck (defeats spaced repetition purpose)

**Repository Location:** `/Users/mike1macbook/Documents/MY STUFF DOCS AND ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck/`

---

## 📊 Current Deck Status (465 Total Cards)

- **Critical Priorities Batch**: 5 essential configuration scenarios
- **RTO/RPO Storage Batch**: 3 disaster recovery fundamentals
- **Storage Replication & DR Batch**: 52 comprehensive storage questions
- **App Service & Container Operations Batch**: 29 questions
- **Enhanced Compute Batch**: 37 questions
- **Deep Storage Mastery Batch**: 36 questions
- **Storage Identity & Security Traps Batch**: 31 questions
- **Storage Endpoints & Encryption Batch**: 20 questions
- **Storage Performance & Lifecycle Batch**: 20 questions
- **Storage Security & Authentication Batch**: 20 questions
- **VM Availability & Fault Tolerance Batch**: 20 questions (FD-UD deep dive)
- **Container Security Batch**: 5 questions (Defender, ACR Tasks, Azure Policy)
- **App Service Deployment Batch**: 5 questions (Auto-Swap, Slot Settings)
- **App Service Security Batch**: 4 questions (VNet Integration, SQL connectivity)
- **Container Scaling Batch**: 4 questions (Traffic Manager, ACI)
- **SSL Certificates Batch**: 3 questions (Wildcard certs, SSL Binding)
- **Golden Rule Enriched Part 1**: 22 scenario-driven questions (App Service, Storage, Redundancy, Blob Tiers)
- **Golden Rule Enriched Part 2**: 35 scenario-driven questions (Redundancy, Disks, Networking, Backup, DR, Performance)
- **VMSS Deep Dive Batch**: 12 scenario-driven questions (Orchestration modes, Update/Fault Domains, Availability Zones, Load Balancing, IaaS operational burden)
- **App Service Deep Dive Batch**: 17 scenario-driven questions (OS constraints, Runtime choices, Deployment methods, Resource contention, VNet integration, Security pipeline, Bicep IaC, Exam traps)
- **Resilience & Disaster Recovery Deep Dive Batch**: 19 scenario-driven questions (VABRF blueprint, RSV regional boundaries, RBAC Backup Contributor, Azure Backup vs ASR distinction, ransomware vs regional recovery, app-consistent recovery points, VSS technology, test failover validation, commit/reprotect sequence, action groups automation, monitoring replication health, Azure Policy resilience architecture)
- **Hybrid Azure Mastery Deep Dive Batch**: 20 scenario-driven questions (RBAC vs Entra DS identity model, Azure Files double-permission layer, SMB port 445 hybrid tunneling, Kerberos authentication for NTFS, Azure Policy governance enforcement, PIM just-in-time privilege, App Service plan scaling architecture, Docker Container runtime ownership, ACI no-scaling limitation, Bicep IaC performance benchmarks, three-tier VNet subnet design, VNet peering vs VPN gateway, internal load balancer vs Application Gateway, WAF tier requirement, Network Watcher IP Flow Verify and Connection Troubleshoot, Azure Monitor KQL, metric/log search/activity log alerts, hybrid Azure Monitor Agent deployment, five-pillar architectural integration, resource tagging + Policy inventory foundation)
- **Storage Identity Resilience Untangled Deep Dive Batch**: 20 scenario-driven questions (Azure Files 3-layer access: network/RBAC/NTFS, Private Endpoints bypassing ISP port blocks, Entra ID vs RBAC vs Azure Policy governance distinctions, Conditional Access MFA >99.9% attack blocking, PIM just-in-time privilege auto-expiration, GRS vs ZRS cost/resilience trade-offs, Recovery Services Vault vs Azure Backup Vault architectures, ASR planned/unplanned/test failover sequencing, Cost Management + Budgets for billing separation beyond tags)
- **VABRF Operational Resilience Deep Dive Batch**: 20 scenario-driven questions (VABRF 5-step framework operational sequence, RSV regional administrative boundaries, RBAC Access step and Reader role limitations, Backup policy contract with data, Azure Backup vs ASR operational differences, Ransomware restore vs regional failover paths, Recovery point timestamp criticality, VM validation before user cutover, Unplanned failover with Commit finality, Reprotect bi-directional redundancy requirement, VSS app-consistent recovery points for databases, Test failover sandbox isolation, Azure Monitor proactive resilience with metric/activity/log search alerts, Action Groups automated remediation, Secondary region VNet pre-provisioning, Azure Policy + Action Groups drift prevention, Resilience architect vs basic admin operational maturity)
- **Last Updated**: November 27, 2025

## 📥 Download

**[⬇️ Download AZ-104-Master-Study-Deck.apkg](https://github.com/mikiemapo/AZ-104-Critical-Priorities-Study-Deck/raw/main/AZ-104-Master-Study-Deck.apkg)**

_Click the link above to download the hierarchical Anki deck file. Double-click to import into Anki._

---

## 🎯 Features

- **Hierarchical subdeck structure** with expandable categories (+/- signs)
- **Visual answer format** with white choice rectangles that turn green on reveal
- **Critical priority focus** on high-impact exam topics
- **Zero blank rectangle issues** - all choices display correctly
- **Randomized answer positions** across A/B/C/D choices
- **Concise explanations** (2 sentences max) for quick review

## 📁 Files Structure

- `AZ-104-Master-Questions.csv` - Master question database
- `create_master_deck.py` - Deck generation script
- `AZ-104-Master-Study-Deck.apkg` - Final hierarchical deck file
- `README.md` - This documentation

## 🔄 **ADDING NEW QUESTION BATCHES**

### ⚠️ CRITICAL FORMAT REQUIREMENTS:

**DO NOT CHANGE THESE - THEY ENSURE THE DECK CONTINUES WORKING**

#### CSV Structure (EXACT ORDER):

```
Question,ChoiceA,ChoiceB,ChoiceC,ChoiceD,Correct,Explanation,Tags,Source,Batch
```

#### Format Rules:

1. **Randomize Answers**: Distribute correct answers across A/B/C/D positions
2. **Short Explanations**: Maximum 2 sentences per explanation
3. **Batch Naming**: Use descriptive batch name for subdeck organization
4. **Choice Format**: Embed choices in question text as HTML rectangles

#### Workflow:

1. Add questions to `AZ-104-Master-Questions.csv`
2. Run: `python3 create_master_deck.py`
3. Commit: `git add . && git commit -m "ADD [Batch Name]: [count] questions"`
4. Push: `git push origin main`

### 🚫 **WORKING FORMAT - DO NOT MODIFY:**

```python
# Template structure in create_master_deck.py
qfmt = """{{Question}}"""  # Shows white rectangles
afmt = """{{QuestionWithAnswer}}<hr>{{Answer}}"""  # Shows green highlighting
```

**Why this works:**

- **Question Field**: Plain question with embedded white rectangles
- **QuestionWithAnswer Field**: Same question with green highlighting for correct choice
- **Separate Front/Back**: Prevents premature green highlighting
- **CSS**: White rectangles turn green only on "Show Answer"

### 📝 **Example New Batch Entry:**

```csv
"Which replication provides zone + region protection?","LRS","ZRS","GZRS","GRS","C","GZRS combines zone redundancy with geo-replication. It provides both local zone protection and cross-region disaster recovery.","Storage,Replication,GZRS","Microsoft Learn","Storage Batch"
```

## 📥 Import Instructions

1. Download `AZ-104-Master-Study-Deck.apkg`
2. Import into Anki
3. Expand/collapse subdecks using + signs for focused study

## 🎉 Perfect for:

- AZ-104 exam preparation
- Storage & disaster recovery mastery
- Critical priority scenarios practice
- Hierarchical study organization

## Study Strategy

1. Focus first on "Golden Rule" batch for fundamental decision frameworks
2. Use spaced repetition for App Service & Containers domain
3. Practice storage redundancy and backup scenarios until automatic
4. Review Critical Priorities batch regularly for high-impact topics

## Import Instructions

1. Download `AZ-104-Master-Study-Deck.apkg`
2. Double-click the file to import into Anki
3. Expand/collapse subdecks using + signs for focused study

---

## 📚 Microsoft Learn References

All questions cross-referenced with official Microsoft Learn documentation:

### Container Security Batch

- [Microsoft Defender for Containers](https://learn.microsoft.com/azure/defender-for-cloud/defender-for-containers-introduction)
- [ACR Tasks](https://learn.microsoft.com/azure/container-registry/container-registry-tasks-overview)
- [Azure Policy for Containers](https://learn.microsoft.com/azure/governance/policy/concepts/policy-for-kubernetes)
- [Container Security Best Practices](https://learn.microsoft.com/azure/container-instances/container-instances-image-security)
- [Secure Container Deployment](https://learn.microsoft.com/azure/container-registry/container-registry-best-practices)

### App Service Deployment Batch

- [App Service Deployment Slots](https://learn.microsoft.com/azure/app-service/deploy-staging-slots)
- [App Service Configuration](https://learn.microsoft.com/azure/app-service/configure-common)
- [App Service Auto-Swap](https://learn.microsoft.com/azure/app-service/deploy-staging-slots#auto-swap)
- [App Service Deployment Best Practices](https://learn.microsoft.com/azure/app-service/deploy-best-practices)

### App Service Security Batch

- [App Service VNet Integration](https://learn.microsoft.com/azure/app-service/overview-vnet-integration)
- [SQL Database Network Security](https://learn.microsoft.com/azure/azure-sql/database/network-access-controls-overview)
- [VNet Integration](https://learn.microsoft.com/azure/app-service/configure-vnet-integration-enable)
- [Secure SQL Connectivity](https://learn.microsoft.com/azure/app-service/app-service-web-tutorial-connect-msi)

### Container Scaling Batch

- [Traffic Manager](https://learn.microsoft.com/azure/traffic-manager/traffic-manager-overview)
- [Azure Load Balancer](https://learn.microsoft.com/azure/load-balancer/load-balancer-overview)
- [ACI Scaling Strategies](https://learn.microsoft.com/azure/container-instances/container-instances-container-groups)
- [Traffic Manager Routing](https://learn.microsoft.com/azure/traffic-manager/traffic-manager-routing-methods)

### SSL Certificates Batch

- [App Service Custom Domains](https://learn.microsoft.com/azure/app-service/app-service-web-tutorial-custom-domain)
- [TLS/SSL Certificates](https://learn.microsoft.com/azure/app-service/configure-ssl-certificate)
- [App Service SSL Binding](https://learn.microsoft.com/azure/app-service/configure-ssl-bindings)

### Golden Rule Batch

- [App Service Runtime Stacks](https://learn.microsoft.com/azure/app-service/overview#built-in-languages-and-frameworks)
- [Storage Account Types](https://learn.microsoft.com/azure/storage/common/storage-account-overview)
- [Storage Performance Tiers](https://learn.microsoft.com/azure/storage/common/storage-account-overview#performance-tiers)
- [AzCopy Overview](https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10)
- [Storage Redundancy Options](https://learn.microsoft.com/azure/storage/common/storage-redundancy)
- [Blob Access Tiers](https://learn.microsoft.com/azure/storage/blobs/access-tiers-overview)
- [Azure Disk Types](https://learn.microsoft.com/azure/virtual-machines/disks-types)
- [App Service Plans](https://learn.microsoft.com/azure/app-service/overview-hosting-plans)
- [AzCopy Authorization](https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-authorize-azure-active-directory)
- [VPN Gateway Types](https://learn.microsoft.com/azure/vpn-gateway/vpn-gateway-about-vpngateways)
- [Azure Load Balancer](https://learn.microsoft.com/azure/load-balancer/load-balancer-overview)
- [VM Backup Consistency](https://learn.microsoft.com/azure/backup/backup-azure-vms-introduction#snapshot-consistency)
- [VM Restore with Encryption](https://learn.microsoft.com/azure/backup/backup-azure-vms-encryption)

### VM Availability & Fault Tolerance Batch

- [Availability Sets](https://learn.microsoft.com/azure/virtual-machines/availability-set-overview)
- [Planned Maintenance](https://learn.microsoft.com/azure/virtual-machines/maintenance-and-updates)

### Storage Batches

- [Azure Storage Documentation](https://learn.microsoft.com/azure/storage/)
- [Storage Replication](https://learn.microsoft.com/azure/storage/common/storage-redundancy)
- [Storage Security](https://learn.microsoft.com/azure/storage/common/security-recommendations)
