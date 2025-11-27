# AZ-104 Study Setup Guide - macOS

## Complete Environment Configuration

**Created:** November 26, 2025

---

## 🚀 Prerequisites Check

```bash
# Verify you have these installed on macOS
which python3
which brew
which git

# Expected output: /usr/bin/python3, /usr/local/bin/brew, /usr/bin/git
# If any missing, run: https://brew.sh for Homebrew
```

---

## 1️⃣ Install & Configure Anki

### Option A: Homebrew (Recommended)

```bash
# Install Anki
brew install anki

# Start Anki for first time
anki

# Once Anki opens, close it (we'll import deck next)
```

### Option B: Direct Download

```bash
# Download from https://apps.ankiweb.net
# Drag AnkiMac.app to Applications folder
# Launch from Launchpad
```

### Import AZ-104 Deck

```bash
# Path to deck
cd ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck

# Open Anki app
open -a Anki

# In Anki: File > Import > Select AZ-104-Master-Study-Deck.apkg
# Click "Import"
# Verify: Should show "380 cards" in Collection

# Set up Anki preferences:
# - Preferences > Syncing > Sign in (optional)
# - Preferences > Display > Night mode (for 6am-6pm study)
# - Preferences > Backup > Set to daily
```

### Daily Anki Workflow

```bash
# Start session at 6 AM
open -a Anki

# Recommended settings per session:
# - New Cards: 50 per day
# - Reviews: Unlimited
# - Study Duration: 1-2 hours per session

# Export weak cards for later review:
# Tools > Export > Select deck > Format: Notes in Plain Text
# Save to ~/Desktop for reference
```

---

## 2️⃣ Tutorial Dojo Setup

### Browser Bookmarks (Safari/Chrome)

```
1. Go to https://tutorialdojo.com
2. Login with your credentials
3. Bookmark in browser toolbar as: "TD - AZ-104"
4. Create local folder: ~/Documents/TD_Progress
5. Screenshot weekly scores for tracking
```

### Daily Workflow

```bash
# Open in browser
open https://tutorialdojo.com

# Daily practice routine:
# - 9:00 AM: Start Tutorial Dojo session
# - Take 20-30 questions
# - Record score in ~/Documents/TD_Progress/scores.txt
# - Review incorrect answers (always read explanation)
```

### Progress Tracking File

```bash
# Create scores tracker
cat > ~/Documents/TD_Progress/scores.txt << 'EOF'
# Tutorial Dojo - AZ-104 Progress

## Week 1
- Mon Nov 27: Foundation Set - 18/30 (60%)
- Thu Nov 30: Foundation Set - 24/30 (80%)
- Fri Dec 1: Foundation Set - 26/30 (87%)

## Week 2
- Mon Dec 4: [Score] [Date]

EOF

# Update weekly
nano ~/Documents/TD_Progress/scores.txt
```

---

## 3️⃣ Whizlabs Setup

### Account & Lab Access

```
1. Login to https://www.whizlabs.com
2. Enroll in "AZ-104 Microsoft Azure Administrator"
3. Bookmark as: "WL - AZ-104"
4. Create lab tracking folder: ~/Documents/WL_Labs
```

### Lab Hands-On Environment

```bash
# When doing Whizlabs labs:
# 1. Open Azure Portal: https://portal.azure.com
# 2. Verify subscription is set (usually "Azure Pass" or trial)
# 3. Open Whizlabs lab instructions in second tab
# 4. Follow along; pause Anki during labs

# Schedule labs across 8 weeks:
# Week 2: 1 lab
# Week 3: 1 lab
# Week 4: 1 lab
# Week 5: 1 lab
# Week 6: 1 lab
# Week 7: 1 lab
# Total: 6 hands-on labs
```

### Practice Exam Tracking

```bash
# Create tracking file
cat > ~/Documents/WL_Labs/exam_scores.txt << 'EOF'
# Whizlabs Practice Exams - AZ-104

## Practice Exam 1 (Week 4)
Date: Dec 11, 2025
Score: 105/150 (70%)
Weak: Storage replication, App Service tiers

## Practice Exam 2 (Week 6)
Date: Dec 25, 2025
Score: [TBD]

## Practice Exam 3 (Week 8)
Date: Jan 8, 2026
Score: [Target: 255+/300 (85%)]

EOF
```

---

## 4️⃣ Media Hub Local Access

### Quick Reference Setup

```bash
# Navigate to media hub
cd ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/docs

# Create Safari bookmark
# File > Bookmark This Page > [Save as "AZ-104 Media Hub"]
# Or copy path to file:/// URL

# Direct path:
file:///Users/mike1macbook/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/docs/index.html

# Faster: Create alias in home folder
ln -s ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/docs ~/Documents/media_hub

# Then access: open ~/Documents/media_hub/index.html
```

### Using Media Hub During Study

