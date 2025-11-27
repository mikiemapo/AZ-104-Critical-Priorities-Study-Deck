# AZ-104 Critical Priorities Study Deck

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

**NEVER:**

- ❌ Add duplicate questions from previous batches
- ❌ Mix up question topics (e.g., adding FD-UD when user asked for Container Security)
- ❌ Write explanations longer than 2 sentences (breaks study flow)
- ❌ Forget to regenerate the .apkg file after CSV changes
- ❌ Commit without updating README card counts and MS Learn references

**Repository Location:** `/Users/mike1macbook/Documents/MY STUFF DOCS AND ALL/EBOOK/AZ-104-Study-Deck/`

---

## 📊 Current Deck Status (366 Total Cards)

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
- **Golden Rule Batch**: 28 questions (Azure best practices and decision frameworks)
- **Golden Rule Enriched Part 1**: 8 scenario questions (Tutorial Dojo grounded)
- **Golden Rule Enriched Part 2**: 8 scenario questions (Tutorial Dojo grounded)
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
