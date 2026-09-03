"""Live webcam hand tracking using the MediaPipe Tasks API.

Press Q or Esc to close the preview window.
"""

from pathlib import Path
import time

import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core.base_options import BaseOptions


MODEL_PATH = Path(__file__).with_name("hand_landmarker.task")
CONNECTIONS = vision.HandLandmarksConnections.HAND_CONNECTIONS


def open_camera() -> cv2.VideoCapture:
    """Open the default Windows webcam and fail with an actionable message."""
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not camera.isOpened():
        camera.release()
        camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError(
            "Could not open webcam. Close other apps using the camera and allow "
            "camera access in Windows Settings > Privacy & security > Camera."
        )
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    return camera


def draw_hand(frame, landmarks) -> None:
    """Draw the 21 detected landmarks and the lines between them."""
    height, width = frame.shape[:2]
    points = [(int(point.x * width), int(point.y * height)) for point in landmarks]

    for connection in CONNECTIONS:
        cv2.line(frame, points[connection.start], points[connection.end], (0, 255, 0), 2)
    for point in points:
        cv2.circle(frame, point, 5, (0, 0, 255), -1)


def main() -> None:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Missing model: {MODEL_PATH.name}. Download it using the command in README.md."
        )

    options = vision.HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=str(MODEL_PATH)),
        running_mode=vision.RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    camera = open_camera()
    cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)

    try:
        with vision.HandLandmarker.create_from_options(options) as detector:
            while True:
                success, frame = camera.read()
                if not success:
                    raise RuntimeError("The webcam stopped returning frames.")

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
                result = detector.detect_for_video(image, int(time.monotonic() * 1000))

                for landmarks in result.hand_landmarks:
                    draw_hand(frame, landmarks)

                count = len(result.hand_landmarks)
                message = f"Hands detected: {count}  |  Press Q or Esc to quit"
                cv2.putText(frame, message, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                cv2.imshow("Hand Tracking", frame)

                key = cv2.waitKey(1) & 0xFF
                if key in (ord("q"), 27):
                    break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
