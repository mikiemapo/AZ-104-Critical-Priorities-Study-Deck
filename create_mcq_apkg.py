#!/usr/bin/env python3

import genanki
import csv

# Create a simple, clean model that works like standard Anki decks - EXACTLY like create_simple_apkg.py
az_104_model = genanki.Model(
    1607392321,  # New Model ID
    'Basic',
    fields=[
        {'name': 'Front'},
        {'name': 'Back'}
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Front}}',
            'afmt': '{{FrontSide}}\n\n<hr id="answer">\n\n{{Back}}',
        },
    ]
)

# Create the deck
az_104_deck = genanki.Deck(
    2059400112,  # New Deck ID
    'AZ-104 Critical Priorities Study Deck'
)

# RESTORE EXACT WORKING FORMAT - Simple multiple choice questions without complex formatting
questions_data = [
    {
        "front": "What are the EXACT steps to configure auto-swap for Azure App Service deployment slots?\n\nA) Create slot → Enable auto-swap → Configure warm-up → Test\nB) Configure warm-up → Create slot → Enable auto-swap → Deploy\nC) Create slot → Deploy → Enable auto-swap → Configure warm-up\nD) Enable auto-swap → Create slot → Configure warm-up → Deploy",
        "back": "Correct Answer: A\n\nA) Create slot → Enable auto-swap → Configure warm-up → Test\n\nThe correct sequence is:\n1. Create deployment slot (staging)\n2. Enable Auto-Swap during slot creation OR in deployment settings\n3. Configure automatic warm-up process before swap\n4. Test to ensure zero-downtime deployment works\n\nThis ensures proper integration with CI/CD pipelines and fail-safe rollback capabilities."
    },
    {
        "front": "You need to securely connect an App Service to Azure SQL Database. What is the CORRECT sequence?\n\nA) Service Endpoint → VNet Integration → Firewall Rules → Disable Public Access → Test\nB) VNet Integration → Service Endpoint → Firewall Rules → Disable Public Access → Test\nC) Firewall Rules → VNet Integration → Service Endpoint → Disable Public Access → Test\nD) Disable Public Access → VNet Integration → Service Endpoint → Firewall Rules → Test",
        "back": "Correct Answer: B\n\nB) VNet Integration → Service Endpoint → Firewall Rules → Disable Public Access → Test\n\nThe sequence is:\n- VNet Integration: Connect App Service to VNet subnet FIRST\n- Service Endpoint: Enable Microsoft.Sql service endpoint\n- Firewall Rules: Update SQL Database firewall rules\n- Disable Public Access: Turn off public internet access\n- Test: Verify end-to-end secure connection\n\nCRITICAL: Must establish VNet integration and service endpoints BEFORE disabling public access."
    },
    {
        "front": "What is Azure Container Instances (ACI) scaling limitation compared to AKS?\n\nA) ACI supports horizontal auto-scaling like AKS\nB) ACI requires manual scaling by updating container specifications\nC) ACI has no scaling support - containers are fixed size\nD) ACI requires delete/redeploy for scaling changes",
        "back": "Correct Answer: D\n\nD) ACI requires delete/redeploy for scaling changes\n\nACI Fundamental Limitation: NO in-place auto-scaling support\n\nACI Scaling Process:\n1. Delete existing container group (az container delete)\n2. Modify deployment template with new specs (CPU, memory, container count)\n3. Redeploy container group (az container create)\n\nvs AKS: In-place Horizontal Pod Autoscaler (HPA) with zero downtime\n\nChoose AKS for production workloads requiring auto-scaling."
    },
    {
        "front": "What are the different Container Apps ingress configuration options?\n\nA) Public, Private, Internal, Disabled\nB) External, Internal, Disabled\nC) Internet, VNet, Private, None\nD) Public, VNet-only, Private, Background",
        "back": "Correct Answer: B\n\nB) External, Internal, Disabled\n\nExternal Ingress:\n• Exposes app to internet traffic\n• Provides public FQDN\n• Use for: Public-facing APIs, web applications\n\nInternal Ingress:\n• VNet-only access - no internet exposure\n• Private connectivity within Container Apps Environment\n• Use for: Internal microservices, backend APIs\n\nDisabled:\n• No HTTP ingress at all\n• Use for: Background jobs, queue processors"
    },
    {
        "front": "What is the correct difference between Fault Domains and Update Domains?\n\nA) Fault Domains = power/network failure protection, Update Domains = planned maintenance isolation\nB) Fault Domains = planned maintenance isolation, Update Domains = power/network failure protection\nC) Both provide the same protection against different types of failures\nD) Fault Domains are for VMs, Update Domains are for containers",
        "back": "Correct Answer: A\n\nA) Fault Domains = power/network failure protection, Update Domains = planned maintenance isolation\n\nFault Domains (FD):\n• Protection against unplanned hardware failures\n• Separate power source and network switch\n• Azure automatically distributes VMs across fault domains\n\nUpdate Domains (UD):\n• Protection during planned maintenance/updates\n• Only one update domain rebooted at a time\n• Ensures service availability during Azure maintenance\n\nKey: FD = unplanned failures, UD = planned maintenance"
    },
    {
        "front": "What are the differences between VMSS Orchestration Modes?\n\nA) Uniform = identical VMs, Flexible = mixed VM sizes and types\nB) Uniform = automatic scaling, Flexible = manual scaling\nC) Uniform = single VM type, Flexible = multiple availability zones\nD) No difference - both modes work identically",
        "back": "Correct Answer: A\n\nA) Uniform = identical VMs, Flexible = mixed VM sizes and types\n\nUniform Orchestration Mode:\n• All VMs must be identical (same size, image, configuration)\n• Built for true scale sets with identical workloads\n• Traditional VMSS behavior\n\nFlexible Orchestration Mode:\n• Mix different VM sizes and types in same scale set\n• Better for heterogeneous workloads\n• More flexibility in VM configuration\n• Can manage existing VMs\n\nChoose Uniform for identical workloads, Flexible for mixed requirements."
    }
]

# Create notes - EXACT WORKING FORMAT
for item in questions_data:
    note = genanki.Note(
        model=az_104_model,
        fields=[item["front"], item["back"]]
    )
    az_104_deck.add_note(note)

# Generate the package
genanki.Package(az_104_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("✅ Successfully created AZ-104-Critical-Priorities-Study-Deck.apkg")
print(f"📊 Deck contains {len(az_104_deck.notes)} cards")
print("🎯 Simple format - should display correctly in Anki!")