import os
from PIL import Image

def convert_tif_to_jpg(src_folder, dst_folder):
    for root, _, files in os.walk(src_folder):
        for file in files:
            if file.lower().endswith('.tif'):
                # Full path of the source .tif file
                src_file_path = os.path.join(root, file)
                
                # Create corresponding destination directory
                relative_path = os.path.relpath(root, src_folder)
                dst_dir_path = os.path.join(dst_folder, relative_path)
                os.makedirs(dst_dir_path, exist_ok=True)
                
                # Full path of the destination .jpg file
                dst_file_name = os.path.splitext(file)[0] + '.jpg'
                dst_file_path = os.path.join(dst_dir_path, dst_file_name)
                
                # Convert and save the .tif image as .jpg
                with Image.open(src_file_path) as img:
                    img = img.convert("RGB")
                    img.save(dst_file_path, "JPEG")
                
                print(f"Converted: {src_file_path} to {dst_file_path}")

# Example usage
src_folder = '/raid/biplab/taha/Ucmerced/Images'
dst_folder = '/raid/biplab/taha/imagesjpeg'

convert_tif_to_jpg(src_folder, dst_folder)
