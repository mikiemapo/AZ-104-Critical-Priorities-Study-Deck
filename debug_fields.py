#!/usr/bin/env python3

import csv

# Read the CSV and debug what's happening with fields
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for i, row in enumerate(csv_reader):
        if i >= 2:  # Just check first 2 cards
            break
            
        print(f"\n=== Card {i+1} Debug ===")
        print(f"Question: {row['Question'][:50]}...")
        print(f"ChoiceA: '{row['ChoiceA']}'")
        print(f"ChoiceB: '{row['ChoiceB']}'")
        print(f"ChoiceC: '{row['ChoiceC']}'")
        print(f"ChoiceD: '{row['ChoiceD']}'")
        print(f"Correct: '{row['Correct']}'")
        
        # Clean the fields like in the main script
        choice_a = row['ChoiceA'].strip('"')
        choice_b = row['ChoiceB'].strip('"')
        choice_c = row['ChoiceC'].strip('"')
        choice_d = row['ChoiceD'].strip('"')
        
        print(f"After cleaning:")
        print(f"ChoiceA: '{choice_a}'")
        print(f"ChoiceB: '{choice_b}'")
        print(f"ChoiceC: '{choice_c}'")
        print(f"ChoiceD: '{choice_d}'")