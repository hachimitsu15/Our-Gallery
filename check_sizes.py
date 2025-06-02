from PIL import Image
import os

folder_path = r"C:\Users\Eric Xavier\Documents\Our_Website\images"

def print_image_sizes(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
                img_path = os.path.join(root, file)
                print(f"Checking: {img_path}")
                try:
                    with Image.open(img_path) as img:
                        print(f"   Size: {img.size}")
                except Exception as e:
                    print(f"   Error: {e}")

print_image_sizes(folder_path)