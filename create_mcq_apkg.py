#!/usr/bin/env python3

import genanki
import csv
import html

# Create a model that matches standard Anki multiple choice format
az_104_model = genanki.Model(
    1607392320,  # New Model ID
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
    2059400111,  # New Deck ID
    'AZ-104 Critical Priorities Study Deck'
)

# Read CSV and create notes
with open('AZ-104-Multiple-Choice.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Clean the fields
        question = row['Front'].strip('"')
        answer = row['Back'].strip('"')
        tags = row['Tags'].strip('"')
        
        # Escape HTML properly
        question = html.escape(question, quote=False).replace('\n', '<br>')
        answer = html.escape(answer, quote=False).replace('\n', '<br>')
        
        # Fix the strong tags that got escaped
        question = question.replace('&lt;strong&gt;', '<strong>').replace('&lt;/strong&gt;', '</strong>')
        answer = answer.replace('&lt;strong&gt;', '<strong>').replace('&lt;/strong&gt;', '</strong>')
        
        # Create note
        note = genanki.Note(
            model=az_104_model,
            fields=[question, answer, tags]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Properly formatted multiple choice questions ready for Anki!")