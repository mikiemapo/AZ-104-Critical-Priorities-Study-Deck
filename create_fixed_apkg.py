#!/usr/bin/env python3

import genanki
import csv

# Use the exact same working model as create_simple_apkg.py
az_104_model_fixed = genanki.Model(
    1607392321,  # New Model ID to avoid conflicts
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
az_104_deck_fixed = genanki.Deck(
    2059400112,  # New Deck ID
    'AZ-104 Critical Priorities - FIXED'
)

# Read CSV and create notes using Front/Back format
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        question = row['Question'].strip('"')
        choice_a = row['ChoiceA'].strip('"')
        choice_b = row['ChoiceB'].strip('"')
        choice_c = row['ChoiceC'].strip('"')
        choice_d = row['ChoiceD'].strip('"')
        correct = row['Correct'].strip('"')
        explanation = row['Explanation'].strip('"')
        
        # Build front with question and choices
        front = f"{question}\n\nA) {choice_a}\nB) {choice_b}\nC) {choice_c}\nD) {choice_d}"
        
        # Build back with correct answer and explanation
        back = f"Correct Answer: {correct}\n\n{explanation}"
        
        # Create note with Front/Back fields
        note = genanki.Note(
            model=az_104_model_fixed,
            fields=[front, back]
        )
        
        az_104_deck_fixed.add_note(note)

# Generate the package
genanki.Package(az_104_deck_fixed).write_to_file('AZ-104-FIXED-Critical-Priorities.apkg')

print("✅ Successfully created AZ-104-FIXED-Critical-Priorities.apkg")
print(f"📊 Deck contains {len(az_104_deck_fixed.notes)} cards")
print("🎯 Fixed format with explicit field mapping!")
print("📝 Fields: Question, A, B, C, D, Answer, Explanation, Tags")