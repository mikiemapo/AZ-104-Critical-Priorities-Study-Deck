#!/usr/bin/env python3
"""
Convert Microsoft Entra ID Cheat Sheet to MCQ format and append to Master Questions CSV
"""

import csv
import random

# Read the cheat sheet
input_file = 'Personalized-Review-Decks/Microsoft_Entra_ID_Cheat_Sheet.csv'
output_file = 'AZ-104-Master-Questions.csv'

new_questions = []

with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        question_text = row['Question']
        correct_answer = row['Answer']
        tags = row['Tags']
        source = row['Source']
        
        # Generate 3 plausible wrong answers based on the question type
        wrong_answers = []
        
        # License questions
        if 'license' in question_text.lower():
            wrong_answers = [
                "Enterprise Mobility + Security E3",
                "Microsoft 365 Business Basic",
                "Azure Active Directory External Identities"
            ]
        # B2B/B2C questions
        elif 'B2B' in question_text or 'B2C' in question_text:
            wrong_answers = [
                "Azure AD Connect for hybrid sync",
                "Microsoft Entra Domain Services",
                "External collaboration policies"
            ]
        # Authentication questions
        elif 'authentication' in question_text.lower() or 'SSPR' in question_text or 'MFA' in question_text:
            wrong_answers = [
                "Conditional Access, Azure AD Connect, Privileged Identity Management",
                "Password hash sync, Pass-through authentication, Federation",
                "Azure AD Application Proxy, Identity Protection, Access Reviews"
            ]
        # Device join questions
        elif 'join' in question_text.lower() or 'device' in question_text.lower():
            wrong_answers = [
                "Hybrid Azure AD registered, Cloud-only joined, On-premises registered",
                "Domain-joined, Workgroup-joined, Azure AD connected",
                "Intune enrolled, MDM managed, Azure AD synced"
            ]
        # Role questions
        elif 'role' in question_text.lower() or 'RBAC' in question_text.lower():
            wrong_answers = [
                "Owner, Contributor, Reader, Custom Role",
                "Global Reader, Security Operator, Compliance Administrator",
                "Application Administrator, Cloud Application Administrator, User Administrator"
            ]
        # Security questions
        elif 'security' in question_text.lower() or 'Identity Protection' in question_text:
            wrong_answers = [
                "Security Center, Defender for Cloud, Sentinel",
                "Azure Firewall, DDoS Protection, Web Application Firewall",
                "Key Vault, Managed Identities, Service Principals"
            ]
        # Default wrong answers
        else:
            wrong_answers = [
                "Azure AD Connect sync services",
                "Microsoft Entra Permissions Management",
                "Azure AD B2B Direct Federation"
            ]
        
        # Randomize answer positions
        all_answers = [correct_answer] + wrong_answers[:3]
        random.shuffle(all_answers)
        
        correct_letter = chr(65 + all_answers.index(correct_answer))  # A, B, C, or D
        
        # Create explanation
        explanation = f"<strong>Correct Answer: {correct_letter}) {correct_answer}</strong><br><br>"
        explanation += f"<strong>Key Concept:</strong> {question_text.replace('What', 'Understanding what')}<br><br>"
        explanation += f"<strong>Source:</strong> {source}"
        
        # Build the MCQ row
        mcq_row = {
            'Question': question_text,
            'ChoiceA': all_answers[0],
            'ChoiceB': all_answers[1],
            'ChoiceC': all_answers[2],
            'ChoiceD': all_answers[3],
            'Correct': correct_letter,
            'Explanation': explanation,
            'Tags': tags + ',Identities,Governance',
            'Source': source,
            'Batch': 'Identities & Governance - Entra ID'
        }
        
        new_questions.append(mcq_row)

# Append to master CSV
with open(output_file, 'a', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=[
        'Question', 'ChoiceA', 'ChoiceB', 'ChoiceC', 'ChoiceD', 
        'Correct', 'Explanation', 'Tags', 'Source', 'Batch'
    ])
    
    for row in new_questions:
        writer.writerow(row)

print(f"✅ Added {len(new_questions)} Entra ID questions to {output_file}")
print(f"📚 Batch name: Identities & Governance - Entra ID")
