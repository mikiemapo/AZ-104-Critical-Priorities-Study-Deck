#!/usr/bin/env python3

import genanki
import csv
import random

# Create a custom model that matches standard Anki multiple choice format
az_104_model = genanki.Model(
    1607392319,  # Model ID
    'AZ-104 Standard Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Tags'},
        {'name': 'Type'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '<div class="question">{{Question}}</div><hr id="answer"><div class="answer">{{Answer}}</div>',
        },
    ],
    css='''
.card {
    font-family: Arial, sans-serif;
    font-size: 18px;
    text-align: left;
    color: #000;
    background-color: #fff;
    padding: 20px;
}

.question {
    font-weight: normal;
    margin-bottom: 15px;
    line-height: 1.4;
    color: #000;
}

.answer {
    margin-top: 15px;
    line-height: 1.4;
    color: #000;
}

.correct {
    font-weight: bold;
    color: #0066cc;
}

.incorrect {
    color: #666;
}

hr {
    border: none;
    border-top: 1px solid #ccc;
    margin: 15px 0;
}

strong {
    color: #0066cc;
    font-weight: bold;
}

em {
    font-style: italic;
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
        
        # Clean up HTML and formatting issues
        front = front.replace('*', '')  # Remove asterisks
        back = back.replace('<br>', '\n').replace('<br/>', '\n')  # Convert breaks to newlines
        back = back.replace('**', '<strong>').replace('**', '</strong>')  # Fix bold formatting
        
        # Create note with clean formatting
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