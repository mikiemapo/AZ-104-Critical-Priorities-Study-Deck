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
            'afmt': '{{Answer}}',
        },
    ],
    css="""
.card {
 font-family: arial;
 font-size: 20px;
 text-align: left;
 color: black;
 background-color: white;
}
.question {
 margin-bottom: 20px;
}
#answer {
 border: 2px solid #0066cc;
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
        
        # Combine question and choices for the Question field with proper line breaks
        full_question = f"""{question_text}<br><br>A) {choice_a}<br><br>B) {choice_b}<br><br>C) {choice_c}<br><br>D) {choice_d}"""
        
        # Create the answer with correct choice and explanation
        answer = f"Correct Answer: {correct}\n\n{explanation}"
        
        # Create note using Question/Answer/Tags fields (the working format!)
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