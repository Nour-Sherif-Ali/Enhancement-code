import cv2
import numpy as np

# Step 1: Load the image
image_path = 'images/C04_png.rf.7ce5e5a7b63e5d471741970418f6bd67.jpg'
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Image file not found: {image_path}")

# Step 2: Convert the image to float32
image_float = image.astype(np.float32)

# Step 3: Normalize the image to the range [0, 1]
normalized_image = image_float / 255.0

# Alternatively, normalize to a specific mean and standard deviation
mean, std = np.mean(normalized_image), np.std(normalized_image)
normalized_image = (normalized_image - mean) / std

# Optional Step 4: Display the normalized image
cv2.imshow('Normalized Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 5: Save the normalized image if needed
output_path = 'normalize_image.jpg'
cv2.imwrite(output_path, (normalized_image * 255).astype(np.uint8))  # Scale back to [0, 255]
print(f"Normalized image saved as {output_path}")
