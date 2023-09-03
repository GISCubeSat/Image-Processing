import numpy as np 
import cv2

def kmeans_image_compression(image_path, num_clusters, output_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert the image to RGB (OpenCV loads images in BGR by default)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Reshape the image to be a list of pixels
    pixels = img_rgb.reshape((-1, 3))

    # Convert to floating point for K-means
    pixels = np.float32(pixels)

    # Define criteria and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert back to 8 bit and the center colors to integer
    centers = np.uint8(centers)
    
    # Map each pixel to its corresponding center
    segmented_image = centers[labels.flatten()]

    # Reshape back to the original image
    compressed_img = segmented_image.reshape(img_rgb.shape)

    # Save the image with JPEG compression (or other formats that compress the image)
    cv2.imwrite(output_path, cv2.cvtColor(compressed_img, cv2.COLOR_RGB2BGR), [int(cv2.IMWRITE_JPEG_QUALITY), 60])

kmeans_image_compression("BlueEarthTest.jpeg", 10, "KMEANS_RESULT.jpeg")
