#!/usr/bin/env python3

import genanki
import csv

# Use the proven Front/Back format - EXACTLY like create_simple_apkg.py
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

# Read the CSV format and create notes - FIXED VERSION
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # NO .strip('"') - let CSV reader handle it properly
        question_text = row['Question']
        choice_a = row['ChoiceA']
        choice_b = row['ChoiceB'] 
        choice_c = row['ChoiceC']
        choice_d = row['ChoiceD']
        correct = row['Correct']
        explanation = row['Explanation']
        
        # Build the question exactly like working version
        front = f"{question_text}\n\nA) {choice_a}\nB) {choice_b}\nC) {choice_c}\nD) {choice_d}"
        
        # Build the answer with correct choice and explanation
        back = f"Correct Answer: {correct}\n\n{explanation}"
        
        # Create note using Front/Back fields
        note = genanki.Note(
            model=az_104_model,
            fields=[front, back]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Original working format restored - should display properly in Anki!")