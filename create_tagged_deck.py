#!/usr/bin/env python3

import genanki
import csv

# Create the WORKING model (DO NOT CHANGE THIS!)
az_104_model = genanki.Model(
    1607392320,  # Original Model ID
    'AZ-104 Study Guide Model',
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

# Create a single deck with tag-based organization
az_104_deck = genanki.Deck(
    2059400200,
    'AZ-104 Study Guide'
)

# Read the master CSV and create notes with hierarchical tags
batch_count = {}

with open('AZ-104-Master-Questions.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        batch = row['Batch']
        batch_count[batch] = batch_count.get(batch, 0) + 1
        
        # Build questions using WORKING format (DO NOT CHANGE!)
        question_text = row['Question']
        choice_a = row['ChoiceA']
        choice_b = row['ChoiceB']
        choice_c = row['ChoiceC']
        choice_d = row['ChoiceD']
        correct = row['Correct']
        explanation = row['Explanation']
        
        # Create hierarchical tags
        if 'Critical' in batch:
            domain_tag = "Critical_Priorities"
        elif 'RTO' in batch:
            domain_tag = "Storage_Recovery"
        else:
            domain_tag = batch.replace(' ', '_').replace('/', '_')
            
        tags = f"AZ-104 {domain_tag} {row['Tags']}"
        
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
                clean_text = explanation.replace('<strong>', '').replace('</strong>', '').replace('<br>', ' ')
                words = clean_text.split()[:20]
                short_explanation = ' '.join(words) + "..."
        else:
            short_explanation = explanation.replace('<strong>', '').replace('</strong>', '').replace('<br>', ' ')
        
        answer = f"Correct: {correct} - {short_explanation}"
        
        # Create note using WORKING format (DO NOT CHANGE!)
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, question_with_answer, answer, tags]
        )
        
        az_104_deck.add_note(note)

# Generate the package with single deck + hierarchical tags
genanki.Package(az_104_deck).write_to_file('AZ-104-Study-Guide-Tagged.apkg')

print(f"\n✅ Successfully created AZ-104-Study-Guide-Tagged.apkg with tag-based organization")
print(f"📊 Total cards: {len(az_104_deck.notes)}")
print(f"📚 Tag-based organization:")
for batch, count in batch_count.items():
    if 'Critical' in batch:
        tag = "Critical_Priorities"
    elif 'RTO' in batch:
        tag = "Storage_Recovery"
    else:
        tag = batch.replace(' ', '_')
    print(f"   🏷️  {tag}: {count} cards")
print("🎯 Single deck with hierarchical tags - may create Connor-style expandable structure!")