#!/usr/bin/env python3
"""
Create Performance Review deck - targets Nov 29 Identities quiz weak spots
Deck Name: AZ-104 Performance Review::Identities Nov 29
"""

import genanki
import csv

# Use the same model format as master deck
review_model = genanki.Model(
    1607392321,
    'AZ-104 Performance Review Model',
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
            'afmt': '''{{QuestionWithAnswer}}<hr><div style="margin-top: 20px; padding: 15px; background-color: #e8f5e9; border-left: 4px solid #4caf50; border-radius: 4px;"><strong>✓ Answer:</strong> {{Answer}}</div>''',
        }
    ],
    css="""
.card {
    font-family: Arial, sans-serif;
    font-size: 18px;
    text-align: left;
    color: #333333;
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

.choice.correct {
    background-color: #d4edda;
    border: 2px solid #28a745;
    font-weight: bold;
}
    """
)

# Create deck
deck = genanki.Deck(
    2089456789,
    'AZ-104 Performance Review::Identities Nov 29'
)

# Read master CSV and filter for Identities & Governance batch
with open('AZ-104-Master-Questions.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    card_count = 0
    
    for row in reader:
        batch = row.get('Batch', '')
        if not batch or ('Identities' not in batch and 'Governance' not in batch):
            continue
            
        # Build question (no highlighting)
        question_text = row.get('Question', '')
        choice_a = row.get('ChoiceA', '')
        choice_b = row.get('ChoiceB', '')
        choice_c = row.get('ChoiceC', '')
        choice_d = row.get('ChoiceD', '')
        
        full_question = f"""{question_text}<br><br>
<div class="choice">A) {choice_a}</div>
<div class="choice">B) {choice_b}</div>
<div class="choice">C) {choice_c}</div>
<div class="choice">D) {choice_d}</div>"""

        # Build question with answer highlighting
        correct = row.get('Correct', 'A').strip()
        choice_a_class = "choice correct" if correct == "A" else "choice"
        choice_b_class = "choice correct" if correct == "B" else "choice"
        choice_c_class = "choice correct" if correct == "C" else "choice"
        choice_d_class = "choice correct" if correct == "D" else "choice"
        
        question_with_answer = f"""{question_text}<br><br>
<div class="{choice_a_class}">A) {choice_a}</div>
<div class="{choice_b_class}">B) {choice_b}</div>
<div class="{choice_c_class}">C) {choice_c}</div>
<div class="{choice_d_class}">D) {choice_d}</div>"""

        explanation = row.get('Explanation', '')
        tags = row.get('Tags', '').split(',')
        tags.append('PerformanceReview')
        tags.append('Nov29Quiz')
        
        note = genanki.Note(
            model=review_model,
            fields=[full_question, question_with_answer, explanation, ','.join(tags)],
            tags=tags
        )
        deck.add_note(note)
        card_count += 1

# Write deck
output_file = '../AZ-104-Performance-Review-Identities-Nov29.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Created: {output_file}")
print(f"📚 Deck: AZ-104 Performance Review::Identities Nov 29")
print(f"🎴 Cards: {card_count}")
print(f"🎯 Targets: Nov 29 Identities & Governance quiz weak spots")
