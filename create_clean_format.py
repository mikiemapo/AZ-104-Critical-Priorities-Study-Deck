#!/usr/bin/env python3

import genanki
import csv

# Create a model with clear separation between question and answer
az_104_model = genanki.Model(
    1607392321,  # Different model ID to avoid conflicts
    'AZ-104 Clean Q&A Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Tags'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="question">{{Question}}</div>',
            'afmt': '<div class="question">{{Question}}</div><hr><div class="answer">{{Answer}}</div>',
        },
    ],
    css="""
.card {
    font-family: Arial, sans-serif;
    font-size: 18px;
    line-height: 1.5;
    color: #333;
    background-color: #fff;
    padding: 20px;
}

.question {
    margin-bottom: 20px;
    border: 2px solid #e0e0e0;
    padding: 15px;
    border-radius: 8px;
    background-color: #f9f9f9;
}

.answer {
    margin-top: 20px;
    padding: 15px;
    border: 2px solid #4CAF50;
    border-radius: 8px;
    background-color: #f0f8f0;
}

hr {
    border: none;
    height: 2px;
    background-color: #4CAF50;
    margin: 20px 0;
}
    """
)

# Create the deck
az_104_deck = genanki.Deck(
    2059400112,  # Different deck ID
    'AZ-104 Critical Priorities (Clean Format)'
)

# Read the CSV and create notes
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Build the complete question with choices
        question_text = row['Question']
        choice_a = row['ChoiceA']
        choice_b = row['ChoiceB']
        choice_c = row['ChoiceC']
        choice_d = row['ChoiceD']
        correct = row['Correct']
        explanation = row['Explanation']
        tags = row['Tags']
        
        # Question field (what shows on front)
        full_question = f"""{question_text}

<b>A)</b> {choice_a}
<b>B)</b> {choice_b}
<b>C)</b> {choice_c}
<b>D)</b> {choice_d}"""
        
        # Answer field (what shows on back after clicking)
        answer = f"<b>Correct Answer: {correct}</b><br><br>{explanation}"
        
        # Create note
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, answer, tags]
        )
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Clean-Format.apkg')

print("✅ Successfully created AZ-104-Clean-Format.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Clean format with proper question/answer separation!")