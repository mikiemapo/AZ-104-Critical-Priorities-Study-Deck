#!/usr/bin/env python3

import genanki
import csv
import html

# Create a model that matches Connor Sayers' AZ-104 multiple choice format
az_104_model = genanki.Model(
    1607392320,  # Unique Model ID
    'AZ-104 Multiple Choice - Connor Format',
    fields=[
        {'name': 'Question'},
        {'name': 'ChoiceA'},
        {'name': 'ChoiceB'},
        {'name': 'ChoiceC'},
        {'name': 'ChoiceD'},
        {'name': 'Correct'},
        {'name': 'Explanation'},
        {'name': 'Tags'},
        {'name': 'Source'}
    ],
    templates=[
        {
            'name': 'AZ-104 Multiple Choice',
            'qfmt': '''
<div class="question">{{Question}}</div>
<div class="choices">
  <div class="choice"><strong>A)</strong> {{ChoiceA}}</div>
  <div class="choice"><strong>B)</strong> {{ChoiceB}}</div>
  <div class="choice"><strong>C)</strong> {{ChoiceC}}</div>
  <div class="choice"><strong>D)</strong> {{ChoiceD}}</div>
</div>
''',
            'afmt': '''
<div class="question">{{Question}}</div>
<div class="choices">
  <div class="choice"><strong>A)</strong> {{ChoiceA}}</div>
  <div class="choice"><strong>B)</strong> {{ChoiceB}}</div>
  <div class="choice"><strong>C)</strong> {{ChoiceC}}</div>
  <div class="choice"><strong>D)</strong> {{ChoiceD}}</div>
</div>
<hr id="answer">
<div class="correct-answer">✅ <strong>Correct Answer: {{Correct}}</strong></div>
<div class="explanation">{{Explanation}}</div>
<div class="source">📚 Source: {{Source}}</div>
''',
        },
    ],
    css='''
.card {
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 16px;
    text-align: left;
    color: #333;
    background-color: #fafafa;
    padding: 25px;
    line-height: 1.6;
    border-radius: 8px;
    max-width: 800px;
    margin: 0 auto;
}

.question {
    font-size: 18px;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 20px;
    padding: 15px;
    background-color: #e8f4f8;
    border-left: 4px solid #3498db;
    border-radius: 4px;
}

.choices {
    margin: 20px 0;
}

.choice {
    margin: 12px 0;
    padding: 12px 15px;
    background-color: #fff;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    transition: all 0.3s ease;
}

.choice:hover {
    border-color: #3498db;
    background-color: #f8f9fa;
}

.choice strong {
    color: #2980b9;
    margin-right: 8px;
}

hr {
    border: none;
    border-top: 3px solid #3498db;
    margin: 25px 0;
    border-radius: 2px;
}

.correct-answer {
    font-size: 18px;
    font-weight: bold;
    color: #27ae60;
    background-color: #d5f4e6;
    padding: 15px;
    border-radius: 6px;
    margin: 15px 0;
    border-left: 4px solid #27ae60;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #fff;
    border-radius: 6px;
    border: 1px solid #e0e0e0;
    font-size: 15px;
    line-height: 1.6;
}

.explanation strong {
    color: #e74c3c;
}

.source {
    margin-top: 15px;
    font-size: 13px;
    color: #7f8c8d;
    font-style: italic;
    text-align: right;
}

.code {
    font-family: 'Courier New', monospace;
    background-color: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 14px;
    color: #d63384;
}

ul, ol {
    margin: 15px 0;
    padding-left: 25px;
}

li {
    margin: 8px 0;
}
'''
)

# Create the deck
az_104_deck = genanki.Deck(
    2059400111,  # Unique Deck ID
    'AZ-104 Critical Priorities Study Deck - Connor Format'
)

# Read the updated CSV format and create notes
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Clean and parse the fields
        question = row['Question'].strip('"').replace('\\n', '<br>')
        choice_a = row['ChoiceA'].strip('"')
        choice_b = row['ChoiceB'].strip('"')
        choice_c = row['ChoiceC'].strip('"')
        choice_d = row['ChoiceD'].strip('"')
        correct = row['Correct'].strip('"')
        explanation = row['Explanation'].strip('"').replace('\\n', '<br>')
        tags = row['Tags'].strip('"')
        source = row.get('Source', 'Microsoft Learn').strip('"')
        
        # Create note with proper field mapping
        note = genanki.Note(
            model=az_104_model,
            fields=[
                question,
                choice_a,
                choice_b, 
                choice_c,
                choice_d,
                correct,
                explanation,
                tags,
                source
            ]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Connor Sayers format - Professional multiple choice questions ready for Anki!")
print("📚 Each card includes question, 4 choices, correct answer, explanation, and source")