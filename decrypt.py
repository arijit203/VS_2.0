import cv2
import numpy as np

def decrypt_shares(share1_path, share2_path, output_path):
    # Load the shares
    share1 = cv2.imread(share1_path, cv2.IMREAD_GRAYSCALE)
    share2 = cv2.imread(share2_path, cv2.IMREAD_GRAYSCALE)

    # Ensure the dimensions match
    assert share1.shape == share2.shape, "Share dimensions do not match."

    # Overlay the shares to reconstruct the image
    reconstructed = np.logical_and(share1 > 0, share2 > 0).astype(np.uint8) * 255

    # Save the reconstructed image
    cv2.imwrite(output_path, reconstructed)
    print(f"Reconstructed image saved as {output_path}")

# Usage example
share1_path = "share1.png"  # Path to the first share
share2_path = "share2.png"  # Path to the second share
output_path = "reconstructed.png"  # Path to save the reconstructed image

decrypt_shares(share1_path, share2_path, output_path)
