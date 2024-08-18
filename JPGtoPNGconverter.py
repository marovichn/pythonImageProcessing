import sys
import os
from PIL import Image

# grabbing arguments

arguments = sys.argv
fromFolder = arguments[1]
toFolder = arguments[2]
print(arguments)

# check if new/ exits

if not os.path.exists(toFolder):
    os.makedirs(toFolder)
    print(f"Created folder: {toFolder}")
else:
    print(f"Folder {toFolder} already exists")

for filename in os.listdir(fromFolder):
    if filename.endswith((".jpg", ".jpeg", ".bmp", ".gif")):  # Check for supported image formats
        img_path = os.path.join(fromFolder, filename)
        img = Image.open(img_path)

        # Convert to PNG format
        png_filename = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(toFolder, png_filename)

        # Save the image as PNG in the toFolder
        img.save(png_path, "PNG")
        print(f"Converted {filename} to {png_filename} and saved to {toFolder}")