# Deep Dive Naming System — UNIFIED CONVENTION

## Problem Statement
Multiple Deep Dive transcripts were being named inconsistently, making it **impossible to distinguish** between:
- Audio-extracted Deep Dive batches
- Original baseline batches (Golden Rules, VMSS, etc.)
- Topic-specific batches

**Result:** Naming chaos. User couldn't track which Deep Dives were already processed.

---

## SOLUTION: Standardized Naming Pattern

### **Pattern: `AZ104_[TOPIC_AREA]_[DESCRIPTOR]_DeepDive.csv`**

Where:
- **`AZ104_`** = Prefix (all study files start here)
- **`[TOPIC_AREA]`** = Primary theme (Storage, Identity, Resilience, Hybrid, etc.)
- **`[DESCRIPTOR]`** = Specific angle or framework (e.g., "Untangled," "Mastery," "VABRF")
- **`_DeepDive`** = Clear indicator this is a transcript-extracted batch
- **`.csv`** = Standard format

### **Batch Name in CSV** (Anki "Batch" column)
Format: `[TOPIC] [DESCRIPTOR] Deep Dive Batch`

---

## Current Deep Dive Inventory (POST-STANDARDIZATION)

### ✅ Audio-Extracted Deep Dives (20 questions each)

| File Name | Topic | Focus | Batch Name | Status |
|-----------|-------|-------|-----------|--------|
| `AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv` | Storage/Identity/Governance | Untangling 3-layer Azure Files, Entra vs RBAC vs Policy, GRS vs ZRS | Storage Identity Resilience Untangled Deep Dive Batch | ✅ NEW (446 total cards) |
| `AZ104_Hybrid_Azure_Mastery_DeepDive.csv` | Hybrid Integration | 5-pillar hybrid architecture (Identity→Storage→Compute→Network→Monitor) | Hybrid Azure Mastery Deep Dive Batch | ✅ Existing |
| `AZ104_Resilience_DR_DeepDive.csv` | Resilience & DR | VABRF blueprint, Backup vs ASR, test failover | Resilience & Disaster Recovery Deep Dive Batch | ✅ Existing |
| `AZ104_App_Service_Deep_Dive.csv` | App Service | Runtime stacks, OS constraints, multi-app planning | App Service Deep Dive Batch | ✅ Existing |
| `AZ104_VMSS_Deep_Dive.csv` | VMSS | Orchestration modes, stateless vs stateful | VMSS Deep Dive Batch | ✅ Existing |

### 📌 Baseline Batches (NOT Deep Dives—original 380 questions)

| File Name | Topic | Count |
|-----------|-------|-------|
| `AZ104_Golden_Rule_Enriched_Part1_FULL.csv` | Golden Rules (basics) | 57 |
| `AZ104_Golden_Rule_Enriched_Part2_FULL.csv` | Golden Rules (storage/resilience) | 57 |
| `AZ-104-Master-Questions.csv` | **COMBINED MASTER** (all 445 Qs + 1 header) | **446 lines** |

---

## Key Naming Rules (ENFORCE GOING FORWARD)

### Rule 1: Deep Dive Identifier
- **ALL audio-extracted questions** MUST include `_DeepDive` in filename
- **Baseline batches** use topic names WITHOUT `_DeepDive`
- Example:
  - ✅ Good: `AZ104_Hybrid_Azure_Mastery_DeepDive.csv` (transcript-extracted)
  - ❌ Bad: `AZ104_HybridMastery.csv` (ambiguous)

### Rule 2: Descriptor Specificity
- Use descriptors that clarify the **unique angle** of this transcript
- Examples:
  - "Untangled" = Clarifying confusing concepts (Storage, Identity, Resilience layers)
  - "Mastery" = Advanced integration (5-pillar hybrid approach)
  - "VABRF" = Specific framework name from transcript
  - Avoid generic names like "Advanced" or "Part2" in Deep Dive files

### Rule 3: Batch Column Format
- All Deep Dive batch names should follow: `[TOPIC] [DESCRIPTOR] Deep Dive Batch`
- Example: `Storage Identity Resilience Untangled Deep Dive Batch`
- This makes Anki subdeck sorting obvious

