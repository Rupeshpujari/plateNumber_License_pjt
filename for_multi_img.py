import os
import cv2
from ultralytics import YOLO
import easyocr
from states_db import states   # import database

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Use relative paths
base_path = os.path.dirname(__file__)   # current folder path
folder_path = os.path.join(base_path, "test_images")
model_path = os.path.join(base_path, "license_plate_detector.pt")

# Load YOLO model
model = YOLO(model_path)

# Loop through all images in folder
for filename in os.listdir(folder_path):
    img_path = os.path.join(folder_path, filename)
    image = cv2.imread(img_path)

    if image is None:
        print(f"Error: Could not read {filename}")
        continue

    color_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = model.predict(color_img, verbose=False)
    if len(results[0].boxes) == 0:
        print(f"No plate detected in {filename}")
        continue

    x1, y1, x2, y2 = map(int, results[0].boxes.xyxy[0].tolist())
    plate_img = color_img[y1:y2, x1:x2]

    lpnum = reader.readtext(plate_img)

    plate_text = None
    for detection in lpnum:
        text = detection[1].replace(" ", "")
        if len(text) >= 6 and any(c.isdigit() for c in text):
            plate_text = text
            break

    print(f"\nImage: {filename}")
    if plate_text:
        print("Detected Plate Number:", plate_text)
        code = plate_text[0:2].upper()
        if code in states:
            print("State:", states[code])
        else:
            print("Unknown/Invalid state code:", code)
    else:
        print("No valid plate number detected")
