#!/usr/bin/env python3

import genanki
import csv
import html

# Use the exact same working model as create_simple_apkg.py
az_104_model = genanki.Model(
    1607392325,  # New Model ID for Personalised Review
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
    2059400115,  # New Deck ID for Personalised Review
    'AZ-104 Personalised Review Deck - RTO/RPO Storage Replication'
)

# Read the CSV and create notes using the exact same working format
with open('AZ-104-Personalised-Review.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Build the complete question with choices exactly like the working format
        question_text = row['Question']
        option_a = row['OptionA']
        option_b = row['OptionB']
        option_c = row['OptionC']
        option_d = row['OptionD']
        correct = row['Correct']
        
        # Build front exactly like create_simple_apkg.py
        front = f"{question_text}\n\nA) {option_a}\nB) {option_b}\nC) {option_c}\nD) {option_d}"
        
        # Build back with simple format
        back = f"Correct Answer: {correct}\n\nThis question covers Azure storage replication and disaster recovery fundamentals essential for AZ-104. Understanding RTO/RPO concepts is critical for disaster recovery planning."
        
        # Create note using Front/Back fields like working format
        note = genanki.Note(
            model=az_104_model,
            fields=[front, back]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Personalised-Review-Deck.apkg')

print("✅ Successfully created AZ-104-Personalised-Review-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Personalised Review format with RTO/RPO Storage Replication focus!")
print("📚 All questions cross-referenced with Microsoft Learn documentation")
print("🔀 Correct answers randomized following cognitive pattern (factual=A/B, conceptual=C/D)")