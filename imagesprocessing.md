# Install Tesseract OCR
https://tesseract-ocr.github.io/tessdoc/Downloads.html

# Install pytesseract python wrapper and pillow_heif

```python
pip install Pillow pytesseract pillow_heif
```


```python
# Re-import necessary libraries
from PIL import Image
import pytesseract
import pillow_heif # Import the HEIF plugin
from pillow_heif import register_heif_opener # Import the registration function

# Register the HEIF opener so Pillow can handle .heic files
register_heif_opener()

# Define the image paths (assuming actual .heic files)
# Make sure these paths point to your actual HEIC files on your system.
image_paths = [
    "/mnt/data/IMG_4255 2023-10-17 12_40_38.heic",
    "/mnt/data/IMG_4254 2023-10-17 12_40_37.heic",
    "/mnt/data/IMG_4253 2023-10-17 12_40_37.heic"
]

# Run OCR and collect results
ocr_results = {}
for path in image_paths:
    try:
        # Image.open will now handle .heic files due to the registration
        img = Image.open(path)
        text = pytesseract.image_to_string(img)
        ocr_results[path] = text
        print(f"OCR successful for {path}")
    except Exception as e:
        print(f"Error processing {path}: {e}")

print("\n--- OCR Results ---")
for path, text in ocr_results.items():
    print(f"File: {path}\nContent:\n{text}\n{'-'*30}")
```
