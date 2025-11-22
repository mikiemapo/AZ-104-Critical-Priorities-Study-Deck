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

## 📊 Current Deck Status (294 Total Cards)

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
- **Last Updated**: November 22, 2025

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

## About This Deck

**Format Alignment:** This deck follows Connor Sayers' AZ-104 Study Deck format exactly, ensuring seamless integration with existing study workflows. Each card uses:

- **Custom Note Type:** AZ-104 Multiple Choice - Connor Format
- **Professional Styling:** Matching Connor's visual design and color scheme
- **Consistent Structure:** Question + 4 choices + correct answer + detailed explanation + source reference
- **Quality Standards:** Microsoft Learn alignment and exam-focused content

This deck was created using analysis of quiz performance data and enhanced study materials from comprehensive Azure guides. It focuses on:

- **Critical Priority:** App Service & Containers (addressing 20% failure rate)
- **High Priority:** Enhanced compute topics including Fault Domains, Container Apps, Network Watcher
- **Medium Priority:** Core AZ-104 concepts with exam-focused scenarios
- **Strategic Coverage:** Topics identified as common exam pitfalls

## Deck Features

- **Connor Sayers Format:** Exact alignment with established AZ-104 Anki best practices
- **Professional Multiple Choice:** 4-option questions with clear correct answer identification
- **Detailed Explanations:** Step-by-step reasoning with key concepts highlighted
- **Source References:** Microsoft Learn citations for credibility and further study
- **Priority-Based Organization:** Critical weak areas receive primary focus
- **Exam-Focused:** Based on actual quiz failure patterns and Microsoft Learn content
- **Clean Formatting:** Professional styling that works perfectly in Anki
- **Seamless Import:** No formatting issues or compatibility problems

## How to Use

### Quick Start (Recommended)

1. **[Click here to download the .apkg file](https://github.com/mikiemapo/AZ-104-Critical-Priorities-Study-Deck/raw/main/AZ-104-Critical-Priorities-Study-Deck.apkg)**
2. **Double-click** the downloaded file to import into Anki
3. **Start studying** immediately with properly formatted multiple choice questions

### Alternative: CSV Import

1. Download the `AZ-104-Connor-Format.csv` file
2. Open Anki → File → Import
3. Map fields: Question, ChoiceA, ChoiceB, ChoiceC, ChoiceD, Correct, Explanation, Tags, Source
4. Import and start studying

**Note:** The new Connor format includes separate fields for each choice and detailed explanations, providing better study experience than the previous format.

### Study Strategy

1. Focus first on "Critical Priority" tagged cards
2. Use spaced repetition for App Service & Containers domain
3. Practice sequence-based cards (D-G-W-C, C→A→D→B→E) until automatic

## Priority Areas Covered

### Critical Priority (App Service & Containers - 20% Failure Rate)

- Auto-swap deployment configuration
- VNet + SQL Database security sequence
- Container security pipeline implementation
- ACI scaling limitations vs AKS
- Container Apps ingress configuration

### High Priority (Enhanced Compute Topics)

- Fault Domains vs Update Domains foundational knowledge
- VMSS Orchestration Modes (Uniform vs Flexible)
- Encrypted VM migration (D-G-W-C sequence)
- Network Watcher Agent deployment
- App Service runtime and OS constraints

### Medium Priority (Core AZ-104)

- VM sizing strategies and performance optimization
- Azure Backup vs Site Recovery differences
- Scaling concepts and autoscale best practices
- Deployment slots and slot-specific settings
- Monitoring stack integration

## Import Instructions

### For .apkg file (Recommended)

1. Download the `AZ-104-Critical-Priorities-Study-Deck.apkg` file
2. Double-click the file to automatically import into Anki
3. Start studying immediately

### For CSV file (Advanced Users)

1. Download the `AZ-104-Connor-Format.csv` file
2. Open Anki application
3. File → Import
4. Select the CSV file
5. Configure field mapping: Question, ChoiceA, ChoiceB, ChoiceC, ChoiceD, Correct, Explanation, Tags, Source
6. Import and start studying

## Format Compatibility

This deck is fully compatible with Connor Sayers' AZ-104 Study Deck format. You can:

- ✅ Import both decks without conflicts
- ✅ Use the same study workflow and shortcuts
- ✅ Benefit from consistent styling and navigation
- ✅ Mix and match cards for comprehensive coverage

## Feedback & Contributions

This deck is designed to complement Connor Sayers' AZ-104 Study Deck by focusing specifically on identified weak areas and common exam pitfalls while maintaining format consistency. The combination of both decks provides comprehensive AZ-104 coverage with unified styling and user experience.

**Acknowledgment:** This deck follows the format and design principles established by Connor Sayers' excellent AZ-104 Study Deck. Special thanks to Connor for creating the foundational template that makes AZ-104 Anki studying so effective.

Feedback on question accuracy and additional priority topics is welcomed.

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

### VM Availability & Fault Tolerance Batch

- [Availability Sets](https://learn.microsoft.com/azure/virtual-machines/availability-set-overview)
- [Planned Maintenance](https://learn.microsoft.com/azure/virtual-machines/maintenance-and-updates)

### Storage Batches

- [Azure Storage Documentation](https://learn.microsoft.com/azure/storage/)
- [Storage Replication](https://learn.microsoft.com/azure/storage/common/storage-redundancy)
- [Storage Security](https://learn.microsoft.com/azure/storage/common/security-recommendations)
