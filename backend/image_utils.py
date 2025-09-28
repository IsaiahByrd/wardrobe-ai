import os
from PIL import Image

def find_image_file(base_name):
    """Find an image file with the given base name and any supported format"""
    supported_formats = ['jpeg', 'jpg', 'png', 'webp', 'bmp', 'tiff', 'gif']
    
    #print(os.listdir('.'))

    for fmt in supported_formats:
        filename = f"{base_name}.{fmt}"
        if os.path.exists(filename):
            return filename
    return None


def validate_and_preprocess_image(image_path, max_size=(1024, 1024), max_file_size_mb=5):
    """Validate and preprocess image to meet API requirements"""
    try:
        file_size_mb = os.path.getsize(image_path) / (1024 * 1024)
        print(f"Image {image_path}: {file_size_mb:.2f} MB")

        if file_size_mb > max_file_size_mb:
            print(f"Warning: {image_path} is {file_size_mb:.2f} MB, may be too large")

        image = Image.open(image_path)
        print(f"Image {image_path}: {image.size[0]}x{image.size[1]} pixels, mode: {image.mode}")

        if image.mode in ('RGBA', 'P', 'L'):
            print(f"Converting {image_path} from {image.mode} to RGB")
            image = image.convert('RGB')

        if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
            print(f"Resizing {image_path} from {image.size} to fit within {max_size}")
            image.thumbnail(max_size, Image.Resampling.LANCZOS)

        return image
    except Exception as e:
        print(f"Error validating image {image_path}: {str(e)}")
        return None
