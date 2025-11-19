#!/usr/bin/env python3

import genanki
import csv

# Create the exact model that worked before
az_104_model = genanki.Model(
    1607392320,  # Original Model ID
    'AZ-104 Multiple Choice Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Tags'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{Question}}<style>.choice.correct { background-color: #4CAF50 !important; color: white !important; border-color: #45a049 !important; font-weight: bold; }</style><hr><div style="background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; margin: 10px 0; font-size: 16px;">{{Answer}}</div>',
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

# Create the deck
az_104_deck = genanki.Deck(
    2059400111,  # Original Deck ID
    'AZ-104 Critical Priorities Study Deck'
)

# Read the CSV and create notes using the WORKING format - embed choices in question text
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Build the complete question with choices embedded (this was the working format!)
        question_text = row['Question']
        choice_a = row['ChoiceA']
        choice_b = row['ChoiceB']
        choice_c = row['ChoiceC']
        choice_d = row['ChoiceD']
        correct = row['Correct']
        explanation = row['Explanation']
        tags = row['Tags']
        
        # Create question with highlighting for correct answer
        correct_letter = correct.strip()
        choice_a_class = "choice correct" if correct_letter == "A" else "choice"
        choice_b_class = "choice correct" if correct_letter == "B" else "choice"
        choice_c_class = "choice correct" if correct_letter == "C" else "choice"
        choice_d_class = "choice correct" if correct_letter == "D" else "choice"
        
        full_question = f"""{question_text}<br><br>
<div class="{choice_a_class}">A) {choice_a}</div>
<div class="{choice_b_class}">B) {choice_b}</div>
<div class="{choice_c_class}">C) {choice_c}</div>
<div class="{choice_d_class}">D) {choice_d}</div>"""
        
        # Create SHORT explanation (1-2 sentences max)
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
            words = clean_text.split()[:20]  # First 20 words max
            short_explanation = ' '.join(words) + "..."
        
        answer = f"Correct: {correct} - {short_explanation}"
        
        # Create note using Question/Answer/Tags fields
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, answer, tags]
        )
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 RESTORED working format - choices embedded in question text!")