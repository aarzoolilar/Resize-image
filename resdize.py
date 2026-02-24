import os
from PIL import Image

# Input and Output folders
input_folder = "images"
output_folder = "resized_images"

# Resize size
new_size = (300, 300)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(input_folder):
    try:
        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path)

        img = img.resize(new_size)

        # Convert to PNG
        new_name = os.path.splitext(file)[0] + ".png"
        save_path = os.path.join(output_folder, new_name)

        img.save(save_path)

        print(f"Processed: {file}")

    except Exception as e:
        print(f"Skipping {file}: {e}")