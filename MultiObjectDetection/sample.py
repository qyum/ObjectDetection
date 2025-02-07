from collections import defaultdict
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import os

# Dictionary to store tracking history with default empty lists
track_history = defaultdict(lambda: [])

# Load the checkpoint from yolo11 trained model
model = YOLO('D:/ObjectDetection/MultiObjectDetection/yolo11n.pt')

output_dir = "D:/yolov8_tracking/output"  
os.makedirs(output_dir, exist_ok=True)

# Process the video and save the output 
result = model("D:/yolov8_tracking/road_trafifc.mp4", save=True, show=True, project=output_dir)