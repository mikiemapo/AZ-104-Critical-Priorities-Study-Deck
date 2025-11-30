#!/usr/bin/env python3
"""
Create Anki deck from Microsoft Entra ID Cheat Sheet CSV
Deck Name: AZ-104 Study Guide::Identities & Governance::Microsoft Entra ID
"""

import genanki
import csv

# Create a simple model for basic flashcards
entra_model = genanki.Model(
    1891234567,
    'Microsoft Entra ID Basic',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Tags'},
        {'name': 'Source'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div style="font-size: 20px; text-align: center; padding: 20px;">{{Question}}</div>',
            'afmt': '''<div style="font-size: 20px; text-align: center; padding: 20px;">{{Question}}</div>
                       <hr>
                       <div style="font-size: 18px; background-color: #d4edda; padding: 15px; border-radius: 5px;">
                       {{Answer}}
                       </div>
                       <div style="font-size: 12px; color: #666; margin-top: 10px;">Source: {{Source}}</div>'''
        }
    ]
)

# Create deck with proper hierarchy
deck = genanki.Deck(
    2089123456,
    'AZ-104 Study Guide::Identities & Governance::Microsoft Entra ID'
)

# Read CSV and add cards
csv_file = 'Personalized-Review-Decks/Microsoft_Entra_ID_Cheat_Sheet.csv'

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        note = genanki.Note(
            model=entra_model,
            fields=[
                row['Question'],
                row['Answer'],
                row['Tags'],
                row['Source']
            ],
            tags=row['Tags'].split(',')
        )
        deck.add_note(note)

# Generate the .apkg file
output_file = '../Microsoft_Entra_ID_Study_Deck.apkg'
genanki.Package(deck).write_to_file(output_file)

print(f"✅ Created: {output_file}")
print(f"📚 Deck: AZ-104 Study Guide::Identities & Governance::Microsoft Entra ID")
print(f"🎴 Cards: {len(deck.notes)}")
