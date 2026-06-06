import math


class GestureDetector:

    @staticmethod
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        return math.hypot(x2 - x1, y2 - y1)

    @staticmethod
    def is_left_click(index_pos, thumb_pos, threshold=35):
        distance = GestureDetector.distance(
            index_pos,
            thumb_pos
        )

        return distance < threshold

    @staticmethod
    def is_right_click(middle_pos, thumb_pos, threshold=35):
        distance = GestureDetector.distance(
            middle_pos,
            thumb_pos
        )

        return distance < threshold