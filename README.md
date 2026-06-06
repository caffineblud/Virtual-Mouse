# 🖱️ Virtual Mouse

*Control your mouse cursor using hand gestures — no hardware required. Built with MediaPipe, OpenCV, and PyAutoGUI*.

---

## Contents

- [Gestures](#gestures)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Dependencies](#dependencies)
- [Configuration](#configuration)

---

## Gestures

| Gesture | Action |
|---|---|
| ☝️ Index finger tip | Move cursor |
| 🤏 Index + Thumb pinch | Left click |
| 🖖 Middle finger + Thumb pinch | Right click |
| *(assign a gesture)* | Scroll up / down |

> `scroll_up()` and `scroll_down()` are available in `MouseController` — wire them to a gesture of your choice.

---

## Project Structure

```
virtual-mouse/
│
├── main.py                    # Entry point — webcam loop, gesture dispatch
│
├── modules/
│   ├── hand_tracker.py        # MediaPipe hand detection & landmark extraction
│   ├── mouse_controller.py    # Smoothed cursor movement, click & scroll actions
│   └── gestures.py            # Euclidean distance–based gesture detection logic
│
└── requirements.txt           # Python dependencies
```

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/caffineblud/virtual-mouse.git
cd virtual-mouse
```

**2. Create a virtual environment** *(recommended)*

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run**

```bash
python main.py
```

Press `Q` to quit the webcam window.

> **macOS users:** grant camera and accessibility permissions to your terminal emulator under System Settings → Privacy & Security before running.

---

## Dependencies

| Package | Purpose |
|---|---|
| `opencv-python` | Webcam capture and frame rendering |
| `mediapipe` | Hand landmark detection |
| `pyautogui` | Mouse control (move, click, scroll) |
| `numpy` | Coordinate interpolation |

Install all at once:

```bash
pip install -r requirements.txt
```

---

## Configuration

These values can be tuned directly in the source files:

| Parameter | Default | Location | Description |
|---|---|---|---|
| `smoothening` | `5` | `mouse_controller.py` | Cursor lag factor. Higher = smoother but slower. |
| `threshold` | `35` | `gestures.py` | Click detection distance in pixels. Lower = harder to trigger. |
| `click_delay` | `0.4s` | `main.py` | Minimum time between clicks. Prevents accidental double-fires. |
| `detection_conf` | `0.7` | `hand_tracker.py` | MediaPipe hand detection confidence threshold. |
| `tracking_conf` | `0.7` | `hand_tracker.py` | MediaPipe hand tracking confidence threshold. |

---

## How It Works

1. Webcam feed is captured and flipped horizontally via OpenCV.
2. Each frame is passed to `HandTracker`, which uses MediaPipe to detect 21 hand landmarks.
3. The index fingertip (landmark `8`) position is mapped to screen coordinates using `numpy.interp`.
4. Cursor movement is smoothed using exponential interpolation controlled by the `smoothening` factor.
5. `GestureDetector` computes Euclidean distances between fingertips to detect click gestures.
6. A `click_delay` prevents repeated firing while a pinch is held.

---
## Author:
***Yash Kumar Singh***
