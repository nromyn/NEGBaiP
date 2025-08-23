import os
from PIL import Image, ImageFilter
import pytesseract
from pillow_heif import register_heif_opener
from tqdm import tqdm # Import the tqdm library

# Register the HEIF opener to allow Pillow to process HEIC files
register_heif_opener()

def preprocess_image(image_path):
    """
    Applies several image processing steps to improve OCR accuracy.
    """
    img = Image.open(image_path).convert('RGB')
    img = img.convert('L') # Convert to grayscale
    img = img.filter(ImageFilter.SHARPEN) # Sharpen the image
    return img

def perform_ocr_on_folder_advanced(folder_path):
    """
    Performs advanced OCR with image preprocessing and configuration.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: The provided path '{folder_path}' is not a valid directory.")
        return

    tess_config = r'--psm 3'
    
    # Get a list of all HEIC, JPG, and PNG files to process
    file_list = [f for f in os.listdir(folder_path) if f.lower().endswith(('.heic', '.jpg', '.png'))]
    
    # Wrap the list with tqdm to display a progress bar
    for filename in tqdm(file_list, desc="Processing images"):
        input_file_path = os.path.join(folder_path, filename)
        
        try:
            preprocessed_img = preprocess_image(input_file_path)
            text = pytesseract.image_to_string(preprocessed_img, config=tess_config)

            output_filename = os.path.splitext(filename)[0] + '.md'
            output_file_path = os.path.join(folder_path, output_filename)
            
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(f"# OCR Result for {filename}\n\n")
                f.write(text)

        except Exception as e:
            tqdm.write(f"Error processing '{input_file_path}': {e}")
            
    print("OCR process completed.")
                
# --- Script Execution ---
if __name__ == "__main__":
    folder_path = r"C:\Users\nicho\OneDrive - Romyn's AAD\CampbellBook\Scans"
    perform_ocr_on_folder_advanced(folder_path)