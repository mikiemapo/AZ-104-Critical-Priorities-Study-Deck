#!/usr/bin/env python3
"""
🎯 AZ-104 Master Study Deck Generator
=====================================

⚠️  CRITICAL: DO NOT MODIFY THE TEMPLATE FORMAT BELOW
    This format fixes the "blank rectangle" issue and ensures proper display

🔧 WORKING TEMPLATE STRUCTURE:
   - qfmt: Shows Question field (white rectangles on front)
   - afmt: Shows QuestionWithAnswer field (green highlighting on back)
   - Separate fields prevent premature highlighting

📝 TO ADD NEW BATCHES:
   1. Add questions to AZ-104-Master-Questions.csv
   2. Run: python3 create_master_deck.py  
   3. Commit and push updated deck

⚡ QUESTION CREATION GUIDELINES:
   - Include misdirecting answer analysis in explanations
   - Explain why wrong answers are tempting but incorrect
   - Helps reinforce concepts by understanding common misconceptions
   - Cross-reference with Microsoft Learn documentation
   - Keep explanations to 2 sentences for the point
   - Randomize correct answers across A-D options

🎉 Maintains hierarchical subdeck structure with expandable categories
"""

import genanki
import csv

# ⚠️  DO NOT MODIFY THIS MODEL - IT FIXES THE BLANK RECTANGLE ISSUE!
# This specific template structure ensures:
# - Question field shows white rectangles on card front
# - QuestionWithAnswer field shows green highlighting on card back  
# - Prevents premature green highlighting that causes blank rectangles
az_104_model = genanki.Model(
    1607392320,  # Original Model ID
    'AZ-104 Master Questions Model',
    fields=[
        {'name': 'Question'},
        {'name': 'QuestionWithAnswer'},
        {'name': 'Answer'},
        {'name': 'Tags'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{QuestionWithAnswer}}<style>.choice.correct { background-color: #4CAF50 !important; color: white !important; border-color: #45a049 !important; font-weight: bold; }</style><hr><div style="background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; margin: 10px 0; font-size: 16px;">{{Answer}}</div>',
        },
    ],
    css="""
.card {
    font-family: Arial, sans-serif;
    font-size: 18px;
    line-height: 1.6;
    color: black;
    background-color: white;
    padding: 20px;
}

.choice {
    background-color: #f9f9f9;
    border: 2px solid #cccccc;
    padding: 12px 16px;
    margin: 10px 0;
    border-radius: 8px;
    display: block;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    color: #333333;
    font-weight: normal;
}
    """
)

# Create hierarchical decks with proper Anki subdeck naming
main_deck_name = 'AZ-104 Study Guide'
decks = {}
all_decks = []

# Create main parent deck first
main_deck = genanki.Deck(
    2059400100,
    main_deck_name
)
all_decks.append(main_deck)

