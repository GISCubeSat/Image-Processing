import cv2
import numpy as np
import os

img = cv2.imread('NAmericaEarth.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define the number of bins and their midpoints
n_bins = 4
bin_size = 256 // n_bins
midpoints = np.linspace(bin_size//2, 255 - bin_size//2, n_bins).astype(np.uint8)

# Quantize each pixel in grayscale
quantized_gray = np.digitize(gray, np.linspace(bin_size, 255-bin_size+1, n_bins-1)) - 1
quantized_gray = midpoints[quantized_gray]

# Convert the quantized grayscale back to RGB
quantized_rgb = cv2.cvtColor(quantized_gray, cv2.COLOR_GRAY2BGR)

# Resize the image to half its original dimensions
new_width = int(quantized_rgb.shape[1] * 0.1)
new_height = int(quantized_rgb.shape[0] * 0.1)
resized_img = cv2.resize(quantized_rgb, (new_width, new_height))

# Display the resized image
cv2.imshow('Resized Image', resized_img)

# Save the resized image to a temporary file
temp_filename = "temp.jpg"
cv2.imwrite(temp_filename, resized_img)

# Calculate the file size
file_size = os.path.getsize(temp_filename)

# Print the file size in kilobytes (KB)
print(f"File size: {file_size / 1024:.2f} KB")
cv2.waitKey(0)
cv2.destroyAllWindows()