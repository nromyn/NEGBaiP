# Install Tesseract OCR
https://tesseract-ocr.github.io/tessdoc/Downloads.html

# Install pytesseract python wrapper and pillow_heif

```python
pip install Pillow pytesseract pillow_heif
```


```python
import os
from PIL import Image
import pytesseract
from pillow_heif import register_heif_opener

# Register the HEIF opener to allow Pillow to process HEIC files
register_heif_opener()

def perform_ocr_on_folder(folder_path):
    """
    Performs OCR on all HEIC files in a given folder and saves the
    extracted text to a Markdown file with the same name.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: The provided path '{folder_path}' is not a valid directory.")
        return

    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .heic extension
        if filename.lower().endswith('.heic'):
            input_file_path = os.path.join(folder_path, filename)

            # Define the output Markdown file path
            # Replaces the '.heic' extension with '.md'
            output_filename = os.path.splitext(filename)[0] + '.md'
            output_file_path = os.path.join(folder_path, output_filename)

            print(f"Processing '{input_file_path}'...")
            
            try:
                # Open the HEIC image and perform OCR
                img = Image.open(input_file_path)
                text = pytesseract.image_to_string(img)

                # Write the extracted text to the new Markdown file
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    # Optional: Add a title to the Markdown file
                    f.write(f"# OCR Result for {filename}\n\n")
                    f.write(text)

                print(f"Successfully saved OCR output to '{output_file_path}'")

            except Exception as e:
                print(f"Error processing '{input_file_path}': {e}")
                
# --- Script Execution ---
if __name__ == "__main__":
    # Specify the folder containing your HEIC files here
    # Example: folder_path = "/Users/yourusername/Documents/photos"
    folder_path = "/mnt/data/"
    perform_ocr_on_folder(folder_path)
```
