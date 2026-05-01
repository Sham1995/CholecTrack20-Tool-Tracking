\# Surgical Tool Detection and Tracking (CholecTrack20)



\## Overview

This project implements a pipeline for surgical tool detection and tracking using the CholecTrack20 dataset.



\## Pipeline

Dataset → JSON → YOLO → Training → Detection → Tracking



\## Steps to Run



\### 1. Download Dataset

Run:

python scripts/download\_cholec.py



\### 2. Convert Annotations to YOLO Format

python scripts/convert\_to\_yolo.py



\### 3. Prepare Dataset

python scripts/prepare\_dataset.py



\### 4. Train YOLO Model

yolo detect train data=data.yaml model=yolov8n.pt epochs=10 imgsz=640



\### 5. Run Tracking

yolo track model=runs/detect/train/weights/best.pt source=path\_to\_frames conf=0.01



\## Results

The model successfully detects and tracks surgical tools across video frames.



\## Notes

\- Dataset is not included due to size and licensing restrictions.

\- Results are stored in the `runs/` directory.



\## Author

Shamsa

