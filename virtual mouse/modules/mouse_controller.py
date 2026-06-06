import pyautogui
import numpy as np

pyautogui.FAILSAFE = False


class MouseController:

    def __init__(self, smoothening=5):
        self.screen_w, self.screen_h = pyautogui.size()

        self.prev_x = 0
        self.prev_y = 0

        self.smoothening = smoothening

    def move(self, x, y, frame_w, frame_h):

        screen_x = np.interp(
            x,
            (0, frame_w),
            (0, self.screen_w)
        )

        screen_y = np.interp(
            y,
            (0, frame_h),
            (0, self.screen_h)
        )

        curr_x = self.prev_x + (
            screen_x - self.prev_x
        ) / self.smoothening

        curr_y = self.prev_y + (
            screen_y - self.prev_y
        ) / self.smoothening

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x = curr_x
        self.prev_y = curr_y

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.rightClick()

    def scroll_up(self):
        pyautogui.scroll(100)

    def scroll_down(self):
        pyautogui.scroll(-100)