# Deep-Dive Text File Extraction Tracker

**Last Updated:** December 9, 2025 (Checker Run)  
**Current Status:** Automated Analysis Complete  
**Completion:** 1 Done / 7 Checking / 5 New = **8% done, 58% pending analysis**

---

## Summary

This tracker maps all text file transcripts in the `/Conversations/AZ-104 CONVERSATIONS/` folder to their corresponding Anki deck CSVs in `/Topic-Based-Decks/`. Only **genuinely new content** (not already in existing CSVs) should be extracted into decks.

**Automated Checker:** `check_new_deep_dive_files.py` ran and categorized all 12 text files:
- ✅ **1 Done:** Compute Decision (19 CPRS questions extracted)
- ⏳ **7 Need Comparison:** Text files match existing CSVs (need verification if duplicate or new)
- 🆕 **5 New:** No existing CSV found (need 20 CPRS questions each)

---

## Existing Deep-Dive CSV Decks (Topic-Based-Decks folder)

| # | CSV File | Questions | Status | Text File Match |
|----|----------|-----------|--------|-----------------|
| 1 | AZ104_VABRF_Operational_Resilience_DeepDive.csv | 20 | ✅ DONE | VABRF_5-Step_Blueprint |
| 2 | AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv | 20 | ⏳ CHECKING | Untangling_Azure_Storage_Identity_and_Governance |
| 3 | AZ104_Hybrid_Azure_Mastery_DeepDive.csv | 20 | ⏳ CHECKING | RBAC vs. Entra DS - Five Pillars |
| 4 | AZ104_Resilience_DR_DeepDive.csv | 19 | ⏳ CHECKING | Azure_Disaster_Recovery_RTO_RPO_Explained |
| 5 | AZ104_App_Service_DeepDive.csv | 17 | ⏳ CHECKING | Azure_App_Service_Golden_Rules_ROADMAP |
| 6 | AZ104_VMSS_DeepDive.csv | 12 | ✅ DONE | (No matching text file) |
| 7 | AZ104_Container_Apps_Ingress_DeepDive.csv | Large | ⏳ CHECKING | Mastering_Azure_Container_Apps_Ingress_Configuration |
| 8 | AZ104_Compute_Decision_DeepDive.csv | 19 | ✅ NEW | Azure_Compute_Decision_Guide_IaaS_vs_PaaS |
| 9 | AZ104_Golden_Rule_Enriched_Part1_FULL.csv | - | ✅ BASELINE | (Baseline batch, not from new text) |
| 10 | AZ104_Golden_Rule_Enriched_Part2_FULL.csv | - | ✅ BASELINE | (Baseline batch, not from new text) |

---

## Text Files Status

### ✅ DONE (Content Extracted)

#### 1. Azure_Compute_Decision_Guide
- **File:** `Azure_Compute_Decision_Guide_IaaS_vs_PaaS_vs_Containers_and_the (Transcribed).txt`
- **Size:** 16.1 KB
- **CSV:** `AZ104_Compute_Decision_DeepDive.csv` (19 CPRS questions)
- **Status:** ✅ COMPLETED Dec 9 - Content fully extracted
- **Content:** IaaS vs PaaS vs Serverless decisions, control/convenience tradeoffs, OS constraints, scaling, cost, tier immutability, exam traps

---

### ⏳ IN PROGRESS (Need Comparison with Existing CSVs)

**Checker found 7 text files that match existing CSVs. Need verification: Are they duplicates or new content?**

#### 1. Azure_App_Service_Golden_Rules_ROADMAP
- **File:** `Azure_App_Service_Golden_Rules_ROADMAP (Transcribed).txt`
- **Size:** 15.2 KB
- **Existing CSV:** `AZ104_App_Service_DeepDive.csv` (17 qs)
- **Status:** ⏳ CHECKING - May have new ROADMAP-specific content
- **Action:** Compare ROADMAP structure vs existing App Service deck

#### 2. Mastering_Azure_Container_Apps_Ingress_Configuration
- **File:** `Mastering_Azure_Container_Apps_Ingress_Configuration (Transcribed).txt`
- **Size:** 15.0 KB
- **Existing CSV:** `AZ104_Container_Apps_Ingress_DeepDive.csv` (large file)
- **Status:** ⏳ CHECKING - May have advanced ingress scenarios
- **Action:** Compare text vs CSV for new ingress modes/configurations

#### 3. RBAC vs. Entra DS - Five Pillars
- **File:** `RBAC vs. Entra DS- The Five Pillars of Hybrid Azure Mastery, Explained with Essential Mnemonics (Transcribed).txt`
- **Size:** 16.6 KB
- **Existing CSV:** `AZ104_Hybrid_Azure_Mastery_DeepDive.csv` (20 qs)
- **Status:** ⏳ CHECKING - May have new RBAC/Entra identity content
- **Action:** Compare to determine if Entra/RBAC content duplicates existing CSV

