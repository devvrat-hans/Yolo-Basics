# Yolo-Basics

This project is focused on object detection using the YOLO (You Only Look Once) algorithm. It includes various Python scripts for detecting objects in images, video streams, and from multiple video sources. Additionally, it includes model weights for YOLO, and a set of pre-recorded videos for testing.

## Project Structure

The repository is organized as follows:
```
├── Images/                  # Folder containing sample images for object detection
├── Yolo_weights/            # Pre-trained YOLO model weights
├── videos/                  # Sample videos for object detection
├── 01_yolo_basics.py        # Basic YOLO object detection script
├── 02_yolo_webcam.py        # YOLO object detection from webcam
├── 03_yolo_multiple.py      # YOLO object detection from multiple sources (webcam/video)
├── LICENSE                  # Project license
├── README.md                # This file
└── requirements.txt         # Python dependencies for the project
```

## Features

- **Image Detection**: Use YOLO to detect objects in static images.
- **Webcam Detection**: Detect objects in real-time using your computer's webcam.
- **Multiple Source Detection**: Run YOLO detection on multiple video sources simultaneously.
- **Pre-trained Weights**: Includes pre-trained YOLO model weights for faster testing.

## Installation

To get started, first clone this repository:

```bash
git clone https://github.com/your-username/Yolo-Basics.git
cd Yolo-Basics
```

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

- **For Image Detection**: Run `01_yolo_basics.py` to test YOLO detection on sample images.
  
  ```bash
  python 01_yolo_basics.py
  ```

- **For Webcam Detection**: Run `02_yolo_webcam.py` to detect objects via your webcam.
  
  ```bash
  python 02_yolo_webcam.py
  ```

- **For Multiple Video Source Detection**: Run `03_yolo_multiple.py` to detect objects from multiple video sources (e.g., webcam and video file).
  
  ```bash
  python 03_yolo_multiple.py
  ```

## Files and Folders

- **Images/**: Contains sample images for testing YOLO detection.
- **Yolo_weights/**: Contains the pre-trained weights file for YOLO.
- **videos/**: Contains sample video files for testing object detection.
- **requirements.txt**: A list of required Python libraries.
- **LICENSE**: The license for the project.

## Requirements

The project requires Python 3.x and the following dependencies:

- OpenCV
- NumPy
- Pytorch
- other dependencies listed in `requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this template to fit your specific project details. Happy coding! 😄🚀
