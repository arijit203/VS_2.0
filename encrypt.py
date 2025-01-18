import cv2
import numpy as np
import random

def generate_all_pairs():
    """
    Generate all valid pairs of 3×3 grids for black and white pixels.
    """
    from itertools import product
    all_grids = [np.array(grid).reshape(3, 3) for grid in product([0, 1], repeat=9)]
    black_pairs = []
    white_pairs = []

    # Iterate through all possible pairs of grids
    for grid1 in all_grids:
        for grid2 in all_grids:
            overlap = np.logical_and(grid1, grid2).astype(int)
            black_count = np.sum(overlap == 0)
            white_count = np.sum(overlap == 1)

            # Check for black pixel condition
            if black_count >= 5 and np.array_equal(grid2, np.logical_not(grid1).astype(int)):
                black_pairs.append((grid1, grid2))

            # For white pixels, shares should be the same
            if white_count >= 5 and np.array_equal(grid1, grid2):
                white_pairs.append((grid1, grid2))


    return black_pairs, white_pairs


def generate_shares_with_pairs(image_path, output_share1_path, output_share2_path):
    # Generate valid pairs for black and white pixels
    black_pairs, white_pairs = generate_all_pairs()

    # Load the binary image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Get dimensions
    height, width = binary_img.shape

    # Initialize empty arrays for shares
    share1 = np.zeros((height * 3, width * 3), dtype=np.uint8)
    share2 = np.zeros((height * 3, width * 3), dtype=np.uint8)

    # Create the shares
    for i in range(height):
        for j in range(width):
            pixel = binary_img[i, j]  # 0 for black, 255 for white
            if pixel == 0:  # Black pixel
                chosen_pair = random.choice(black_pairs)
            else:  # White pixel
                chosen_pair = random.choice(white_pairs)

            # Fill in the shares with sub-pixels
            share1[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3] = chosen_pair[0] * 255
            share2[i * 3:(i + 1) * 3, j * 3:(j + 1) * 3] = chosen_pair[1] * 255

    # Save the shares as images
    cv2.imwrite(output_share1_path, share1)
    cv2.imwrite(output_share2_path, share2)
    print(f"Shares saved as {output_share1_path} and {output_share2_path}")


# Usage example
input_image_path = "./Input.png"  # Replace with your input file path
output_share1_path = "share1.png"
output_share2_path = "share2.png"

generate_shares_with_pairs(input_image_path, output_share1_path, output_share2_path)
