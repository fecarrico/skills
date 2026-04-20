import os
import zipfile
import argparse
import yaml

def package_skill(skill_path, output_dir=None):
    if not os.path.isdir(skill_path):
        print(f"Error: {skill_path} is not a directory.")
        return

    skill_file_path = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_file_path):
        print(f"Error: SKILL.md not found in {skill_path}")
        return

    # Try to get skill name from frontmatter
    skill_name = os.path.basename(skill_path)
    try:
        with open(skill_file_path, 'r') as f:
            content = f.read()
            if content.startswith('---'):
                parts = content.split('---')
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1])
                    if 'name' in metadata:
                        skill_name = metadata['name']
    except Exception as e:
        print(f"Warning: Could not parse SKILL.md frontmatter: {e}")

    output_name = f"{skill_name}.skill"
    if output_dir:
        output_path = os.path.join(output_dir, output_name)
    else:
        output_path = os.path.join(os.path.dirname(skill_path), output_name)

    print(f"Packaging skill '{skill_name}' to {output_path}...")

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, skill_path)
                zipf.write(file_path, arcname)

    print("Success!")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package an Antigravity skill.")
    parser.add_argument("skill_path", help="Path to the skill directory")
    parser.add_argument("--output", help="Output directory for the .skill file")
    args = parser.parse_args()
    package_skill(args.skill_path, args.output)
