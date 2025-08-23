import os
from PIL import Image, ImageFilter
import pytesseract
from pillow_heif import register_heif_opener

# Register the HEIF opener to allow Pillow to process HEIC files
register_heif_opener()

def preprocess_image(image_path):
    """
    Applies several image processing steps to improve OCR accuracy.
    """
    # Open the image
    img = Image.open(image_path).convert('RGB')
    
    # Pre-processing steps
    img = img.convert('L') # Convert to grayscale
    img = img.filter(ImageFilter.SHARPEN) # Sharpen the image
    
    # You can also try thresholding
    # from PIL import ImageOps
    # img = ImageOps.invert(img) # Invert colors for dark text on light background
    # img = img.point(lambda p: 255 if p > 128 else 0) # Simple binary threshold
    
    return img

def perform_ocr_on_folder_advanced(folder_path):
    """
    Performs advanced OCR with image preprocessing and configuration.
    """
    if not os.path.isdir(folder_path):
        print(f"Error: The provided path '{folder_path}' is not a valid directory.")
        return

    # Tesseract configuration for single column text
    # You can change this based on your document layout
    # '--psm 6' for a single uniform block of text.
    # '--psm 3' for automatic page segmentation.
    tess_config = r'--psm 3'
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.heic', '.jpg', '.png')):
            input_file_path = os.path.join(folder_path, filename)
            
            try:
                # Preprocess the image
                preprocessed_img = preprocess_image(input_file_path)
                
                # Perform OCR with the specified configuration
                text = pytesseract.image_to_string(preprocessed_img, config=tess_config)

                # Save the extracted text to a Markdown file
                output_filename = os.path.splitext(filename)[0] + '.md'
                output_file_path = os.path.join(folder_path, output_filename)
                
                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(f"# OCR Result for {filename}\n\n")
                    f.write(text)

                print(f"Successfully processed '{filename}' and saved output to '{output_file_path}'")
                
            except Exception as e:
                print(f"Error processing '{input_file_path}': {e}")
                
# --- Script Execution ---
if __name__ == "__main__":
    folder_path = r"C:\Users\nicho\OneDrive - Romyn's AAD\CampbellBook\Scans"
    perform_ocr_on_folder_advanced(folder_path)
# --- 