import json
import subprocess
import time

input_file = '/home/fecarrico/.gemini/antigravity/brain/d69b6c6e-c34e-4ca3-aff7-409efe9275d7/.system_generated/steps/169/output.txt'

def get_all_ids():
    with open(input_file, 'r') as f:
        lines = f.readlines()
    ids = []
    for line in lines:
        if '"id":' in line:
            node_id = line.split('"id":')[1].split('"')[1]
            ids.append(node_id)
    return ids

all_ids = get_all_ids()
print(f"Total IDs to scan: {len(all_ids)}")

# Since I can't call MCP from here easily without a tool, 
# I will just extract the first 200 IDs and suggest scanning them.
# Or better, I'll use the scan_nodes_by_types result which already exists.
