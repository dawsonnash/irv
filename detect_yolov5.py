import argparse
import os
import sys
from yolov5.detect import run as run_detect
import torch

def detect_objects(weights_path, source, img_size=640, conf_thres=0.005, max_det=1, output_dir=None):
    # Check if the weights file exists
    if not os.path.exists(weights_path):
        print(f"Error: Weights file not found at {weights_path}")
        sys.exit(1)

    detect_args = {
        'weights': weights_path,
        'source': source,
        'imgsz': (img_size, img_size),
        'conf_thres': conf_thres,
        'device': 'cuda' if torch.cuda.is_available() else 'cpu',
        'max_det': max_det,
        'save_txt': True,  # Enable saving mapped labels to text files

    }

    # Run detection
    results = run_detect(**detect_args)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Detect Objects with YOLOv5")
    parser.add_argument('--weights', type=str, required=True, help='Trained weights path')
    parser.add_argument('--source', type=str, required=True, help='Path to images or video for detection')
    parser.add_argument('--img_size', type=int, default=640, help='Image size for detection')
    parser.add_argument('--conf_thres', type=float, default=0.005, help='Confidence threshold for detection')
    parser.add_argument('--max_det', type=int, default=1, help='Maximum number of detections per image')
    parser.add_argument('--output_dir', type=str, default=None, help='Output directory for mapped labels')


    args = parser.parse_args()
    detect_objects(args.weights, args.source, args.img_size, args.conf_thres, args.max_det, args.output_dir)
