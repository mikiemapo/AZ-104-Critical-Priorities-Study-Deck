#!/usr/bin/env python3

import genanki
import csv

# Create the exact model that worked before
az_104_model = genanki.Model(
    1607392320,  # Original Model ID
    'AZ-104 Multiple Choice Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'Explanation'},
        {'name': 'Tags'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{Question}}<hr id="answer"><div style="background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; margin: 10px 0;">{{Explanation}}</div>',
        },
    ],
    css="""
.card {
    font-family: Arial, sans-serif;
    font-size: 18px;
    line-height: 1.6;
    color: black;
    background-color: white;
    padding: 20px;
}

.choice {
    background-color: white;
    border: 2px solid #ddd;
    padding: 10px 15px;
    margin: 8px 0;
    border-radius: 6px;
    display: block;
}

.choice.correct {
    background-color: #4CAF50 !important;
    color: white !important;
    border-color: #45a049 !important;
    font-weight: bold;
}

#answer {
    border: 2px solid #4CAF50;
    margin: 20px 0;
}
    """
)

# Create the deck
az_104_deck = genanki.Deck(
    2059400111,  # Original Deck ID
    'AZ-104 Critical Priorities Study Deck'
)

# Read the CSV and create notes using the WORKING format - embed choices in question text
with open('AZ-104-Connor-Format.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # Build the complete question with choices embedded (this was the working format!)
        question_text = row['Question']
        choice_a = row['ChoiceA']
        choice_b = row['ChoiceB']
        choice_c = row['ChoiceC']
        choice_d = row['ChoiceD']
        correct = row['Correct']
        explanation = row['Explanation']
        tags = row['Tags']
        
        # Create question with white rectangles, correct answer will turn green
        correct_letter = correct.strip()
        choice_a_class = "choice correct" if correct_letter == "A" else "choice"
        choice_b_class = "choice correct" if correct_letter == "B" else "choice"
        choice_c_class = "choice correct" if correct_letter == "C" else "choice"
        choice_d_class = "choice correct" if correct_letter == "D" else "choice"
        
        full_question = f"""{question_text}<br><br><div class="{choice_a_class}">A) {choice_a}</div><div class="{choice_b_class}">B) {choice_b}</div><div class="{choice_c_class}">C) {choice_c}</div><div class="{choice_d_class}">D) {choice_d}</div>"""
        
        # Create SHORT 2-sentence explanations
        if 'auto-swap' in question_text.lower():
            summary = "Create deployment slot first, then configure warm-up settings. Enable auto-swap to automatically swap staging to production after successful deployment."
        elif 'VNet Integration' in explanation:
            summary = "Must establish VNet integration and service endpoints BEFORE disabling public access. This prevents connectivity loss during the security configuration."
        elif 'Three-Layer Security' in explanation:
            summary = "Combine Microsoft Defender for vulnerability scanning with ACR Tasks for CI/CD automation. Add Azure Policy to enforce security compliance and block vulnerable images."
        elif 'ACI' in explanation and 'scaling' in explanation:
            summary = "ACI has no in-place auto-scaling capability like AKS. You must delete and redeploy the container group with new resource specifications."
        elif 'Container Apps' in explanation:
            summary = "External ingress provides internet access with public FQDN. Internal ingress restricts access to VNet only, while disabled is for background jobs."
        elif 'fault domain' in explanation.lower():
            summary = "Fault domains separate VMs across different physical hardware racks. This provides protection against hardware failures within the same data center."
        elif 'availability' in explanation.lower() and 'zone' in explanation.lower():
            summary = "Availability zones are physically separate data centers within the same region. They provide protection against data center-level failures."
        elif 'VMSS' in explanation:
            summary = "Uniform scale sets manage identical VM instances for consistent workloads. Flexible scale sets support different VM sizes and mixed workload types."
        elif 'storage' in explanation.lower() and 'replication' in explanation.lower():
            summary = "GZRS provides the lowest RTO with zone-redundant storage plus geo-replication. It offers both local zone protection and cross-region disaster recovery."
        else:
            # Generic 2-sentence summary
            clean_text = explanation.replace('<strong>', '').replace('</strong>', '').replace('<br>', ' ')
            sentences = clean_text.split('. ')[:2]
            summary = '. '.join(sentences) + '.' if len(sentences) >= 2 else sentences[0]
        
        # Create note using Question/Answer/Explanation/Tags fields
        note = genanki.Note(
            model=az_104_model,
            fields=[full_question, correct, summary, tags]
        )
        az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 RESTORED working format - choices embedded in question text!")