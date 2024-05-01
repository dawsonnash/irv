import pandas as pd
import os
from PIL import Image

def convert_csv_to_yolo_labels(csv_path, images_dir, labels_dir):
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Process each row in the CSV file
    for index, row in df.iterrows():
        image_filename = row['image']
        image_path = os.path.join(images_dir, image_filename)

        # Open the image to get its dimensions
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                print(f"Successfully opened: {image_path}")

                # Calculate normalized bbox coordinates
                x_center = ((row['x1'] + row['x2']) / 2) / width
                y_center = ((row['y1'] + row['y2']) / 2) / height
                bbox_width = (row['x2'] - row['x1']) / width
                bbox_height = (row['y2'] - row['y1']) / height

                # Prepare the label file path
                label_filename = os.path.splitext(image_filename)[0] + '.txt'
                label_path = os.path.join(labels_dir, label_filename)

                # Write the YOLO label file
                with open(label_path, 'w') as file:
                    file.write(f"{row['Class']} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")
        except IOError as e:
            print(f"Error opening image: {image_path}. Error: {e}")

convert_csv_to_yolo_labels(
    r'C:\Users\dawso\.vscode\Projects\IRV_Model\cardatasettrain.csv',
    r'C:\Users\dawso\.vscode\Projects\IRV_Model\archive\cars_train\cars_train',
    r'C:\Users\dawso\.vscode\Projects\IRV_Model\archive\cars_train\cars_train_labels'
)
