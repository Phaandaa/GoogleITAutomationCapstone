#!/usr/bin/env python3
import os
from PIL import Image
folder_path = "./supplier-data/images"
output_path = "./supplier-data/images"

new_width, new_height = 600, 400
new_format = "JPEG"
def process_images_in_folder(folder_path):
    file_list = os.listdir(folder_path)
    print(file_list)
    for filename in file_list:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            file_path = os.path.join(folder_path, filename)
            print(f'changing {filename} in {file_path}')
            image = Image.open(file_path)
            if image.mode in ('LA', 'RGBA', 'P'):
                image = image.convert('RGB')
            resized_image = image.resize((new_width, new_height))
            output_filename = os.path.splitext(filename)[0] + "." + new_format.lower()
            output_file_path = os.path.join(output_path, output_filename)
            resized_image.save(output_file_path, format=new_format)
            print(f'image saved in {output_file_path}')
            image.close()

process_images_in_folder(folder_path)