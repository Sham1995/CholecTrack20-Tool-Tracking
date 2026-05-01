import os
import json

# Paths
DATASET_PATH = r"C:\Users\shamsa\Desktop\StrongSORT\datasets\CholecTrack20\Training"
OUTPUT_PATH = r"C:\Users\shamsa\Desktop\StrongSORT\datasets\yolo_labels"

os.makedirs(OUTPUT_PATH, exist_ok=True)

for vid in os.listdir(DATASET_PATH):
    vid_path = os.path.join(DATASET_PATH, vid)

    json_file = os.path.join(vid_path, f"{vid.lower()}.json")
    
    if not os.path.exists(json_file):
        continue

    print(f"Processing {vid}...")

    with open(json_file, 'r') as f:
        data = json.load(f)

    frames_path = os.path.join(vid_path, "Frames")

    for frame_id, objects in data["annotations"].items():

        frame_name = str(frame_id).zfill(6) + ".txt"
        label_path = os.path.join(OUTPUT_PATH, frame_name)

        lines = []

        for obj in objects:
            cls = obj["instrument"]
            x, y, w, h = obj["tool_bbox"]

            # Convert to YOLO format
            x_center = x + w / 2
            y_center = y + h / 2

            line = f"{cls} {x_center} {y_center} {w} {h}"
            lines.append(line)

        with open(label_path, "w") as f:
            f.write("\n".join(lines))

print("✅ Conversion complete!")