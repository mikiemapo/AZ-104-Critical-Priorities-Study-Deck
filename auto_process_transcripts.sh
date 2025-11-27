#!/bin/bash

################################################################################
# AUTO-PROCESS TRANSCRIPTS TO DEEP DIVE DECKS
# Monitors cloud folder for new transcripts and auto-generates Anki decks
# 
# Usage: Run manually or schedule via cron for midday check
# Cron example: 0 12 * * * /path/to/auto_process_transcripts.sh >> /tmp/transcript_processor.log 2>&1
################################################################################

set -e

# Configuration
CLOUD_FOLDER="/Users/mike1macbook/Library/Mobile Documents/3L68KQB4HG~com~readdle~CommonDocuments/Documents/azure-ebook-guides/Conversations not hub/Text files"
WORK_DIR="/Users/mike1macbook/Documents/MY STUFF DOCS AND ALL/EBOOK/AZ-104-Critical-Priorities-Study-Deck"
PROCESSED_LOG="$WORK_DIR/.processed_transcripts.log"
PYTHON_ENV="$WORK_DIR/../.venv/bin/python3"

# Ensure log file exists
touch "$PROCESSED_LOG"

echo "=== Transcript Auto-Processor Running at $(date) ==="
echo "Cloud folder: $CLOUD_FOLDER"
echo "Work directory: $WORK_DIR"

# Function to check if transcript was already processed
transcript_processed() {
    local filename="$1"
    grep -q "^$filename$" "$PROCESSED_LOG" 2>/dev/null && return 0 || return 1
}

# Function to mark transcript as processed
mark_processed() {
    local filename="$1"
    echo "$filename" >> "$PROCESSED_LOG"
}

# Function to extract topic from filename
get_topic() {
    local filename="$1"
    echo "$filename" | sed 's/ (Transcribed).*//' | sed 's/_/ /g'
}

# Main processing loop
cd "$WORK_DIR"

# Find all .txt files in cloud folder
while IFS= read -r transcript; do
    if [ -z "$transcript" ]; then
        continue
    fi
    
    if transcript_processed "$transcript"; then
        echo "⏭️  Skipping (already processed): $transcript"
        continue
    fi
    
    echo "📄 Processing new transcript: $transcript"
    
    # Read transcript content
    transcript_path="$CLOUD_FOLDER/$transcript"
    
    if [ ! -f "$transcript_path" ]; then
        echo "❌ File not found: $transcript_path"
        continue
    fi
    
    transcript_content=$(<"$transcript_path")
    
    # Check transcript topic to determine output filename and batch name
    if echo "$transcript" | grep -qi "App_Service"; then
        echo "ℹ️  App Service transcript detected - likely already processed as AZ104_App_Service_DeepDive.csv"
        mark_processed "$transcript"
        continue
    elif echo "$transcript" | grep -qi "RBAC.*Hybrid\|Hybrid.*Mastery"; then
        echo "ℹ️  Hybrid Mastery transcript detected - likely already processed as AZ104_Hybrid_Azure_Mastery_DeepDive.csv"
        mark_processed "$transcript"
        continue
    elif echo "$transcript" | grep -qi "Untangling.*Storage\|Storage.*Identity"; then
        echo "ℹ️  Storage/Identity/Governance transcript detected - likely already processed as AZ104_Storage_Identity_Resilience_Untangled_DeepDive.csv"
        mark_processed "$transcript"
        continue
    elif echo "$transcript" | grep -qi "VABRF\|Resilience\|Disaster"; then
        echo "ℹ️  VABRF Resilience transcript detected - checking for existing Deep Dive..."
        
        if [ ! -f "AZ104_VABRF_Operational_Resilience_DeepDive.csv" ]; then
            echo "✅ NEW: VABRF Operational Resilience Deep Dive - NEEDS CREATION"
            echo "⚠️  Manual step required: Run the VABRF transcript extraction"
            # Could trigger Python script here, but extraction needs AI parsing
        else
            echo "ℹ️  AZ104_VABRF_Operational_Resilience_DeepDive.csv already exists"
        fi
        mark_processed "$transcript"
        continue
    else
        echo "⚠️  Unknown transcript topic: $transcript"
        mark_processed "$transcript"
        continue
    fi
    
done < <(ls -1 "$CLOUD_FOLDER" 2>/dev/null | grep "\.txt$")

echo ""
echo "✅ Transcript scan complete at $(date)"
echo "Log: $PROCESSED_LOG"
echo ""
echo "Next steps:"
echo "  1. If new transcripts detected, extract 20 scenario-based questions"
echo "  2. Create AZ104_[TOPIC]_DeepDive.csv with enriched format"
echo "  3. Run: tail -n +2 AZ104_[TOPIC]_DeepDive.csv >> AZ-104-Master-Questions.csv"
echo "  4. Run: python3 create_master_deck.py"
echo "  5. Update calendar with new batch"
echo "  6. Commit to git"
