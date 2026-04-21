import json

input_file = '/home/fecarrico/.gemini/antigravity/brain/d69b6c6e-c34e-4ca3-aff7-409efe9275d7/.system_generated/steps/223/output.txt'

def find_screens(node, is_root=False):
    screens = []
    
    # Logic: If it's a Section or the Page, its children that are Frame/Component/Instance
    # are "Screens" (unless they are nested sections, handled recursively).
    
    if node['type'] in ['CANVAS', 'SECTION', 'PAGE']:
        if 'children' in node:
            for child in node['children']:
                if child['type'] in ['FRAME', 'COMPONENT', 'INSTANCE']:
                    # This is a candidate for a screen
                    screens.append({
                        'id': child['id'],
                        'name': child.get('name', 'Unnamed'),
                        'type': child['type'],
                        'parent_name': node.get('name', 'Document Root')
                    })
                elif child['type'] == 'SECTION':
                    # Recursive dive into nested section
                    screens.extend(find_screens(child))
    
    return screens

try:
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    all_screens = find_screens(data, is_root=True)
    
    print(f"Total 'Telas' encontradas (1º nível de seção/página): {len(all_screens)}\n")
    for s in all_screens:
        print(f"[{s['parent_name']}] -> {s['name']} ({s['id']})")

except Exception as e:
    print(f"Erro ao processar: {e}")
