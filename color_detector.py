import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def find_dominant_color(image, bbox):
    # Convert the image to RGB
    image_rgb = image.convert('RGB')

    # Crop the image to the bounding box
    cropped_image = image_rgb.crop(bbox)

    # Convert cropped image to numpy array
    cropped_array = np.array(cropped_image)

    # Flatten the 3D array to 2D array
    pixels = cropped_array.reshape(-1, 3)

    # Compute histogram for each color channel
    hist_r, bins_r = np.histogram(pixels[:, 0], bins=256, range=[0, 256])
    hist_g, bins_g = np.histogram(pixels[:, 1], bins=256, range=[0, 256])
    hist_b, bins_b = np.histogram(pixels[:, 2], bins=256, range=[0, 256])

    # Find the bin with the highest count for each channel
    dominant_color_r = bins_r[np.argmax(hist_r)]
    dominant_color_g = bins_g[np.argmax(hist_g)]
    dominant_color_b = bins_b[np.argmax(hist_b)]

    # Combine the RGB values
    dominant_color = (dominant_color_r, dominant_color_g, dominant_color_b)

    return dominant_color

# Load the image
image_path = 'path_to_your_image.jpg'
image = Image.open(image_path)

# Bounding box coordinates (xmin, ymin, xmax, ymax)
bbox = (xmin, ymin, xmax, ymax)

# Find the dominant color within the bounding box
dominant_color = find_dominant_color(image, bbox)

print("Dominant color:", dominant_color)
