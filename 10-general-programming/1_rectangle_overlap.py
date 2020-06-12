# Rectangle overlap
# Write a function to find the rectangular intersection of two given rectangles.
# Each side is parallel with either the x-axis or the y-axis. They are defined
# as dictionaries like this:
#
# my_rectangle = {
#    # Coordinates of bottom-left corner
#    'left_x'   : 1,
#    'bottom_y' : 1,
#
#    # Width and height
#    'width'    : 6,
#    'height'   : 3,
# }
#
# Your output rectangle should use this format as well.
#
# BONUS
# 1. What if we had a list of rectangles and wanted to find all the rectangular
# overlaps between all possible pairs of two rectangles within the list? Note
# that we'd be returning a list of rectangles.
#
# 2. What if we had a list of rectangles and wanted to find the overlap between
# all of them, if there was one? Note that we'd be returning a single rectangle.

from typing import Dict, Tuple
import unittest


def rectangle_overlap(a: Dict[str, int], b: Dict[str, int]) -> Dict[str, int]:
    labels = ["left_x", "bottom_y", "width", "height"]
    left_x, width = overlap(a["left_x"], a["width"], b["left_x"], b["width"])
    bottom_y, height = overlap(
        a["bottom_y"], a["height"], b["bottom_y"], b["height"])
    if not width or not height:
        return None
    else:
        return dict(zip(labels, [left_x, bottom_y, width, height]))


def overlap(start1: int, length1: int, start2: int, length2: int) -> Tuple[int, int]:
    """Returns start and length of overlap"""
    start = max(start1, start2)
    end = min(start1+length1, start2+length2)
    length = end-start
    return (start, length) if length > 0 else (None, None)


class TestRectangleOverlap(unittest.TestCase):
    def test_rectangle_overlap(self):
        labels = ["left_x", "bottom_y", "width", "height"]
        tests = [
            # [left_x, bottom_y, width, height] for a, b, expected
            [[1, 1, 6, 3], [5, 2, 3, 6], [5, 2, 2, 2]],
            [[1, 2, 6, 5], [3, 3, 2, 1], [3, 3, 2, 1]],
            [[1, 1, 3, 4], [9, 6, 7, 8], None],
            [[1, 1, 3, 4], [4, 2, 7, 8], None],
        ]
        for a, b, expected in tests:
            a = dict(zip(labels, a))
            b = dict(zip(labels, b))
            with self.subTest(a=a, b=b):
                if expected:
                    expected = dict(zip(labels, expected))
                    self.assertEqual(rectangle_overlap(a, b), expected)
                else:
                    self.assertIsNone(rectangle_overlap(a, b))


if __name__ == "__main__":
    unittest.main()
