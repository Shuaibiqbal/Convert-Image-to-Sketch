import numpy as np
import imageio
import cv2
from scipy.ndimage import gaussian_filter

def convert_to_sketch(image_path):
    # Read the image
    img = imageio.imread(image_path)

    # Convert to grayscale using cv2
    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Apply Gaussian blur
    blurred_img = gaussian_filter(gray_img, sigma=1)

    # Invert the image
    inverted_img = cv2.bitwise_not(blurred_img)

    # Create the sketch by dividing the grayscale image by the inverted blurred image
    sketch_img = cv2.divide(gray_img, inverted_img, scale=256.0)

    # Display or save the result
    cv2.imshow('Original Image', img)
    cv2.imshow('Sketch', sketch_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = '/home/shuaib/Pictures/test.jpg'
convert_to_sketch(image_path)
