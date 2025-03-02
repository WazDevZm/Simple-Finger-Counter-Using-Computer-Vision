# Finger Counter using OpenCV and Mediapipe

## Project Overview
This project is a real-time finger counting application that utilizes OpenCV and Mediapipe to track and detect raised fingers from a webcam feed. Additionally, it integrates text-to-speech functionality using `pyttsx3` to announce the number of raised fingers aloud. The project is designed to work with a single hand and is useful for gesture-based applications, human-computer interaction, or accessibility solutions.

## Features
- Real-time hand tracking using MediaPipe
- Finger counting based on finger tip positions
- Visual overlay showing the number of raised fingers
- Text-to-speech output to announce the count
- Smooth performance with a webcam feed

## Tech Stack Used
- **Python**: Programming language used to develop the application.
- **OpenCV**: Used for video capture and image processing.
- **MediaPipe**: A framework for real-time hand tracking and gesture recognition.
- **pyttsx3**: A text-to-speech conversion library for Python.
- **NumPy**: (Implicitly used by OpenCV) for handling array operations efficiently.

## How It Works
1. The webcam captures the video feed.
2. OpenCV processes the frames, converting them to RGB format.
3. MediaPipe detects the hand landmarks and extracts the key points.
4. The program checks the relative positions of fingertips to count the number of raised fingers.
5. The count is displayed on the screen using OpenCV.
6. `pyttsx3` announces the number of fingers raised when the count changes.

## How to Run the Project Locally
### Prerequisites
Ensure you have Python installed (preferably Python 3.7 or later). You also need to install the required dependencies.

### Installation Steps
1. **Clone the Repository** (or create a new Python script and copy the code):
   ```sh
   git clone https://github.com/your-repository/finger-counter.git
   cd finger-counter
   ```
2. **Create a Virtual Environment (Recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. **Install Dependencies**:
   ```sh
   pip install opencv-python mediapipe pyttsx3 numpy
   ```
4. **Run the Script**:
   ```sh
   python finger_counter.py
   ```
5. **Usage**:
   - The program will launch your webcam and start detecting fingers.
   - Show different numbers of fingers to see the count on the screen.
   - The program will announce the number of raised fingers aloud.
   - Press 'q' to exit the program.

## Future Improvements
- Support for multiple hands.
- Improved finger detection accuracy using deep learning.
- Gesture-based command execution (e.g., controlling system volume or media playback).
- UI-based interface instead of OpenCV window.
- Integration with IoT devices for smart home applications.

## Credits
Developed by **Wazingwa Mugala** - Computer Engineering @ Copperbelt University (CBU).

## License
This project is open-source and available under the MIT License.

