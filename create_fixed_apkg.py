#!/usr/bin/env python3

import genanki
import csv

# Create a more explicit model with very specific field names
az_104_model_fixed = genanki.Model(
    1607392321,  # New Model ID to avoid conflicts
    'AZ-104 MCQ Fixed Format',
    fields=[
        {'name': 'Question'},
        {'name': 'A'},
        {'name': 'B'}, 
        {'name': 'C'},
        {'name': 'D'},
        {'name': 'Answer'},
        {'name': 'Explanation'},
        {'name': 'Tags'}
    ],
    templates=[
        {
            'name': 'Multiple Choice',
            'qfmt': '''
<div style="font-size: 18px; margin-bottom: 20px;">{{Question}}</div>
<div style="margin: 15px 0;">
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>A)</strong> {{A}}</div>
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>B)</strong> {{B}}</div>
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>C)</strong> {{C}}</div>
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>D)</strong> {{D}}</div>
</div>
''',
            'afmt': '''
<div style="font-size: 18px; margin-bottom: 20px;">{{Question}}</div>
<div style="margin: 15px 0;">
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>A)</strong> {{A}}</div>
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>B)</strong> {{B}}</div>
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>C)</strong> {{C}}</div>
  <div style="margin: 8px 0; padding: 10px; border: 1px solid #ddd;"><strong>D)</strong> {{D}}</div>
</div>
<hr style="border: 2px solid #3498db; margin: 20px 0;">
<div style="font-size: 18px; color: green; margin: 15px 0;"><strong>✓ Correct Answer: {{Answer}}</strong></div>
<div style="margin-top: 20px;">{{Explanation}}</div>
''',
        },
    ]
)

# Create the deck
az_104_deck_fixed = genanki.Deck(
    2059400112,  # New Deck ID
    'AZ-104 Critical Priorities - FIXED'
)

# Read CSV and create notes with simple field mapping
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
        tags = row['Tags'].strip('"')
        
        # Create note with simple field mapping
        note = genanki.Note(
            model=az_104_model_fixed,
            fields=[
                question,
                choice_a,
                choice_b,
                choice_c, 
                choice_d,
                correct,
                explanation,
                tags
            ]
        )
        
        az_104_deck_fixed.add_note(note)

# Generate the package
genanki.Package(az_104_deck_fixed).write_to_file('AZ-104-FIXED-Critical-Priorities.apkg')

print("✅ Successfully created AZ-104-FIXED-Critical-Priorities.apkg")
print(f"📊 Deck contains {len(az_104_deck_fixed.notes)} cards")
print("🎯 Fixed format with explicit field mapping!")
print("📝 Fields: Question, A, B, C, D, Answer, Explanation, Tags")