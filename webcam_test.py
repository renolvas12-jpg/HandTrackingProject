"""Professional real-time hand tracking application.

Press Q or Esc to close the preview window.
"""

from pathlib import Path
import time

import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core.base_options import BaseOptions


# --------------------------------------------------
# Configuration
# --------------------------------------------------

MODEL_PATH = Path(__file__).with_name("hand_landmarker.task")

WINDOW_NAME = "Hand Tracking"

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

MIN_DETECTION_CONFIDENCE = 0.5
MIN_PRESENCE_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5

CONNECTIONS = vision.HandLandmarksConnections.HAND_CONNECTIONS


# --------------------------------------------------
# Camera
# --------------------------------------------------

def open_camera() -> cv2.VideoCapture:
    """Open the default webcam."""

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not camera.isOpened():
        camera.release()
        camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise RuntimeError(
            "Could not open webcam.\n"
            "Close other applications using the camera and "
            "check Windows camera permissions."
        )

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    return camera


# --------------------------------------------------
# Drawing
# --------------------------------------------------

def draw_hand(frame, landmarks) -> None:
    """Draw the 21 hand landmarks and connections."""

    height, width = frame.shape[:2]

    points = [
        (int(point.x * width), int(point.y * height))
        for point in landmarks
    ]

    # Draw connections
    for connection in CONNECTIONS:
        start = points[connection.start]
        end = points[connection.end]

        cv2.line(
            frame,
            start,
            end,
            (0, 255, 0),
            2
        )

    # Draw landmarks
    for point in points:
        cv2.circle(
            frame,
            point,
            5,
            (0, 0, 255),
            -1
        )


# --------------------------------------------------
# Information panel
# --------------------------------------------------

def draw_info_panel(frame, fps, hand_count):
    """Draw a professional information panel."""

    height, width = frame.shape[:2]

    # Semi-transparent top panel
    overlay = frame.copy()

    cv2.rectangle(
        overlay,
        (0, 0),
        (width, 90),
        (20, 20, 20),
        -1
    )

    frame[:] = cv2.addWeighted(
        overlay,
        0.75,
        frame,
        0.25,
        0
    )

    # Project title
    cv2.putText(
        frame,
        "HAND TRACKING",
        (20, 32),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # FPS
    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (20, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    # Hand count
    cv2.putText(
        frame,
        f"Hands: {hand_count}",
        (180, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    # Status
    status = "TRACKING" if hand_count > 0 else "SEARCHING..."

    cv2.putText(
        frame,
        f"Status: {status}",
        (340, 65),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

    # Quit instruction
    cv2.putText(
        frame,
        "Q / ESC: Quit",
        (width - 180, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (220, 220, 220),
        1
    )


# --------------------------------------------------
# Main application
# --------------------------------------------------

def main() -> None:

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Missing model: {MODEL_PATH.name}\n"
            "Download the MediaPipe hand-landmarker model "
            "and place it in the project folder."
        )

    options = vision.HandLandmarkerOptions(
        base_options=BaseOptions(
            model_asset_path=str(MODEL_PATH)
        ),
        running_mode=vision.RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=MIN_DETECTION_CONFIDENCE,
        min_hand_presence_confidence=MIN_PRESENCE_CONFIDENCE,
        min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
    )

    camera = open_camera()

    cv2.namedWindow(
        WINDOW_NAME,
        cv2.WINDOW_NORMAL
    )

    previous_time = time.perf_counter()

    try:

        with vision.HandLandmarker.create_from_options(
            options
        ) as detector:

            while True:

                success, frame = camera.read()

                if not success:
                    raise RuntimeError(
                        "The webcam stopped returning frames."
                    )

                # Mirror camera
                frame = cv2.flip(frame, 1)

                # Convert BGR → RGB
                rgb_frame = cv2.cvtColor(
                    frame,
                    cv2.COLOR_BGR2RGB
                )

                image = mp.Image(
                    image_format=mp.ImageFormat.SRGB,
                    data=rgb_frame
                )

                # MediaPipe timestamp
                timestamp = int(
                    time.monotonic() * 1000
                )

                result = detector.detect_for_video(
                    image,
                    timestamp
                )

                # Draw detected hands
                for landmarks in result.hand_landmarks:
                    draw_hand(
                        frame,
                        landmarks
                    )

                hand_count = len(
                    result.hand_landmarks
                )

                # Calculate FPS
                current_time = time.perf_counter()

                elapsed = current_time - previous_time

                if elapsed > 0:
                    fps = 1.0 / elapsed
                else:
                    fps = 0.0

                previous_time = current_time

                # Draw UI
                draw_info_panel(
                    frame,
                    fps,
                    hand_count
                )

                # Display
                cv2.imshow(
                    WINDOW_NAME,
                    frame
                )

                key = cv2.waitKey(1) & 0xFF

                if key in (ord("q"), 27):
                    break

    finally:

        camera.release()

        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()