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
