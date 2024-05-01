import argparse
from pathlib import Path
import yaml
import torch

def train_model(data_yaml, weights_path, img_size=640, batch_size=16, epochs=50):
    # Ensure CUDA is available if possible
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    
    # Load the training script from YOLOv5
    from yolov5.train import run as run_train
    
    # Prepare the training arguments
    train_args = {
        'data': data_yaml,
        'weights': weights_path,
        'imgsz': img_size,
        'batch_size': batch_size,
        'epochs': epochs,
        'device': device
    }
    
    # Run the training
    run_train(**train_args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Train YOLOv5 Model")
    parser.add_argument('--data_yaml', type=str, help='Path to dataset YAML file')
    parser.add_argument('--weights', type=str, help='Initial weights path')
    parser.add_argument('--img_size', type=int, default=640, help='Image size')
    parser.add_argument('--batch_size', type=int, default=16, help='Batch size')
    parser.add_argument('--epochs', type=int, default=50, help='Number of epochs')
    
    args = parser.parse_args()
    
    train_model(args.data_yaml, args.weights, args.img_size, args.batch_size, args.epochs)

# Training command
# python python train_yolov5.py --data_yaml dataset.yaml --weights yolov5s.pt --epochs 50   
