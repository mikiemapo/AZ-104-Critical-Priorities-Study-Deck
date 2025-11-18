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

# Read CSV and create notes using Front/Back format - FIXED VERSION
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        question = row['Question']
        choice_a = row['ChoiceA']
        choice_b = row['ChoiceB']
        choice_c = row['ChoiceC']  
        choice_d = row['ChoiceD']
        correct = row['Correct']
        explanation = row['Explanation']
        
        # Build front exactly like working version
        front = f"{question}\n\nA) {choice_a}\nB) {choice_b}\nC) {choice_c}\nD) {choice_d}"
        
        # Build back with correct answer and clean explanation
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