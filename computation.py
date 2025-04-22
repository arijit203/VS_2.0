import cv2
import numpy as np

def calculate_black_pixel_percentage(image_path):
    # Load the binary image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Threshold to ensure it's a binary image (0 for black, 255 for white)
    _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    
    # Count the black pixels (0 values in the binary image)
    black_pixels = np.sum(binary_img == 0)
    
    # Count the total number of pixels
    total_pixels = binary_img.size
    
    # Calculate the percentage of black pixels
    black_percentage = (black_pixels / total_pixels) * 100
    
    return black_percentage

# Usage example
image_path = 'Input.png'  # Replace with your binary image path
black_percentage = calculate_black_pixel_percentage(image_path)
print(f"The % of black pixels in original image is: {black_percentage}%")
print(f"The % of black pixels in reconstructed image is: {calculate_black_pixel_percentage("reconstructed.png")}%")
