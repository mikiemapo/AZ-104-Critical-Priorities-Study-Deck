# Transcript Auto-Processing System

## Overview

**Problem Solved:** Manual monitoring of cloud transcripts folder, deciding which ones are new, and manually extracting Deep Dive questions is tedious and error-prone.

**Solution:** Automated script that:

1. ✅ Monitors `/Users/mike1macbook/Library/Mobile Documents/.../Conversations not hub/Text files` daily at **12:00 PM**
2. ✅ Detects NEW transcripts
3. ✅ Tracks processed transcripts in `.processed_transcripts.log`
4. ✅ Alerts when new Deep Dives need creation
5. ✅ Logs to `/tmp/transcript_processor.log`

---

## System Components

### 1. **Monitoring Script**

**File:** `auto_process_transcripts.sh`

**What it does:**

- Scans cloud folder for `.txt` transcript files
- Compares against `.processed_transcripts.log` to find NEW transcripts
- Identifies transcript topic (App Service, Hybrid, Storage/Identity, VABRF, etc.)
- Checks if corresponding Deep Dive CSV already exists
- Alerts if new Deep Dive needs creation

**How to run manually:**

```bash
cd "/Users/mike1macbook/Documents/MY STUFF DOCS AND ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck"
./auto_process_transcripts.sh
```

**Log location:** `/tmp/transcript_processor.log`

### 2. **Cron Job Automation**

**Schedule:** Daily at **12:00 PM** (noon)

**Verify cron is active:**

```bash
crontab -l | grep auto_process
```

**Manually trigger a check:**

```bash
/Users/mike1macbook/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck/auto_process_transcripts.sh
```

### 3. **Processed Transcripts Log**

**File:** `.processed_transcripts.log` (in study deck directory)

**Contains:** List of transcript filenames already processed (one per line)

**Example:**

```
Azure_App_Service_Golden_Rules_ROADMAP (Transcribed).txt
RBAC vs. Entra DS- The Five Pillars of Hybrid Azure Mastery, Explained with Essential Mnemonics (Transcribed).txt
Untangling_Azure_Storage_Identity_and_Governance (Transcribed).txt
```

---

## Current Transcript Status

### ✅ Already Processed

| Transcript                               | Deep Dive CSV                                              | Questions |
| ---------------------------------------- | ---------------------------------------------------------- | --------- |
| Azure App Service Golden Rules ROADMAP   | `AZ104_App_Service_DeepDive.csv`                           | 17        |
| RBAC vs. Entra DS - Hybrid Azure Mastery | `AZ104_Hybrid_Azure_Mastery_DeepDive.csv`                  | 20        |
| Untangling Storage/Identity/Governance   | `AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv` | 20        |
| [Others in AZ-104 CONVERSATIONS folder]  | Various                                                    | 300+      |

### ⚠️ New / Needs Processing

| Transcript                                | Status   | Action                                                                       |
| ----------------------------------------- | -------- | ---------------------------------------------------------------------------- |
| VABRF - 5-Step Azure Resilience Blueprint | Detected | Manual extraction needed → `AZ104_VABRF_Operational_Resilience_DeepDive.csv` |

---

## Workflow When NEW Transcript Detected

When the script finds a new transcript (not in `.processed_transcripts.log`):

### Automated Steps (Script Does):

1. ✅ Scan transcript for topic keywords
2. ✅ Check if matching Deep Dive CSV exists
3. ✅ Alert user if new Deep Dive needed
4. ✅ Mark transcript as processed (add to log)

### Manual Steps (You Do):

1. 📝 **Extract 20 scenario-based questions** from transcript

   - Include mnemonics, decision frameworks, operational context
   - Format: `Question,ChoiceA,ChoiceB,ChoiceC,ChoiceD,Correct,Explanation,Tags,Source,Batch`
   - Explanation: 2 sentences MAX
   - Batch: `[TOPIC] Deep Dive Batch`

2. 📄 **Create CSV file:** `AZ104_[TOPIC]_DeepDive.csv`

3. 🔗 **Append to master:**

   ```bash
   tail -n +2 AZ104_[TOPIC]_DeepDive.csv >> AZ-104-Master-Questions.csv
   ```

4. 🎴 **Rebuild deck:**

   ```bash
   python3 create_master_deck.py
   ```

5. 📅 **Update calendar** (if applicable):

   - Add new batch to `AZ104_Study_Schedule_DETAILED.ics`

6. 📤 **Commit to git:**
   ```bash
   git add -A
   git commit -m "ADD: [TOPIC] Deep Dive (20 Q) = [TOTAL] total cards"
   git push
   ```

---

## Automation Limitations

**What the script does NOT do (by design):**

- ❌ Extract questions from transcripts (requires AI/human judgment)
- ❌ Create CSV files automatically (question quality matters)
- ❌ Update calendar or README (manual review recommended)
- ❌ Commit to git (you control when/what gets committed)

**Why?** These require human judgment, context, and validation to ensure:

- ✅ Questions match user's learning goals
- ✅ Explanations are accurate and concise
- ✅ Mnemonics align with exam patterns
- ✅ Batch naming stays consistent

---

## Monitoring the Automation

### Check today's transcript scan:

```bash
tail -20 /tmp/transcript_processor.log
```

### See processed transcripts:

```bash
cat /Users/mike1macbook/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck/.processed_transcripts.log
```

### Re-scan manually (force check):

```bash
/Users/mike1macbook/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck/auto_process_transcripts.sh
```

### View active cron jobs:

```bash
crontab -l
```

---

## Next Steps

1. **Verify cron is running:**

   - At 12:00 PM today, check `/tmp/transcript_processor.log` for new scan
   - If cron isn't triggering, verify system time is correct

2. **For VABRF transcript:**

   - Review transcript content (already available in cloud folder)
   - Extract 20 questions following format
   - Create `AZ104_VABRF_Operational_Resilience_DeepDive.csv`
   - Follow workflow above to integrate

3. **Monitor for future transcripts:**
   - Script runs automatically daily at noon
   - Check log weekly to see if new transcripts appear
   - When detected, follow manual workflow above

---

## Troubleshooting

**Cron job not running?**

```bash
# Check if cron is enabled
sudo launchctl list | grep cron

# Restart cron (macOS)
sudo launchctl stop com.vixie.cron
sudo launchctl start com.vixie.cron

# Or use launchd instead (modern macOS):
# Create ~/Library/LaunchAgents/com.az104.transcript-processor.plist
```

**Script not finding transcripts?**

```bash
# Verify cloud folder exists and has files
ls -la "/Users/mike1macbook/Library/Mobile Documents/3L68KQB4HG~com~readdle~CommonDocuments/Documents/azure-ebook-guides/Conversations not hub/Text files"

# Check script path is correct
which auto_process_transcripts.sh
```

**Log file permissions?**

```bash
# Ensure /tmp is writable
touch /tmp/test_write.txt
rm /tmp/test_write.txt
```

---

## File Structure

```
AZ-104-Critical-Priorities-Study-Deck/
├── auto_process_transcripts.sh          ← Monitoring script
├── .processed_transcripts.log           ← Processed transcript tracking
├── AZ104_*_DeepDive.csv                 ← Individual Deep Dive CSVs
├── AZ-104-Master-Questions.csv          ← Master deck database
├── AZ-104-Master-Study-Deck.apkg        ← Final Anki deck
├── create_master_deck.py                ← Deck builder
└── README.md                            ← Main documentation
```

---

## Summary

**You set this up once. It runs automatically at noon every day. You get alerts when new transcripts arrive. You decide when/how to extract and integrate them.**

Minimal overhead. Maximum flexibility.
