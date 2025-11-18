#!/usr/bin/env python3

import genanki
import random

# Use the exact same model structure as standard Anki decks
# This matches what most successful Anki decks use
model_id = random.randrange(1 << 30, 1 << 31)
deck_id = random.randrange(1 << 30, 1 << 31)

my_model = genanki.Model(
    model_id,
    'Simple Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
        },
    ])

my_deck = genanki.Deck(
    deck_id,
    'AZ-104 Critical Priorities Study Deck')

# Create very simple cards without any complex formatting
my_deck.add_note(genanki.Note(
    model=my_model,
    fields=['What are the EXACT steps to configure auto-swap for Azure App Service deployment slots?\n\nA) Create slot → Enable auto-swap → Configure warm-up → Test\nB) Configure warm-up → Create slot → Enable auto-swap → Deploy\nC) Create slot → Deploy → Enable auto-swap → Configure warm-up\nD) Enable auto-swap → Create slot → Configure warm-up → Deploy', 
            'ANSWER: A\n\nA) Create slot → Enable auto-swap → Configure warm-up → Test\n\nCorrect sequence:\n1. Create deployment slot (staging)\n2. Enable Auto-Swap during slot creation\n3. Configure automatic warm-up process\n4. Test zero-downtime deployment']))

my_deck.add_note(genanki.Note(
    model=my_model,
    fields=['You need to securely connect an App Service to Azure SQL Database. What is the CORRECT sequence?\n\nA) Service Endpoint → VNet Integration → Firewall Rules → Disable Public Access → Test\nB) VNet Integration → Service Endpoint → Firewall Rules → Disable Public Access → Test\nC) Firewall Rules → VNet Integration → Service Endpoint → Disable Public Access → Test\nD) Disable Public Access → VNet Integration → Service Endpoint → Firewall Rules → Test', 
            'ANSWER: B\n\nB) VNet Integration → Service Endpoint → Firewall Rules → Disable Public Access → Test\n\nSequence:\n- VNet Integration: Connect App Service to VNet subnet FIRST\n- Service Endpoint: Enable Microsoft.Sql service endpoint\n- Firewall Rules: Update SQL Database firewall rules\n- Disable Public Access: Turn off public internet access\n- Test: Verify connection']))

my_deck.add_note(genanki.Note(
    model=my_model,
    fields=['What is Azure Container Instances (ACI) scaling limitation?\n\nA) ACI supports horizontal auto-scaling like AKS\nB) ACI requires manual scaling by updating container specifications\nC) ACI has no scaling support - containers are fixed size\nD) ACI requires delete/redeploy for scaling changes', 
            'ANSWER: D\n\nD) ACI requires delete/redeploy for scaling changes\n\nACI has NO in-place auto-scaling support\n\nScaling Process:\n1. Delete existing container group\n2. Modify deployment template\n3. Redeploy container group\n\nAKS has in-place auto-scaling with zero downtime']))

my_deck.add_note(genanki.Note(
    model=my_model,
    fields=['What are Container Apps ingress configuration options?\n\nA) Public, Private, Internal, Disabled\nB) External, Internal, Disabled\nC) Internet, VNet, Private, None\nD) Public, VNet-only, Private, Background', 
            'ANSWER: B\n\nB) External, Internal, Disabled\n\nExternal Ingress: Internet traffic, public FQDN\nInternal Ingress: VNet-only access, no internet\nDisabled: No HTTP ingress, for background jobs']))

my_deck.add_note(genanki.Note(
    model=my_model,
    fields=['What is the difference between Fault Domains and Update Domains?\n\nA) Fault Domains = power/network failure protection, Update Domains = planned maintenance isolation\nB) Fault Domains = planned maintenance isolation, Update Domains = power/network failure protection\nC) Both provide the same protection\nD) Fault Domains are for VMs, Update Domains are for containers', 
            'ANSWER: A\n\nA) Fault Domains = power/network failure protection, Update Domains = planned maintenance isolation\n\nFault Domains: Protection against unplanned hardware failures\nUpdate Domains: Protection during planned maintenance\n\nFD = unplanned failures, UD = planned maintenance']))

my_deck.add_note(genanki.Note(
    model=my_model,
    fields=['What are the differences between VMSS Orchestration Modes?\n\nA) Uniform = identical VMs, Flexible = mixed VM sizes and types\nB) Uniform = automatic scaling, Flexible = manual scaling\nC) Uniform = single VM type, Flexible = multiple availability zones\nD) No difference - both modes work identically', 
            'ANSWER: A\n\nA) Uniform = identical VMs, Flexible = mixed VM sizes and types\n\nUniform: All VMs identical (same size, image, config)\nFlexible: Mix different VM sizes and types in same scale set\n\nUniform for identical workloads, Flexible for mixed requirements']))

genanki.Package(my_deck).write_to_file('AZ-104-Critical-Priorities-Study-Deck.apkg')

print("Created AZ-104-Critical-Priorities-Study-Deck.apkg with basic format")
print("This should work exactly like any standard Anki deck")