import json
import os

input_file = '/home/fecarrico/.gemini/antigravity/brain/d69b6c6e-c34e-4ca3-aff7-409efe9275d7/.system_generated/steps/91/output.txt'
output_file = '/tmp/figma_full_scan.json'

def scan_node(node, path=""):
    results = []
    name = node.get('name', 'Unnamed')
    node_type = node.get('type', 'UNKNOWN')
    node_id = node.get('id', '??')
    
    current_path = f"{path} > {name}[{node_type}]" if path else f"{name}[{node_type}]"
    
    if node_type == 'TEXT':
        results.append({
            'id': node_id,
            'text': node.get('characters', ''),
            'path': current_path,
            'type': node_type
        })
    
    if 'children' in node:
        for child in node['children']:
            results.extend(scan_node(child, current_path))
            
    return results

try:
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    full_scan = scan_node(data)
    
    with open(output_file, 'w') as f:
        json.dump(full_scan, f, indent=2)
        
    print(f"Deep scan complete. Found {len(full_scan)} text nodes.")
except Exception as e:
    print(f"Error: {e}")
