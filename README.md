License Plate Recognition 🚘🔍
This project uses YOLOv8 for license plate detection and EasyOCR for text recognition. It can process both single images and multiple images in a folder. The project also maps license plate prefixes to Indian states (e.g., HR → Haryana).
📂 Project Structure
plateNumber_License_pjt/
│── single_img.py        # Run recognition on a single image
│── multi_img.py         # Run recognition on multiple images
│── states_db.json       # Database of Indian state codes
│── test_images/         # Folder containing test images
│── runs/                # YOLO output (detections)
│── README.md            # Project documentation
⚙️ Requirements
Install dependencies before running:
pip install ultralytics easyocr opencv-python matplotlib
▶️ Usage
1. Run on a Single Image:
   python single_img.py
   Detects license plate
   Extracts text using EasyOCR
   Prints the plate number and state name
2. Run on Multiple Images
   Put all test images inside test_images/ folder, then run:
   python multi_img.py
   Loops through all images in the folder
   Detects plates and recognizes text
   Prints plate numbers + states for each image
🗂️ State Database
   State codes are stored in states_db.json:
   {
  "AP": "Andhra Pradesh",
  "HR": "Haryana",
  "TS": "Telangana",
  "MH": "Maharashtra",
  "TN": "Tamil Nadu",
  "KA": "Karnataka"
  }
You can add more states as needed.
📸 Example
Input Image:
Car with number plate → HR26FC2782
Output:
Detected Plate Number: HR26FC2782
State: Haryana
🚀 Future Enhancements
Add support for video input
Improve OCR accuracy with preprocessing
Expand the states database for all RTO codes
👨‍💻 Author
Rupesh Pujari
📍 Innomatics Research Labd
💼 Data Analytics/Science
