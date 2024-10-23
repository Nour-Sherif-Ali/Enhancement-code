import cv2
import matplotlib.pyplot as plt

# Reading the RGB file into Python environment
skI = cv2.imread('images/C01_png.rf.30b378eb272884b9d8b8a7605a8432b6.jpg')

# Convert the image from BGR to RGB (OpenCV loads images in BGR format)
skI = cv2.cvtColor(skI, cv2.COLOR_BGR2RGB)

# Display the original RGB im
betngaaan 
plt.subplot(1, 2, 1)
plt.imshow(skI)
plt.title("Original Image")
plt.axis('off')  # Hide axes for better viewing

# Define the levels of an 8-bit image (256 levels)
L = 2 ** 8

# Finding the negative of the image
neg = (L - 1) - skI

# Display the negative image
plt.subplot(1, 2, 2)
plt.imshow(neg)
plt.title("Negative Image")
plt.axis('off')  # Hide axes for better viewing

# Show both images
plt.show()