### Rule 4: Master CSV Organization
- **SINGLE source of truth:** `AZ-104-Master-Questions.csv` (combines all 445 questions)
- Never edit original Deep Dive CSVs after appending (keep as archive/reference)
- Rebuild `.apkg` deck from master CSV only

---

## Processing Checklist (WHEN NEW DEEP DIVE PROVIDED)

- [ ] **Step 1:** Check existing Deep Dives to avoid duplicates
  - Existing: Untangled, Mastery, VABRF (Resilience/DR), App Service, VMSS
  
- [ ] **Step 2:** Name NEW Deep Dive file using pattern
  - `AZ104_[TOPIC]_[DESCRIPTOR]_DeepDive.csv`
  
- [ ] **Step 3:** Set Batch column to
  - `[TOPIC] [DESCRIPTOR] Deep Dive Batch`
  
- [ ] **Step 4:** Extract 20 scenario-based questions with:
  - Mnemonics & decision frameworks
  - Exam traps & edge cases
  - Operational context
  
- [ ] **Step 5:** Append to master
  - `tail -n +2 [NEW_FILE].csv >> AZ-104-Master-Questions.csv`
  
- [ ] **Step 6:** Rebuild deck
  - `python3 create_master_deck.py`
  
- [ ] **Step 7:** Update README with new batch description
  
- [ ] **Step 8:** Commit to git
  - Message: `ADD: [TOPIC] [DESCRIPTOR] Deep Dive (20 Q) = [TOTAL] total cards`

---

## Current Card Count by Batch

```
Golden Rule Enriched Part 1:        57 cards
Golden Rule Enriched Part 2:        57 cards
VMSS Deep Dive:                     12 cards
App Service Deep Dive:              17 cards
Enhanced Compute:                   20 cards
Container Operations:               29 cards
Container Security:                  5 cards
Container & Network Scaling:        20 cards
SSL & Advanced Networking:          20 cards
Storage Replication:                52 cards
Storage Endpoints:                  20 cards
Storage Performance:                20 cards
Storage Security:                   20 cards
Storage & Identity:                 31 cards
RTO/RPO Essentials:                  3 cards
VM Availability:                    20 cards
Critical Priorities:                 5 cards
─────────────────────────────────────
Resilience & Disaster Recovery:     20 cards (Deep Dive)
Hybrid Azure Mastery:               20 cards (Deep Dive)
Storage Identity Resilience Untangled: 20 cards (Deep Dive)  ← NEW
─────────────────────────────────────
TOTAL:                             445 cards (+ 1 header line = 446 lines)
```

---

## Future Deep Dive Tracking

| Transcript Title | Status | File Name | Batch Name | Questions |
|------------------|--------|-----------|-----------|-----------|
| Storage, Identity & Governance Deep Dive | ✅ PROCESSED | AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv | Storage Identity Resilience Untangled Deep Dive Batch | 20 |
| Resilience & Disaster Recovery Deep Dive | ✅ PROCESSED | AZ104_Resilience_DR_DeepDive.csv | Resilience & Disaster Recovery Deep Dive Batch | 20 |
| Hybrid Azure Mastery Deep Dive | ✅ PROCESSED | AZ104_Hybrid_Azure_Mastery_DeepDive.csv | Hybrid Azure Mastery Deep Dive Batch | 20 |
| [NEW TRANSCRIPTS GO HERE] | PENDING | ? | ? | ? |

---

## Example: How to Check for Duplicates

**User provides new transcript:** "Welcome to Deep Dive on Azure Virtual Machines..."

**Quick check:**
1. `ls AZ104_*_DeepDive.csv` → See all existing Deep Dives
2. Read first 5 questions of each to confirm topic
3. If topic matches an existing Deep Dive → **DON'T RE-PROCESS** (already done)
4. If topic is NEW → Create new file with clear naming

---

## Why This Matters

- ✅ **No accidental re-processing** → Wasted effort prevented
- ✅ **Anki deck clarity** → Each batch name tells you the source/focus
- ✅ **Easy to update README** → Batch descriptions match file names
- ✅ **Git history cleaner** → Commit messages reference clear batch names
- ✅ **Study schedule alignment** → Calendar events can reference exact batch names

---

**DECISION:** Use this naming convention for ALL future Deep Dives.
