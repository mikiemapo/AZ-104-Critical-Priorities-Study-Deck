#!/usr/bin/env python3

import genanki
import csv
import random

# Create a custom model for AZ-104 cards
az_104_model = genanki.Model(
    1607392319,  # Model ID
    'AZ-104 Critical Priorities Model',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'},
        {'name': 'Tags'},
        {'name': 'Type'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
        },
    ],
    css='''
.card {
    font-family: arial;
    font-size: 20px;
    text-align: center;
    color: black;
    background-color: white;
}

.card.front {
    background-color: #f8f9fa;
}

.question {
    font-weight: bold;
    margin-bottom: 20px;
    padding: 20px;
    border-left: 4px solid #007acc;
    background-color: #f0f8ff;
}

.answer {
    text-align: left;
    margin: 20px 0;
    line-height: 1.6;
}

.priority-critical {
    border-color: #dc3545;
    background-color: #ffe6e6;
}

.priority-high {
    border-color: #fd7e14;
    background-color: #fff3e0;
}

.priority-medium {
    border-color: #ffc107;
    background-color: #fffde7;
}

.priority-low {
    border-color: #28a745;
    background-color: #e8f5e8;
}

strong, b {
    color: #0066cc;
}

ul, ol {
    text-align: left;
    margin: 10px 20px;
}

code {
    background-color: #f1f1f1;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
}
'''
)

# Create the deck
az_104_deck = genanki.Deck(
    2059400110,  # Deck ID
    'AZ-104 Critical Priorities Study Deck'
)

# Read CSV and create notes
with open('AZ-104-Critical-Priorities-Study-Deck.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Clean the fields by removing quotes if present
        front = row['Front'].strip('"')
        back = row['Back'].strip('"')
        tags = row['Tags'].strip('"')
        card_type = row['Type'].strip('"')
        
        # Add priority class based on tags
        if 'Critical Priority' in tags:
            front = f'<div class="question priority-critical">{front}</div>'
        elif 'High Priority' in tags:
            front = f'<div class="question priority-high">{front}</div>'
        elif 'Medium Priority' in tags:
            front = f'<div class="question priority-medium">{front}</div>'
        else:
            front = f'<div class="question priority-low">{front}</div>'
        
        back = f'<div class="answer">{back}</div>'
        
        # Create note
        note = genanki.Note(
            model=az_104_model,
            fields=[front, back, tags, card_type]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Ready for import into Anki!")