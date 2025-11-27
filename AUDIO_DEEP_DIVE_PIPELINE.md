# Audio Deep Dive to Anki Deck Pipeline

## Overview
Convert audio transcripts (Deep Dive explainer series) into focused Anki decks using the **Enriched scenario-based format**.

---

## Current Status

### ✅ Completed Decks (2)
1. **VMSS Deep Dive** (12 cards)
   - Orchestration modes (Uniform vs. Flexible)
   - Update Domains, Fault Domains
   - Availability Zones
   - Load Balancer session persistence
   - VMSS vs. App Service trade-off

2. **App Service Deep Dive** (17 cards)
   - OS constraints (Windows-only .NET Framework, Linux-only multi-container)
   - Runtime choices & deployment methods
   - Resource contention management
   - VNet integration tier requirements
   - Slot swaps for zero-downtime
   - Bicep IaC (serverFarmId, linuxFxVersion)
   - Container security pipeline
   - ROADMAP mnemonic & exam traps

### 📋 Pending/In-Queue (To Process)
- [ ] [Topic needed] - audio file reference/link

---

## Workflow: Audio → Anki Deck

### Phase 1: Transcript Extraction
- Source: Audio file (.mp3, .wav, .m4a)
- Tool: `openai-whisper` (local, offline)
- Output: `transcript.txt`

### Phase 2: Topic Analysis
- Read transcript
- Identify key concepts, decision frameworks, golden rules
- Extract scenario examples from speaker dialogue

### Phase 3: Question Generation
- Convert topics into **Enriched scenario-based Q&A**
- Include: use-case context, constraints, trade-offs, gotchas
- Format: CSV (Question, ChoiceA-D, Correct, Explanation, Tags, Source, Batch)
- Keep explanations ≤2 sentences

### Phase 4: Integration
- Create `AZ104_[Topic]_Deep_Dive.csv`
- Append to `AZ-104-Master-Questions.csv`
- Run `python3 create_master_deck.py`
- Update README with new batch count
- Commit & push to GitHub

---

## Format Rules (Enriched Style)

```
Question,ChoiceA,ChoiceB,ChoiceC,ChoiceD,Correct,Explanation,Tags,Source,Batch
"A [scenario with constraint]. What is [the decision/concept]?","Wrong","Correct answer","Wrong","Wrong","B","[Explanation with trade-off or constraint detail]. [Actionable guidance or best practice].","Topic,Concept,Deep Dive","Deep Dive: [Topic]","[Topic] Deep Dive Batch"
```

### Key Elements
- **Scenario**: Real-world use-case or problem
- **Constraints**: Specific numbers, timeframes, limitations
- **Correct answer**: Clear, defensible
- **Explanation**: Why correct + when applicable + trade-offs
- **Tags**: Topic tags for filtering (VMSS, App Service, Storage, etc.)
- **Source**: "Deep Dive: [Topic]"
- **Batch**: "[Topic] Deep Dive Batch"

---

## Tracking Template

Use this to log incoming audio files:

```
| Audio File | Topic | Speaker(s) | Duration | Status | Deck Name | Card Count | Notes |
|-----------|-------|-----------|----------|--------|-----------|-----------|-------|
| vmss_deep_dive.mp3 | VMSS Orchestration | [names] | ~45 min | ✅ Complete | VMSS Deep Dive | 12 | Covers orchestration modes, FD/UD, AZ |
| app_service_deep_dive.mp3 | App Service | [names] | ~50 min | ✅ Complete | App Service Deep Dive | 17 | OS constraints, deployment methods, Bicep |
| [next_topic].mp3 | [Topic] | [names] | [duration] | 📋 Queued | — | — | [notes] |
```

---

## Quick Reference: When to Recommend Anki Deck

**Look for these patterns in user questions:**
- "How do I remember the difference between X and Y?"
- "What are the trade-offs for this Azure service?"
- "What's the exam trap here?"
- "I keep getting this wrong..."
- Multiple questions about a single topic/service

**Response template:**
> "I notice you're asking several questions about [Topic]. Would you like me to extract that Deep Dive audio into a focused Anki batch? I can create [estimated count] scenario-based cards covering [key areas] and add them to your deck. Takes ~30 min, results in production-ready cards."

---

## Future Automation: Local Transcription + Deck Generation

### Architecture (For Later Sprint)
```
audio_file
    ↓
[faster-whisper] → transcript.txt
    ↓
[topic_extractor.py] → key_concepts.json
    ↓
[deck_generator.py + Claude/GPT] → questions.csv
    ↓
[append_to_master.py] → master CSV updated
    ↓
[create_master_deck.py] → .apkg rebuilt
    ↓
[git_push.sh] → GitHub updated
```

**Tools needed:**
- `faster-whisper` (faster alternative to OpenAI Whisper)
- Python script for topic extraction
- Prompt template for Q&A generation (Claude/GPT API or local LLM)
- CSV append logic
- Git automation

**Effort estimate:** 4-6 hours setup, 30 sec per audio file after automation complete.

**ROI trigger:** After 10-15 more audio Deep Dives processed manually, automation pays for itself.

---

## Current Deck Stats
- **Total Cards:** 380
- **Batches:** 20
- **Deep Dive Batches:** 2 (VMSS, App Service)
- **Last Updated:** November 26, 2025

---

## Notes
- Each Deep Dive typically yields 12-20 cards
- Maintain enriched scenario-based format across all new batches
- Golden Rule questions recommended per Deep Dive
- Include exam traps/critical gotchas when relevant
- All source links to official MS Learn documentation
