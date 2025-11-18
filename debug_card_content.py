#!/usr/bin/env python3

import csv

print("=== DEBUGGING CARD CONTENT ===\n")

# Read the CSV and show what goes into each field
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for i, row in enumerate(csv_reader, 1):
        if i > 2:  # Just show first 2 cards
            break
            
        print(f"CARD {i}:")
        print("-" * 50)
        
        # Build the question field
        question_text = row['Question']
        choice_a = row['ChoiceA']
        choice_b = row['ChoiceB']
        choice_c = row['ChoiceC']
        choice_d = row['ChoiceD']
        
        full_question = f"""{question_text}

A) {choice_a}

B) {choice_b}

C) {choice_c}

D) {choice_d}"""
        
        # Build the answer field
        correct = row['Correct']
        explanation = row['Explanation']
        answer = f"Correct Answer: {correct}\n\n{explanation}"
        
        print("QUESTION FIELD (Front of card):")
        print(full_question)
        print("\n" + "="*30)
        print("ANSWER FIELD (Back of card):")
        print(answer)
        print("\n" + "="*50 + "\n")