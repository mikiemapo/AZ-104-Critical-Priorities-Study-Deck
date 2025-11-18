#!/usr/bin/env python3

import genanki
import csv
import html

# Use the proven Front/Back format
az_104_model = genanki.Model(
    1607392320,  # Original Model ID
    'Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{FrontSide}}\n\n<hr id="answer">\n\n{{Back}}',
        },
    ]
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
        correct = row['Correct'].strip('"')
        explanation = row['Explanation'].strip('"')
        
        # Combine question and choices for the front
        full_question = f"{question_text}\n\nA) {choice_a}\nB) {choice_b}\nC) {choice_c}\nD) {choice_d}"
        
        # Create the answer with correct choice and explanation
        answer = f"Correct Answer: {correct}\n\n{explanation}"
        
        # Create note using Front/Back fields
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, answer]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Original working format restored - should display properly in Anki!")