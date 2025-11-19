# AZ-104 Critical Priorities Study Deck

## 📊 Current Deck Status (34 Total Cards)

- **Critical Priorities Batch**: 5 essential configuration scenarios
- **RTO/RPO Storage Batch**: 3 disaster recovery fundamentals
- **Storage Replication & DR Batch**: 26 comprehensive storage questions
- **Last Updated**: November 18, 2025

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
