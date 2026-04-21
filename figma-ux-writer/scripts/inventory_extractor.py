import json
import os

with open('/home/fecarrico/.gemini/antigravity/brain/d69b6c6e-c34e-4ca3-aff7-409efe9275d7/.system_generated/steps/91/output.txt', 'r') as f:
    data = json.load(f)

inventory = []

def traverse(node):
    if node['type'] in ['SECTION', 'FRAME', 'COMPONENT', 'INSTANCE']:
        inventory.append({
            'id': node['id'],
            'name': node.get('name', 'Unnamed'),
            'type': node['type']
        })
    if 'children' in node:
        for child in node['children']:
            traverse(child)

traverse(data)

with open('/tmp/figma_audit_inventory.json', 'w') as f:
    json.dump(inventory, f, indent=2)

print(f"Inventory saved with {len(inventory)} items.")
