import json

with open('/Users/felipe.carrico/.gemini/antigravity/brain/9fb46cd5-d91f-4a20-b295-cbba911dc251/.system_generated/steps/17/output.txt', 'r') as f:
    data = json.load(f)

for child in data.get('children', []):
    if child.get('visible', True) == False:
        continue
    if child.get('type') in ['FRAME', 'COMPONENT', 'INSTANCE']:
        print(f"Screen: {child['id']} - {child['name']} ({child['type']})")
