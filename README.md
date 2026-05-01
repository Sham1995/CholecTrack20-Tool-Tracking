# Surgical Tool Detection and Tracking (CholecTrack20)

## Overview
This project implements a complete pipeline for detecting and tracking surgical tools using the CholecTrack20 dataset and YOLOv8.

The workflow includes:
- Dataset preparation
- Annotation conversion (JSON → YOLO format)
- Model training
- Detection
- Tracking

## Pipeline
CholecTrack20 Dataset → JSON Annotations → YOLO Format → Training → Detection → Tracking

## Repository Structure
scripts/        # Python scripts for preprocessing  
results/        # Training outputs and evaluation results  
screenshots/    # Evidence for report  
data.yaml       # YOLO dataset configuration  
requirements.txt  
README.md  

## Setup Instructions

### 1. Clone Repository
git clone https://github.com/YOUR_USERNAME/CholecTrack20-Tool-Tracking.git  
cd CholecTrack20-Tool-Tracking  

### 2. Install Dependencies
pip install -r requirements.txt  

### 3. Download Dataset
Download the CholecTrack20 dataset from:  
https://www.synapse.org/Synapse:syn53182642/wiki/628404  

Place it inside:  
datasets/CholecTrack20/  

## Running the Pipeline

### Step 1: Convert JSON Annotations to YOLO Format
python scripts/convert_to_yolo.py  

### Step 2: Prepare Dataset (Images + Labels)
python scripts/prepare_dataset.py  

This creates:  
datasets/cholec_yolo/images/train/  
datasets/cholec_yolo/images/val/  
datasets/cholec_yolo/labels/train/  
datasets/cholec_yolo/labels/val/  

### Step 3: Train YOLO Model
yolo detect train data=data.yaml model=yolov8n.pt epochs=10 imgsz=640  

Output saved to:  
runs/detect/train-*/  

### Step 4: Run Detection
yolo detect predict model=runs/detect/train-*/weights/best.pt source=PATH_TO_IMAGES  

### Step 5: Run Tracking
yolo track model=runs/detect/train-*/weights/best.pt source=PATH_TO_FRAMES imgsz=640  

Tracking results saved to:  
runs/detect/track-*/  

## Results
- Model successfully detects surgical tools in laparoscopic images  
- Tracking applied across video frames  
- Output includes bounding boxes and trajectories  

Sample outputs are available in the results/ and screenshots/ folders.

## Important Notes
- The dataset is NOT included due to size (~35GB) and licensing restrictions  
- Make sure dataset paths match data.yaml  
- Training was performed using YOLOv8  

## Author
Shamsa
