import json
import re

with open('/tmp/figma_full_scan.json', 'r') as f:
    data = json.load(f)

manual_rules = {
    'branding': r'(?i)Sem\s+parar(?! Parar)', # Case insensitive 'Sem parar' not followed by ' Parar'
    'colons': r':$', # Colon at the end
    'placeholder_repeat': None, # Manual check
}

violations = []

for node in data:
    text = node['text']
    node_id = node['id']
    path = node['path']
    
    # Rule 1: Branding
    if re.search(r'Sem\s+parar', text) and 'Sem Parar' not in text:
         violations.append({
             'id': node_id,
             'text': text,
             'issue': 'Branding Incorreto ("Sem Parar")',
             'suggestion': text.replace('Sem parar', 'Sem Parar').replace('Sem Parar', 'Sem Parar') # naive fix
         })
    
    # Rule 2: Colons in labels (simplified check: if it's short and has a colon)
    if len(text) < 30 and text.endswith(':'):
         violations.append({
             'id': node_id,
             'text': text,
             'issue': 'Pontuação (Dois pontos desnecessários em label)',
             'suggestion': text.rstrip(':')
         })

print(json.dumps(violations[:20], indent=2))
