import os
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import easyocr
from states_db import states   # import database

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Base project path (where this script is located)
base_path = os.path.dirname(__file__)

# Paths (relative, not absolute)
image_path = os.path.join(base_path, "test_images", "car1.webp")
model_path = os.path.join(base_path, "license_plate_detector.pt")

# Load image
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found at", image_path)
    exit()

# Convert to RGB
color_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Load YOLO model
model = YOLO(model_path)

# Run detection
results = model.predict(color_img, verbose=False)

if len(results[0].boxes) == 0:
    print("No plate detected")
    exit()

# Bounding box
x1, y1, x2, y2 = map(int, results[0].boxes.xyxy[0].tolist())
plate_img = color_img[y1:y2, x1:x2]

# OCR
lpnum = reader.readtext(plate_img)

plate_text = None
for detection in lpnum:
    text = detection[1].replace(" ", "")
    if len(text) >= 6 and any(c.isdigit() for c in text):
        plate_text = text
        break

if plate_text:
    print("Detected Plate Number:", plate_text)
    code = plate_text[0:2].upper()
    if code in states:
        print("State:", states[code])
    else:
        print("Unknown/Invalid state code:", code)
else:
    print("No valid plate number detected")
