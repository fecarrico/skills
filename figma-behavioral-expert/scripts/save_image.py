import base64
import sys
import os

def save_base64_image(base64_string, output_path):
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Remove data URI prefix if present
    if "," in base64_string:
        base64_string = base64_string.split(",")[1]
    
    try:
        image_data = base64.b64decode(base64_string)
        with open(output_path, "wb") as f:
            f.write(image_data)
        print(f"Success: Image saved to {output_path}")
    except Exception as e:
        print(f"Error: Failed to save image. {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 save_image.py <base64_string> <output_path>")
        sys.exit(1)
    
    base64_val = sys.argv[1]
    path_val = sys.argv[2]
    save_base64_image(base64_val, path_val)