#### 4. Untangling_Azure_Storage_Identity_and_Governance (File 1)
- **File:** `Untangling_Azure_Storage_Identity_and_Governance (Transcribed).txt`
- **Size:** 14.3 KB
- **Existing CSV:** `AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv` (20 qs)
- **Status:** ⏳ CHECKING - Verify if content matches existing CSV
- **Action:** Compare Storage/Identity/Governance content

#### 5. Untangling_Azure_Storage_Identity_and_Governance (File 2 - Duplicate)
- **File:** `Untangling_Azure_Storage_Identity_and_Governance (Transcribed)-1.txt`
- **Size:** 14.3 KB
- **Existing CSV:** `AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv` (20 qs)
- **Status:** ⏳ CHECKING - Likely duplicate of File 1 (different suffix)
- **Action:** Verify content identity between the two Storage files

#### 6. VABRF_5-Step_Azure_Resilience_Blueprint
- **File:** `VABRF__The_5-Step_Azure_Resilience_Blueprint_for_Ransomware_and (Transcribed).txt`
- **Size:** 16.2 KB
- **Existing CSV:** `AZ104_VABRF_Operational_Resilience_DeepDive.csv` (20 qs)
- **Status:** ⏳ CHECKING - Previously verified as DUPLICATE (same content)
- **Action:** Confirm SKIP (no new content)

#### 6. VABRF_5-Step_Azure_Resilience_Blueprint
- **File:** `VABRF__The_5-Step_Azure_Resilience_Blueprint_for_Ransomware_and (Transcribed).txt`
- **Size:** 16.2 KB
- **Existing CSV:** `AZ104_VABRF_Operational_Resilience_DeepDive.csv` (20 qs)
- **Status:** ⏳ CHECKING - Previously verified as DUPLICATE (same content)
- **Action:** Confirm SKIP (no new content)

---

### 🆕 NEW (No Existing CSV Found - Need New Decks)

**Checker identified 5 new text files with no corresponding CSVs. Need extraction: 20 CPRS questions each.**

#### 1. AZ-104 VPN Gateway Hybrid Networking Explained
- **File:** `AZ-104-Networking-VPN_Gateway_Hybrid_Networking_Explained (Transcribed).txt` OR `AZ-104 VPN Gateway Hybrid Networking Explained (Transcribed).txt`
- **Size:** 30.0 KB (largest file - most comprehensive)
- **Existing CSV:** ❌ NONE FOUND
- **Status:** 🆕 NEW DECK NEEDED
- **Extraction:** Create `AZ104_VPN_Gateway_Hybrid_Networking_DeepDive.csv` with 20 CPRS questions
- **Topics:** VPN Gateway types (Policy-based, Route-based), S2S connectivity, P2P connectivity, hybrid cloud architecture, redundancy, failover, bandwidth, exam traps, mnemonic

#### 2. Azure_Disaster_Recovery_RTO_RPO_Explained
- **File:** `Azure_Disaster_Recovery_RTO_RPO_Explained (Transcribed).txt`
- **Size:** 12.8 KB
- **Existing CSV:** ❌ NONE FOUND (separate from AZ104_Resilience_DR_DeepDive)
- **Status:** 🆕 NEW DECK NEEDED
- **Extraction:** Create `AZ104_Disaster_Recovery_RTO_RPO_DeepDive.csv` with 20 CPRS questions
- **Topics:** RTO vs RPO definitions, tradeoffs, backup windows, replication lag, ASR, failover, recovery time SLAs, cost-recovery balance, exam traps

#### 3. Azure_Monitor_Operations_Overhaul (DINE Policy)
- **File:** `Azure_Monitor_Operations_Overhaul__Using_Triage,_DINE_Policy,_a (Transcribed).txt`
- **Size:** 9.5 KB
- **Existing CSV:** ❌ NONE FOUND
- **Status:** 🆕 NEW DECK NEEDED
- **Extraction:** Create `AZ104_Azure_Monitor_Operations_DeepDive.csv` with 20 CPRS questions
- **Topics:** Monitor setup, DINE Policy (Deny Inheritance Nesting Exemption), alerting strategy, diagnostics, KQL, log analytics, action groups, exam traps

#### 4. RPO_RTO_and_Azure_Storage_Tiers_Explained
- **File:** `RPO_RTO_and_Azure_Storage_Tiers_Explained (1) (Transcribed).txt`
- **Size:** 12.4 KB
- **Existing CSV:** ❌ NONE FOUND
- **Status:** 🆕 NEW DECK NEEDED
- **Extraction:** Create `AZ104_Storage_Tiers_RPO_RTO_DeepDive.csv` with 20 CPRS questions
- **Topics:** Hot/Cool/Archive tiers, RPO/RTO in storage context, access patterns, cost optimization, rehydration, blob tier lifecycle, failover, exam traps, decision framework

