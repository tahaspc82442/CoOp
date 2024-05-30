from PIL import Image
import os

def analyze_tif_image(image_path):
    try:
        # Open the .tif image
        with Image.open(image_path) as img:
            # Print basic details
            print(f"Filename: {os.path.basename(image_path)}")
            print(f"Format: {img.format}")
            print(f"Mode: {img.mode}")
            print(f"Size (Width x Height): {img.size}")
            print(f"Number of Frames: {img.n_frames}")

            # Determine the number of channels
            mode_to_channels = {
                "1": 1,      # (1-bit pixels, black and white, stored with one pixel per byte)
                "L": 1,      # (8-bit pixels, black and white)
                "P": 1,      # (8-bit pixels, mapped to any other mode using a color palette)
                "RGB": 3,    # (3x8-bit pixels, true color)
                "RGBA": 4,   # (4x8-bit pixels, true color with transparency mask)
                "CMYK": 4,   # (4x8-bit pixels, color separation)
                "YCbCr": 3,  # (3x8-bit pixels, color video format)
                "I": 1,      # (32-bit signed integer pixels)
                "F": 1       # (32-bit floating point pixels)
            }

            number_of_channels = mode_to_channels.get(img.mode, "Unknown")
            print(f"Number of Channels: {number_of_channels}")

            # Print details for each frame if it is a multi-frame image
            if img.n_frames > 1:
                for i in range(img.n_frames):
                    img.seek(i)
                    print(f"Frame {i+1}: Size (Width x Height) - {img.size}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
image_path = '/raid/biplab/taha/Ucmerced/Images/airplane/airplane00.tif'
analyze_tif_image(image_path)
