import cv2
import os

def draw_bounding_box(image_path, label_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image {image_path}")
        return

    # Check image dimensions
    height, width, _ = image.shape

    # Read the label file and draw each bounding box
    with open(label_path, 'r') as file:
        for line in file:
            class_id, x_center, y_center, bbox_width, bbox_height = map(float, line.split())
            
            # Convert normalized coordinates to absolute coordinates
            x_center *= width
            y_center *= height
            bbox_width *= width
            bbox_height *= height

            # Calculate the bounding box's top-left corner
            x_min = int(x_center - bbox_width / 2)
            y_min = int(y_center - bbox_height / 2)

            # Draw the bounding box
            cv2.rectangle(image, (x_min, y_min), (int(x_min + bbox_width), int(y_min + bbox_height)), (0, 255, 0), 2)
            cv2.putText(image, str(int(class_id)), (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    # Show the image with bounding boxes
    cv2.imshow('Image with Bounding Boxes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = r'C:\Users\dawso\.vscode\Projects\IRV_Model\archive\cars_test\cars_test_images\00002.jpg'
label_path = r'C:\Users\dawso\.vscode\Projects\IRV_Model\archive\cars_test\cars_test_labels\00002.txt'
draw_bounding_box(image_path, label_path)