```bash
# Keep in separate window while studying Anki
# Split screen: Anki left, Media Hub right
# Command+Space to switch between windows quickly

# Chrome split view:
# 1. Open Anki window (left)
# 2. Open Media Hub in browser (right)
# 3. Mission Control (F3) to arrange

# or use Mac Rectangle app:
brew install --cask rectangle
# Then: Option+Right/Left to snap windows
```

---

## 5️⃣ Deep Dive Audio Setup

### File Organization

```bash
# Create folder for audio files
mkdir -p ~/Documents/AZ-104-DeepDives

# Organize by topic
# ~/Documents/AZ-104-DeepDives/VMSS_DeepDive_Transcript.txt
# ~/Documents/AZ-104-DeepDives/AppService_DeepDive_Transcript.txt
# ~/Documents/AZ-104-DeepDives/[Future]_DeepDive_Transcript.txt

# Quick access in Finder
# Drag folder to Favorites sidebar
```

### Audio Playback

```bash
# If you have audio files (not just transcripts)
# Use built-in QuickTime Player or VLC

brew install --cask vlc
# Then: File > Open > Select audio file

# For transcripts, use default Text Editor
open ~/Documents/AZ-104-DeepDives/VMSS_DeepDive_Transcript.txt
```

### Referencing During Study

```bash
# When reviewing Anki card on VMSS:
# 1. Command+Tab to Deep Dive transcript
# 2. Command+F to search "Fault Domain"
# 3. Read context from transcript
# 4. Command+Tab back to Anki
# 5. Mark card correct/incorrect

# Batch processing:
# Monday: Read VMSS transcript while reviewing Anki cards
# Take notes on difficult concepts
```

---

## 6️⃣ Study Notes System

### Choose Your Tool

#### Option 1: Apple Notes (Built-in, Simplest)

```bash
# Open Notes app
open -a Notes

# Create folder: "AZ-104 Study"
# New note per week: "Week 1 - Golden Rules"
# Benefits: Syncs via iCloud, clean interface
```

#### Option 2: Bear (Markdown, Recommended)

```bash
# Install Bear
brew install --cask bear

# Create notebook: "AZ-104"
# New note per week
# Benefits: Markdown support, local storage, tagging
```

#### Option 3: Obsidian (Advanced, Most Powerful)

```bash
# Install Obsidian
brew install --cask obsidian

# Create vault: ~/Documents/AZ-104-Vault
# Use templates for notes
# Benefits: Backlinks, graph view, full Markdown support

# Template for weekly note:
# ---
# Title: Week 1 - Golden Rules
# Date: Nov 27, 2025
# Topics: [Storage], [Compute], [Networking]
# Weak Areas: [List]
# Key Rules: [Decision trees]
# ---
```

### Daily Note Template

```markdown
## Week 1, Monday - Nov 27, 2025

**Anki Session #1 (6-7 AM):** 50 cards, 85% accuracy

- Golden Rule Part 1 (App Service, Storage tiers)
- Tricky: LRS vs. GRS vs. RA-GRS difference
- **Key takeaway:** GRS = different regions; RA-GRS = read access to secondary

**Anki Session #2 (7-8 AM):** 50 cards, 88% accuracy

- Golden Rule Part 1 continued (Redundancy strategies)

**Synthesis (11 AM-12 PM):**

- Created visual: Storage redundancy decision tree
- Weak area: When to use ZRS vs. GZRS (need more practice)
- Rule to remember: ZRS for <500m zone coverage; GZRS for multi-region read

**Tomorrow's focus:** Understand VMSS fault domains
```

---

## 7️⃣ Daily Scheduling on Calendar

### macOS Calendar Setup

```bash
# Open Calendar app
open -a Calendar

# Create new calendar: "AZ-104 Study"
# Color: Blue (to distinguish)

# Add recurring events:
# Every Mon-Tue-Thu-Fri: "Study Session 6am-12pm"
# Every Wed: "OFF DAY"
# Every Sun: "Whizlabs Exam"

# Set reminders:
# 5:50 AM: "Study starts in 10 min - coffee ready?"
# 12:00 PM: "Session complete - great work!"
```

### Notion/Todoist Alternative

```bash
# Or use Todoist for granular task tracking
brew install --cask todoist

# Create recurring tasks:
# - "Week X Monday: Anki [topic], TD [count] Q, review notes"
# - "Week X Thursday: TD set 2, Whizlab lab, synthesis"
# - "Week X Sunday: Whizlabs exam, gap analysis"
```

---

## 8️⃣ Backup Strategy

### Automated Backups

```bash
# Anki auto-exports daily backups
# Check: Anki > Preferences > Backup location
# Default: ~/Library/Application Support/Anki2/backups/

# macOS Time Machine (easy backup all documents)
# System Preferences > Time Machine > Add backup disk

# Manual backup to cloud
brew install --cask dropbox
# Or: Google Drive, OneDrive, iCloud Drive

# Create sync folder
ln -s ~/Dropbox ~/Study_Backup
cp -r ~/Documents/AZ-104-DeepDives ~/Study_Backup/
```

