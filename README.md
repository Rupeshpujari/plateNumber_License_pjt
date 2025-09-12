## License Plate Recognition 🚘🔍
- This project uses YOLOv8 for license plate detection and EasyOCR for text recognition. It can process both single images and multiple images in a folder. The project also maps license plate prefixes to Indian states (e.g., HR → Haryana).
### 🌟 Features
- Detects license plates with high accuracy using YOLOv8
- Reads and extracts plate numbers with EasyOCR
- Supports single image and batch (folder) processing
- Maps plate prefixes to Indian states
- Extendable to video and real-time recognition
### 🔧 Tech Stack
- Python
- YOLOv8 (Ultralytics)
- OpenCV
- EasyOCR
- Matplotlib
### 📌 Use Cases
- Traffic monitoring
- Parking systems
- Toll collection automation
- Security and surveillance
## 📂 Project Structure
<pre> 
plateNumber_License_pjt/
│── test_images/         # Folder containing test image
│── single_img.py        # Run recognition on a single image
│── multi_img.py         # Run recognition on multiple images
│── states_db.json       # Database of Indian state codes
│── README.md            # Project documentation
    </pre>
## ⚙️ Requirements
Install dependencies before running:
```
pip install ultralytics
pip install matplotlib
pip install opencv-python
pip install easyocr
```
## 1. Run on a Single Image:
``` 
python single_img.py
```
- Detects license plate
- Extracts text using EasyOCR
- Prints the plate number and state name
## 2. Run on Multiple Images
   - Put all test images inside test_images/ folder, then run:
   ```
python multi_img.py
```
   Loops through all images in the folder
   Detects plates and recognizes text
   Prints plate numbers + states for each image
## 🗂️ State Database
   - State codes are stored in states_db.json:
   ```
{
  "AP": "Andhra Pradesh",
  "HR": "Haryana",
  "TS": "Telangana",
  "MH": "Maharashtra",
  "TN": "Tamil Nadu",
  "KA": "Karnataka"
  }
```
- You can add more states as needed.
📸 Example
```
Input Image:
Car with number plate → HR26FC2782
```
```
Output:
Detected Plate Number: HR26FC2782
State: Haryana
```
🚀 Future Enhancements

🔹 Add support for video input (process video files in addition to static images)

🔹 Enable real-time detection from live video/webcam

🔹 Improve OCR accuracy with preprocessing techniques (grayscale, thresholding, noise removal, contrast enhancement)

🔹 Expand the states database to include all RTO codes for finer location mapping

🔹 Support for multiple license plates in a single frame

🔹 Export results (plate number, state, timestamp) into CSV/Excel for record-keeping
## 👨‍💻 Author
- Rupesh Pujari
- 📍 Innomatics Research Labs
- 💼 Data Analytics/Science
