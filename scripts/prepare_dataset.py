import os
import shutil

# -------- CONFIG --------
PROJECT_DIR = r"C:\Users\shamsa\Desktop\StrongSORT"

VIDEO_NAME = "VID02"

frames_dir = os.path.join(
    PROJECT_DIR,
    "datasets",
    "CholecTrack20",
    "Training",
    VIDEO_NAME,
    "Frames"
)

labels_dir = os.path.join(
    PROJECT_DIR,
    "datasets",
    "yolo_labels"
)

out_images_dir = os.path.join(
    PROJECT_DIR,
    "datasets",
    "cholec_yolo",
    "images",
    "train"
)

out_labels_dir = os.path.join(
    PROJECT_DIR,
    "datasets",
    "cholec_yolo",
    "labels",
    "train"
)

os.makedirs(out_images_dir, exist_ok=True)
os.makedirs(out_labels_dir, exist_ok=True)

copied = 0
missing_labels = 0

for image_file in os.listdir(frames_dir):
    if not image_file.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    base_name = os.path.splitext(image_file)[0]
    label_file = base_name + ".txt"

    image_path = os.path.join(frames_dir, image_file)
    label_path = os.path.join(labels_dir, label_file)

    if not os.path.exists(label_path):
        missing_labels += 1
        continue

    out_image_path = os.path.join(out_images_dir, image_file)
    out_label_path = os.path.join(out_labels_dir, label_file)

    if not os.path.exists(out_image_path):
        shutil.copy2(image_path, out_image_path)

    if not os.path.exists(out_label_path):
        shutil.copy2(label_path, out_label_path)

    copied += 1

print("Dataset preparation complete.")
print(f"Video processed: {VIDEO_NAME}")
print(f"Copied image-label pairs: {copied}")
print(f"Images skipped because label was missing: {missing_labels}")
print(f"Images saved to: {out_images_dir}")
print(f"Labels saved to: {out_labels_dir}")