### Git Backup (For Study Notes)

```bash
# If using Obsidian vault with git
cd ~/Documents/AZ-104-Vault
git init
git add .
git commit -m "Initial study vault"
git remote add origin https://github.com/[your-username]/az104-notes.git
git push -u origin main

# Then sync daily
cd ~/Documents/AZ-104-Vault
git add .
git commit -m "Daily notes - Week X"
git push origin main
```

---

## 9️⃣ Time Tracking (Optional but Useful)

### Track Study Hours

```bash
# Install Timing app (free tier)
brew install --cask timing

# Or use Terminal stopwatch
# Terminal command for quick timer:
python3 << 'EOF'
import time
import os

def timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(f'Time: {timeformat}', end='\r')
        time.sleep(1)
        seconds -= 1
    os.system('say "Study session complete"')
    print('\nDone!')

# Example: timer(60) for 1 hour session
timer(60)
EOF

# Or simpler: Use Mac's built-in Timer
# Siri: "Set a timer for 1 hour"
```

### Weekly Hour Target

```bash
# Create tracking file
cat > ~/Documents/Study_Hours.txt << 'EOF'
# AZ-104 Study Hours Tracker

Week 1: 0/25 hours
Week 2: 0/25 hours
Week 3: 0/25 hours
Week 4: 0/25 hours
Week 5: 0/25 hours
Week 6: 0/25 hours
Week 7: 0/25 hours
Week 8: 0/25 hours

Target Total: 200 hours

EOF

# Update weekly
echo "Week 1: 26/25 hours ✅" >> ~/Documents/Study_Hours.txt
```

---

## 🔟 Quick Shortcuts (Shell Aliases)

### Add to ~/.zshrc

```bash
# Edit shell config
nano ~/.zshrc

# Add these lines:
alias az104="cd ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck"
alias anki-study="open -a Anki"
alias td-study="open https://tutorialdojo.com"
alias wl-study="open https://www.whizlabs.com"
alias media-hub="open ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/docs/index.html"
alias note-week="open -a Bear ~/Documents/AZ-104-Notes"

# Reload shell
source ~/.zshrc

# Now use: anki-study, td-study, media-hub from terminal
```

---

## 🎯 Pre-Study Checklist

**Monday 6 AM (Before Week 1 Starts):**

```bash
# 1. Verify all tools installed
brew list | grep -i anki   # Should show: anki
which python3              # Should show: /usr/bin/python3
open -a Anki               # Should open Anki app

# 2. Verify deck imported
# Open Anki > Click on "AZ-104" > Should show "380 cards"

# 3. Verify tutorial dojo access
open https://tutorialdojo.com  # Should log in successfully

# 4. Verify Whizlabs access
open https://www.whizlabs.com  # Should load lab instructions

# 5. Verify media hub
open ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/docs/index.html
# Should see: HTML with blue "NEW" indicators

# 6. Create study notes
open -a Bear
# Should have "AZ-104 Study" notebook ready

# 7. Set calendar reminders
open -a Calendar
# Should have "6am Study Session" blocked for Mon-Tue-Thu-Fri

# 8. Check backup
ls ~/Dropbox/ | grep -i study  # Should see Study_Backup folder

# All checks complete? ✅ Ready to start Week 1!
```

---

## 🆘 Troubleshooting

### Anki Won't Open

```bash
# Reinstall
brew uninstall anki
brew install anki
open -a Anki
```

### Deck Won't Import

```bash
# Check file exists
ls ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck/AZ-104-Master-Study-Deck.apkg

# Try dragging directly onto Anki window
# Or: Anki > File > Import > Browse to file
```

### Can't Access Tutorial Dojo

```bash
# Clear browser cache
# Chrome: Settings > Clear browsing data > All time
# Safari: Develop > Empty Web Storage

# Try incognito window
# Or different browser (Chrome vs. Safari)
```

### Can't Remember Study Folder Paths

```bash
# Create quick finder shortcut
open ~/Documents/MY\ STUFF\ DOCS\ AND\ ALL/EBOOK/
# Drag "AZ-104-Critical-Priorities-Study-Deck" to Finder sidebar
# Now click from any Finder window
```

---

## 📊 Setup Validation

**If all of these work, you're ready:**

1. ✅ Anki opens with 380 cards in AZ-104 collection
2. ✅ Tutorial Dojo loads and you can answer practice questions
3. ✅ Whizlabs shows available labs
4. ✅ Media Hub HTML displays with visual indicators
5. ✅ Notes app is ready (Bear/Apple Notes/Obsidian)
6. ✅ Calendar has study sessions blocked
7. ✅ Azure Portal loads (for Whizlabs labs)
8. ✅ Backup system is configured

**Ready to start Week 1! Let's go. 💪**

---

**Created:** November 26, 2025  
**Next Step:** Read STUDY_CALENDAR_8WEEK.md for Week 1 schedule  
**Questions?** Refer to DAILY_TRACKER.md for adjustment guidance
