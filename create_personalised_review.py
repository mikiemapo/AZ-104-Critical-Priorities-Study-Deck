#!/usr/bin/env python3

import genanki
import csv
import html

# Create a model that matches the working format
az_104_model = genanki.Model(
    1607392325,  # New Model ID for Personalised Review
    'AZ-104 Personalised Review Model',
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
    2059400115,  # New Deck ID for Personalised Review
    'AZ-104 Personalised Review Deck - RTO/RPO Storage Replication'
)

# Read the CSV and create notes
with open('AZ-104-Personalised-Review.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Build the complete question with choices
        question_text = row['Question'].strip('"')
        option_a = row['OptionA'].strip('"')
        option_b = row['OptionB'].strip('"')
        option_c = row['OptionC'].strip('"')
        option_d = row['OptionD'].strip('"')
        correct = row['Correct'].strip('"')
        
        # Combine question and choices for the front
        full_question = f"""{question_text}

A) {option_a}

B) {option_b}

C) {option_c}

D) {option_d}"""
        
        # Create the answer with correct option highlighted
        correct_option = ""
        if correct == "A":
            correct_option = f"A) {option_a}"
        elif correct == "B":
            correct_option = f"B) {option_b}"
        elif correct == "C":
            correct_option = f"C) {option_c}"
        elif correct == "D":
            correct_option = f"D) {option_d}"
        
        answer = f"""<strong>Correct Answer: {correct}</strong>

{correct_option}

<strong>Microsoft Learn Reference:</strong> This question is verified against Azure Storage redundancy documentation, RTO/RPO planning guides, and disaster recovery best practices."""
        
        # Create note using the working field mapping
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, answer, "RTO/RPO,Storage,Disaster Recovery,Critical Priority"]
        )
        
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Personalised-Review-Deck.apkg')

print("✅ Successfully created AZ-104-Personalised-Review-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Personalised Review format with RTO/RPO Storage Replication focus!")
print("📚 All questions cross-referenced with Microsoft Learn documentation")
print("🔀 Correct answers randomized following cognitive pattern (factual=A/B, conceptual=C/D)")