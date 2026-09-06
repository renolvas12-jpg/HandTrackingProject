# 🤖 Hand Tracking & Gesture Recognition

> A real-time computer vision project for detecting hands, tracking 21 hand landmarks, and recognizing hand gestures using **Python, OpenCV, and MediaPipe**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv" alt="OpenCV">
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge" alt="MediaPipe">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">
</p>

---

## 📌 Overview

**Hand Tracking & Gesture Recognition** is a real-time computer vision system that uses a webcam to detect and track human hands.

The project uses **MediaPipe's Hand Landmarker** to identify hand landmarks and **OpenCV** to capture and process video frames.

The detected landmarks can then be used to recognize different hand gestures and serve as the foundation for gesture-based human-computer interaction.

---

## ✨ Features

* 🎥 Real-time webcam hand tracking
* 🖐️ Detection of human hands
* 📍 Tracking of **21 hand landmarks**
* 🤖 Gesture recognition
* ⚡ Real-time video processing
* 📊 Landmark visualization
* 👥 Support for hand-tracking applications
* 🧩 Modular Python code
* 🔧 Easy to extend with new gestures and actions

---

## 🧠 How It Works

The system follows this pipeline:

```text
                 📷 Webcam
                    │
                    ▼
             🎥 Video Capture
                 OpenCV
                    │
                    ▼
              🖐️ Hand Detection
                 MediaPipe
                    │
                    ▼
             📍 21 Landmarks
                    │
                    ▼
          ✋ Gesture Recognition
                    │
                    ▼
              🎯 Output / Action
```

### Hand Landmark Detection

MediaPipe detects **21 key points** on the hand.

```text
              8     12     16     20
              ●      ●      ●      ●
              │      │      │      │
              │      │      │      │
       4 ●────┘      │      │      │
         │            │      │      │
         │            │      │      │
         ●────────────●──────●──────●
         0
```

These landmarks provide the coordinates needed to understand the position and movement of the fingers.

---

## 🛠️ Technologies Used

| Technology                   | Purpose                              |
| ---------------------------- | ------------------------------------ |
| 🐍 Python                    | Core programming language            |
| 👁️ OpenCV                   | Webcam capture and image processing  |
| 🖐️ MediaPipe                | Hand detection and landmark tracking |
| 🤖 MediaPipe Hand Landmarker | Real-time hand landmark detection    |

---

## 📂 Project Structure

```text
HandTrackingProject/
│
├── gesture.py
├── hand_detector.py
├── utils.py
├── webcam_test.py
├── hand_landmarker.task
├── requirements.txt
└── README.md
```

### File Description

| File                   | Description                            |
| ---------------------- | -------------------------------------- |
| `gesture.py`           | Handles gesture-related logic          |
| `hand_detector.py`     | Hand detection and landmark processing |
| `utils.py`             | Helper and utility functions           |
| `webcam_test.py`       | Runs the real-time webcam application  |
| `hand_landmarker.task` | MediaPipe hand landmark model          |
| `requirements.txt`     | Required Python dependencies           |
| `README.md`            | Project documentation                  |

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/renolvas12-jpg/HandTrackingProject.git
```

Move into the project directory:

```bash
cd HandTrackingProject
```

---

## 2️⃣ Create a Virtual Environment

It is recommended to use a virtual environment.

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Project

Start the webcam hand-tracking application:

```bash
python webcam_test.py
```

Your webcam should open and the system will begin detecting and tracking your hand.

---

# 🎮 Gesture Recognition

The project can be extended to recognize gestures such as:

| Gesture       | Possible Action    |
| ------------- | ------------------ |
| 🖐️ Open Palm | Pause / Stop       |
| ✊ Fist        | Select / Stop      |
| 👍 Thumbs Up  | Confirm            |
| ✌️ Peace      | Next               |
| ☝️ Point      | Cursor / Selection |
| 🤏 Pinch      | Click / Control    |

> Gesture names and actions depend on the implementation in the current version of the project.

---

# 📸 Demo

Add screenshots or a GIF of the project here.

### Example

```text
assets/
└── demo.gif
```

Then add it to this section:

```markdown
![Hand Tracking Demo](assets/demo.gif)
```

A short GIF showing the webcam, hand landmarks, and gesture recognition is recommended because it allows visitors to understand the project immediately.

---

# 📊 Performance

The system is designed for real-time computer vision applications.

Performance can depend on:

* 💻 Computer hardware
* 📷 Webcam resolution
* 🎥 Video frame rate
* 🖐️ Number of detected hands
* 🤖 Model configuration
* ⚙️ Processing environment

---

# 🔮 Future Improvements

The project is currently focused on the core hand-tracking and gesture-recognition pipeline.

Planned improvements include:

* [ ] ✋ Improved gesture classification
* [ ] 🎯 Gesture confidence score
* [ ] 👥 Multi-hand interaction
* [ ] 🖱️ Virtual mouse control
* [ ] 🎨 Air drawing
* [ ] 🔊 Volume control using hand gestures
* [ ] 📊 Real-time FPS and performance monitoring
* [ ] 🎤 Media control using gestures
* [ ] 📽️ Presentation control
* [ ] 🤖 Custom machine-learning gesture classifier
* [ ] 🌐 Web-based interface
* [ ] 📱 Improved user interface

---

# 🧪 Possible Applications

This technology can be used as a foundation for:

### 🖥️ Human-Computer Interaction

Control computer applications without physical input devices.

### 🖱️ Virtual Mouse

Use hand movements and gestures to control the mouse.

### 🎨 Virtual Drawing

Draw on the screen using your finger.

### 📽️ Presentation Control

Navigate presentation slides using hand gestures.

### 🎮 Gesture-Based Gaming

Use hand movements as game controls.

### ♿ Touchless Interfaces

Create interfaces that can be controlled without physical contact.

---

# ⚙️ Requirements

Make sure you have:

* Python 3.x
* Webcam
* Working internet connection for initial dependency installation

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

# 🐛 Troubleshooting

### Camera is not opening

Make sure:

* Your webcam is connected.
* No other application is using the camera.
* Your operating system has given Python permission to access the camera.

### `ModuleNotFoundError`

Try:

```bash
pip install -r requirements.txt
```

If a specific package is missing:

```bash
pip install <package-name>
```

### MediaPipe model error

Make sure:

```text
hand_landmarker.task
```

exists in the expected project directory.

---

# 🤝 Contributing

Contributions are welcome!

If you want to improve this project:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git add .
git commit -m "Add new gesture feature"
```

5. Push the branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

# 📜 License

This project is available under the **MIT License**.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

## Renol Vas

**Artificial Intelligence & Machine Learning Student**

Interested in:

* 🤖 Artificial Intelligence
* 🧠 Machine Learning
* 👁️ Computer Vision
* 🐍 Python
* 💻 Software Development

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

Your feedback and suggestions are always welcome!

---

<p align="center">
  Made with ❤️ using Python, OpenCV & MediaPipe
</p>
