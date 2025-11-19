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
        {'name': 'Explanation'},
        {'name': 'Tags'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{Question}}<hr id="answer"><div style="background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; font-weight: bold; margin: 10px 0;">{{Answer}}</div><div style="background-color: #f0f8f0; color: #333; padding: 10px; border-radius: 5px; border-left: 4px solid #4CAF50; margin: 10px 0;"><strong>Why:</strong> {{Explanation}}</div>',
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
    background-color: white;
    border: 1px solid #ddd;
    padding: 8px 12px;
    margin: 5px 0;
    border-radius: 4px;
    display: block;
}

#answer {
    border: 2px solid #4CAF50;
    margin: 20px 0;
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
        
        # Combine question and choices for the Question field with proper line breaks and white backgrounds
        full_question = f"""{question_text}<br><br><div class="choice">A) {choice_a}</div><div class="choice">B) {choice_b}</div><div class="choice">C) {choice_c}</div><div class="choice">D) {choice_d}</div>"""
        
        # Create the answer with correct choice and SHORT explanation
        # Extract key points from the full explanation for concise summary
        explanation_text = explanation.replace('<strong>', '').replace('</strong>', '').replace('<br><br>', ' ').replace('<br>', ' ')
        
        # Create short summary (first 2-3 key points only)
        if 'Step-by-Step Process:' in explanation_text:
            summary = explanation_text.split('Step-by-Step Process:')[1].split('Key Benefits:')[0][:200] + "..."
        elif 'Critical Sequence' in explanation_text:
            summary = "Follow the sequence: VNet Integration → Service Endpoint → Firewall Rules → Disable Public Access"
        elif 'Three-Layer Security' in explanation_text:
            summary = "Use Microsoft Defender (scanning) + ACR Tasks (CI/CD automation) + Azure Policy (enforcement)"
        elif 'ACI Fundamental Limitation' in explanation_text:
            summary = "ACI has NO auto-scaling - must delete and redeploy with new specs (unlike AKS HPA)"
        elif 'External Ingress' in explanation_text:
            summary = "External = internet access, Internal = VNet only, Disabled = background jobs"
        else:
            # Generic short summary for other questions
            words = explanation_text.split()[:25]  # First 25 words
            summary = ' '.join(words) + "..."
        
        answer = f"Correct Answer: {correct}"
        
        # Create note using Question/Answer/Explanation/Tags fields
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, answer, summary, tags]
        )
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 RESTORED working format - choices embedded in question text!")