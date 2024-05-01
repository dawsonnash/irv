import os

label_dir = r'C:\Users\dawso\.vscode\Projects\IRV_Model\archive\cars_test\labels'

# Get a list of all the label files
label_files = os.listdir(label_dir)

# Go through each label file and adjust the class IDs
for label_file in label_files:
    label_file_path = os.path.join(label_dir, label_file)
    with open(label_file_path, 'r') as file:
        labels = file.readlines()

    # Adjust the class IDs
    new_labels = []
    for label in labels:
        parts = label.strip().split()
        class_id = int(parts[0]) - 1  # Subtract 1 from the class ID
        new_label = f"{class_id} {' '.join(parts[1:])}\n"
        new_labels.append(new_label)

    # Write the adjusted labels back to the file
    with open(label_file_path, 'w') as file:
        file.writelines(new_labels)
