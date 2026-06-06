import cv2
import time

from modules.hand_tracker import HandTracker
from modules.mouse_controller import MouseController
from modules.gestures import GestureDetector

tracker = HandTracker()
mouse = MouseController()

cap = cv2.VideoCapture(0)

p_time = 0

click_delay = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    frame = tracker.find_hands(frame)

    landmarks = tracker.find_position(frame)

    frame_h, frame_w, _ = frame.shape

    if landmarks:

        index_tip = landmarks[8][1:]
        thumb_tip = landmarks[4][1:]
        middle_tip = landmarks[12][1:]

        x, y = index_tip

        mouse.move(
            x,
            y,
            frame_w,
            frame_h
        )

        cv2.circle(frame, index_tip, 10, (255, 0, 255), -1)
        cv2.circle(frame, thumb_tip, 10, (0, 255, 0), -1)

        current_time = time.time()

        if current_time - click_delay > 0.4:

            if GestureDetector.is_left_click(
                index_tip,
                thumb_tip
            ):
                mouse.left_click()
                click_delay = current_time

            elif GestureDetector.is_right_click(
                middle_tip,
                thumb_tip
            ):
                mouse.right_click()
                click_delay = current_time

    c_time = time.time()

    fps = 1 / (c_time - p_time) if c_time != p_time else 0

    p_time = c_time

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()