#### 5. AZ-104 VPN Gateway (Alternative Filename - likely duplicate of #1)
- **File:** `AZ-104 VPN Gateway Hybrid Networking Explained (Transcribed).txt`
- **Size:** 30.0 KB
- **Status:** ⚠️ LIKELY DUPLICATE of file #1 (check before extraction)
- **Action:** Verify if both files have identical content; if so, extract once

---

## Creation Progress

| Task | Created | Questions | Notes |
|------|---------|-----------|-------|
| Compute Decision Deep Dive | ✅ Dec 9 | 19 CPRS | IaaS vs PaaS vs Serverless, control/convenience tradeoffs, OS constraints, scaling, cost, tier immutability |
| Storage/Identity Comparison | ⏳ PENDING | - | Need to compare text vs existing CSV |
| RBAC/Entra Comparison | ⏳ PENDING | - | Need to compare text vs existing CSV |
| DR/RTO/RPO Comparison | ⏳ PENDING | - | May have RTO/RPO focus |
| App Service ROADMAP Comparison | ⏳ PENDING | - | Need to compare text vs existing CSV |
| Container Apps Ingress Comparison | ⏳ PENDING | - | Need to check for new scenarios |
| Storage Tiers NEW Deck | ⏳ PENDING | ~20 CPRS | Brand new topic (no existing CSV) |
| Monitor Operations NEW Deck | ⏳ PENDING | ~20 CPRS | Brand new topic (no existing CSV) |
| VPN Gateway/Hybrid Networking NEW Deck | ⏳ PENDING | ~20 CPRS | Brand new topic (no existing CSV) |

---

## Cross-Reference: Text File → CSV Status

**Legend:** ✅ = Done | ⏳ = In Progress | 🆕 = New Deck Needed | ⚠️ = Verify Duplicate

| Text File | CSV Status | Match Type | Action |
|-----------|-----------|-----------|--------|
| Compute Decision | ✅ AZ104_Compute_Decision_DeepDive (19 qs) | NEW | ✅ EXTRACTED Dec 9 |
| App Service ROADMAP | ⏳ AZ104_App_Service_DeepDive (17 qs) | Likely Match | COMPARE |
| Container Apps Ingress | ⏳ AZ104_Container_Apps_Ingress_DeepDive (large) | Likely Match | COMPARE |
| RBAC vs Entra Five Pillars | ⏳ AZ104_Hybrid_Azure_Mastery_DeepDive (20 qs) | Likely Match | COMPARE |
| Storage/Identity (File 1) | ⏳ AZ104_Storage_Identity_Resilience_Untangled (20 qs) | Likely Match | COMPARE |
| Storage/Identity (File 2) | ⏳ AZ104_Storage_Identity_Resilience_Untangled (20 qs) | Likely Duplicate | VERIFY IDENTITY |
| VABRF Blueprint | ⏳ AZ104_VABRF_Operational_Resilience (20 qs) | KNOWN DUPLICATE | SKIP |
| VPN Gateway Hybrid (File 1) | 🆕 NONE | NEW | CREATE AZ104_VPN_Gateway_Hybrid_DeepDive |
| VPN Gateway Hybrid (File 2) | ⚠️ Check vs File 1 | Possible Duplicate | COMPARE FILES |
| Disaster Recovery RTO/RPO | 🆕 NONE | NEW | CREATE AZ104_Disaster_Recovery_RTO_RPO_DeepDive |
| Monitor Operations DINE | 🆕 NONE | NEW | CREATE AZ104_Azure_Monitor_Operations_DeepDive |
| Storage Tiers RPO/RTO | 🆕 NONE | NEW | CREATE AZ104_Storage_Tiers_RPO_RTO_DeepDive |

---

## Deck Quality Standards

All deep-dive decks follow **CPRS (Critical Priorities Research-Scenario)** format:
1. **Foundation:** Define core concept
2. **Definition:** Differentiate related terms
3. **Differentiation:** Compare alternatives
4. **Scenario + Misdirect:** Real-world tradeoff + exam trap
5. **Anti-Confusion:** Counter exam tricks
6. **Compression:** Decision tree / mnemonic

**CSV Format:** `Question | ChoiceA | ChoiceB | ChoiceC | ChoiceD | Correct | Explanation | Tags | Source | Batch`

**Anki Styling:** Green (#4CAF50) matching AZ104 Master Deck

---

## Next Steps

1. ⏳ **Compare existing CSVs with text files** (Storage, RBAC, DR, App Service, Container Apps)
2. ⏳ **Create 3 new decks** if no CSV exists (Storage Tiers, Monitor Operations, VPN Gateway)
3. ⏳ **Generate .apkg Anki packages** for all new/updated CSVs
4. ✅ **Run periodic check script** to monitor for new text files in cloud folder
5. ✅ **Commit to git** on `feature/cli-az104-focus` branch

---

## Periodic Monitoring

See `check_new_deep_dive_files.py` for automated text file discovery and CSV status checking.

**Run:** `python3 tools/check_new_deep_dive_files.py`

**Output:** Summary of new text files in cloud folder vs existing CSVs in Topic-Based-Decks

---
