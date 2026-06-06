import cv2
import mediapipe as mp


class HandTracker:
    def __init__(
        self,
        mode=False,
        max_hands=1,
        detection_conf=0.7,
        tracking_conf=0.7
    ):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_conf = detection_conf
        self.tracking_conf = tracking_conf

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_conf,
            min_tracking_confidence=self.tracking_conf
        )

        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame,
                    hand,
                    self.mp_hands.HAND_CONNECTIONS
                )

        return frame

    def find_position(self, frame):
        landmarks = []

        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]

            h, w, _ = frame.shape

            for idx, lm in enumerate(hand.landmark):
                cx = int(lm.x * w)
                cy = int(lm.y * h)

                landmarks.append((idx, cx, cy))

        return landmarks