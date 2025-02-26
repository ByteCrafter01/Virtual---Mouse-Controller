# Hand Gesture Detection using OpenCV and Mediapipe

## Overview
This project uses OpenCV and Mediapipe to detect and track hand landmarks in real-time from a webcam feed. The captured frames are processed to identify hand gestures, which can later be used for various applications like sign language recognition, virtual mouse control, or gesture-based interactions.

## Requirements
Make sure you have the following dependencies installed:

### Prerequisites
- Python 3.x
- OpenCV (`cv2`)
- Mediapipe

### Installation
Run the following command to install the required packages:
```sh
pip install opencv-python mediapipe
```

## How It Works
1. The script accesses the webcam feed using OpenCV.
2. It uses Mediapipe's `Hands` module to detect and track hand landmarks in real-time.
3. The detected hand landmarks are extracted and stored in a list.
4. The hand landmarks are drawn on the frame for visualization.
5. The processed frame is displayed in a window.
6. The script terminates when the user presses the `Esc` key.

## Code Breakdown
### Initializing Mediapipe Hands Module
The `Hands` module is configured to detect a maximum of one hand with a minimum confidence of 70% for both detection and tracking.

### Capturing Video
OpenCV's `VideoCapture(0)` is used to access the primary webcam.

### Processing Frames
- The frame is flipped to mirror the image.
- The frame is converted to RGB (as Mediapipe expects RGB images).
- Hand landmarks are detected and extracted.
- The landmarks are drawn on the frame.

### Displaying Output
The processed frame is displayed using OpenCV's `imshow` function.

### Exit Condition
The script exits when the `Esc` key (ASCII code 27) is pressed.

## Running the Code
To execute the script, run the following command:
```sh
python script_name.py
```
Replace `script_name.py` with the actual filename of your script.

## Possible Enhancements
- Implement a function to recognize specific hand gestures.
- Extend support for multiple hands.
- Integrate gesture-based control functionalities.

## Notes
- Ensure your webcam is functional before running the script.
- The `util` module is imported but not used in this script; it may be required for further enhancements.

## License
This project is open-source and can be modified for educational and research purposes.