# Track batches and create subdecks with double colon notation
with open('AZ-104-Master-Questions.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        batch = row.get('Batch', '')
        if not batch:
            continue
        if batch not in decks:
            # Create subdeck using SEGMENTED hierarchy
            clean_batch = batch.replace(' Batch', '').replace('/', ' & ')
            
            if 'Golden Rule' in batch:
                # Golden Rules segment
                subdeck_name = f"{main_deck_name}::Golden Rules::{clean_batch}"
            elif 'Deep Dive' in batch:
                # Deep Dives segment
                subdeck_name = f"{main_deck_name}::Deep Dives::{clean_batch}"
            elif 'Performance Review' in batch:
                # Performance Review segment
                subdeck_name = f"{main_deck_name}::Performance Review::{clean_batch}"
            else:
                # Study Guide Cards segment (everything else)
                subdeck_name = f"{main_deck_name}::Study Guide Cards::{clean_batch}"
            
            # Generate CONSISTENT deck ID from batch name hash (same batch = same ID always)
            import hashlib
            deck_id = int(hashlib.md5(batch.encode()).hexdigest()[:8], 16)
            # Ensure ID is positive and in valid range
            deck_id = 2059400111 + (deck_id % 10000)
                
            decks[batch] = genanki.Deck(
                deck_id,  # Consistent deck ID based on batch name
                subdeck_name
            )
            all_decks.append(decks[batch])
            print(f"📁 Created subdeck: {subdeck_name}")

print(f"\n🔄 Processing questions into subdecks...")

# Read again and add notes to appropriate subdecks
current_batch = ""
batch_count = {}

with open('AZ-104-Master-Questions.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Track batches
        batch = row.get('Batch', '')
        if not batch:
            continue
        if batch != current_batch:
            current_batch = batch
            batch_count[batch] = batch_count.get(batch, 0)
        batch_count[batch] += 1
        
        # Build questions using WORKING format (DO NOT CHANGE!)
        question_text = row.get('Question', '')
        choice_a = row.get('ChoiceA', '')
        choice_b = row.get('ChoiceB', '')
        choice_c = row.get('ChoiceC', '')
        choice_d = row.get('ChoiceD', '')
        correct = row.get('Correct', 'A')
        explanation = row.get('Explanation', '')
        tags = f"{row.get('Tags', '')},{batch}"
        
        # Create question with NO highlighting for front side
        full_question = f"""{question_text}<br><br>
<div class="choice">A) {choice_a}</div>
<div class="choice">B) {choice_b}</div>
<div class="choice">C) {choice_c}</div>
<div class="choice">D) {choice_d}</div>"""

        # Create question WITH highlighting for back side
        correct_letter = correct.strip()
        choice_a_class = "choice correct" if correct_letter == "A" else "choice"
        choice_b_class = "choice correct" if correct_letter == "B" else "choice"
        choice_c_class = "choice correct" if correct_letter == "C" else "choice"
        choice_d_class = "choice correct" if correct_letter == "D" else "choice"
        
        question_with_answer = f"""{question_text}<br><br>
<div class="{choice_a_class}">A) {choice_a}</div>
<div class="{choice_b_class}">B) {choice_b}</div>
<div class="{choice_c_class}">C) {choice_c}</div>
<div class="{choice_d_class}">D) {choice_d}</div>"""

        # Create SHORT explanation based on batch
        if 'Critical Priorities' in batch:
            # Keep existing short explanations for critical priorities
            if 'auto-swap' in question_text.lower():
                short_explanation = "Create deployment slot first, configure warm-up, then enable auto-swap for automatic staging-to-production deployment."
            elif 'VNet Integration' in explanation:
                short_explanation = "Must establish VNet integration and service endpoints BEFORE disabling public access to prevent connectivity loss."
            elif 'Three-Layer Security' in explanation:
                short_explanation = "Combine Microsoft Defender (scanning) + ACR Tasks (CI/CD) + Azure Policy (enforcement) for complete security."
            elif 'ACI' in explanation and 'scaling' in explanation:
                short_explanation = "ACI has no auto-scaling - must delete and redeploy container group with new specs (unlike AKS HPA)."
            elif 'Container Apps' in explanation:
                short_explanation = "External = internet access, Internal = VNet only, Disabled = background jobs only."
            else:
                # Generic short explanation
                clean_text = explanation.replace('<strong>', '').replace('</strong>', '').replace('<br>', ' ')
                words = clean_text.split()[:20]
                short_explanation = ' '.join(words) + "..."
        else:
            # For other batches, use the explanation as provided (already short)
            short_explanation = explanation.replace('<strong>', '').replace('</strong>', '').replace('<br>', ' ')
        
        answer = f"Correct: {correct} - {short_explanation}"
        
        # Create note using WORKING format (DO NOT CHANGE!)
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, question_with_answer, answer, tags]
        )
        
        # Add note to the appropriate subdeck
        decks[batch].add_note(note)

# Generate the package with all subdecks
genanki.Package(all_decks).write_to_file('AZ-104-Master-Study-Deck.apkg')

total_cards = sum(len(deck.notes) for deck in all_decks)
print(f"\n✅ Successfully created AZ-104-Master-Study-Deck.apkg with hierarchical structure")
print(f"📊 Total cards: {total_cards}")
print(f"📚 Subdeck structure:")
for batch, count in batch_count.items():
    print(f"   📁 {main_deck_name}::{batch}: {count} cards")
print("🎯 WORKING format preserved with expandable subdeck structure!")