# Hand Tracking

This project uses the MediaPipe Tasks hand-landmarker API. The older
`mp.solutions.hands` API is not included in MediaPipe 1.0.0, so use
`webcam_test.py` rather than legacy examples.

## One-time model download

Run this from the project folder in PowerShell:

```powershell
Invoke-WebRequest https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task -OutFile hand_landmarker.task
```

## Run

```powershell
.\venv\Scripts\python.exe webcam_test.py
```

Allow camera access for desktop apps in **Windows Settings > Privacy & security > Camera**. Keep your hand in good light, palm facing the camera, and fully inside the frame. Press `Q` or `Esc` to exit.


## Description ✏️
```To perform video tracking an algorithm analyzes sequential video frames and outputs the movement of targets between the frames. There are a variety of algorithms, each having strengths and weaknesses. Considering the intended use is important when choosing which algorithm to use. There are two major components of a visual tracking system: target representation and localization, as well as filtering and data association.

Video tracking is the process of locating a moving object (or multiple objects) over time using a camera. It has a variety of uses, some of which are: human-computer interaction, security and surveillance, video communication and compression, augmented reality, traffic control, medical imaging and video editing.
```
