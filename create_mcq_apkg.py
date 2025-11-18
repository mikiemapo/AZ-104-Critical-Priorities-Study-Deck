#!/usr/bin/env python3

import genanki
import csv
import html

# Create a model that matches your original working format
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
            'afmt': '{{Question}}<hr id="answer">{{Answer}}',
        },
    ],
    css='''
.card {
    font-family: Arial, sans-serif;
    font-size: 16px;
    text-align: left;
    color: #333;
    background-color: #fff;
    padding: 20px;
    line-height: 1.5;
}

.question {
    margin-bottom: 20px;
}

.answer {
    margin-top: 15px;
}

hr {
    border: none;
    border-top: 2px solid #0066cc;
    margin: 20px 0;
}

strong {
    color: #0066cc;
    font-weight: bold;
}

.correct {
    color: #0066cc;
    font-weight: bold;
}

ul, ol {
    margin: 10px 0;
    padding-left: 20px;
}

li {
    margin: 5px 0;
}
'''
)

# Create the deck
az_104_deck = genanki.Deck(
    2059400111,  # Original Deck ID
    'AZ-104 Critical Priorities Study Deck'
)

# Read the updated CSV format and create notes
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Build the complete question with choices
        question_text = row['Question'].strip('"')
        choice_a = row['ChoiceA'].strip('"')
        choice_b = row['ChoiceB'].strip('"')
        choice_c = row['ChoiceC'].strip('"')
        choice_d = row['ChoiceD'].strip('"')
        
        # Combine question and choices for the front
        full_question = f"""{question_text}

A) {choice_a}

B) {choice_b}

C) {choice_c}

D) {choice_d}"""
        
        # Use explanation as the back
        answer = row['Explanation'].strip('"')
        tags = row['Tags'].strip('"')
        
        # Create note using original field mapping
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, answer, tags]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Original working format restored - should display properly in Anki!")