from unittest import TestCase, mock

import numpy as np

from lafontaine.feature_director.features.image.frame_delta_detector import FrameDeltaDetector
from lafontaine.feature_director.features.image.color_counter import ColorCounter


class TestFeatureDirector(TestCase):
    def test_can_get_unique_colors(self):
        with mock.patch('lafontaine.helpers.frame.Frame') as mock_frame:
            mock_frame.image = np.array(
                [[[2, 4, 2], [5, 5, 1], [9, 2, 1]],
                 [[2, 4, 2], [5, 5, 1], [9, 2, 2]]]
            )

            unique_colors = ColorCounter.get_unique_colors(mock_frame)

            self.assertEqual(len(unique_colors), 4)

    def test_can_calculate_frame_image_delta(self):
        with mock.patch('lafontaine.helpers.frame.Frame') as mock_frame1, mock.patch('lafontaine.helpers.frame.Frame') as mock_frame2:

            mock_frame1.image = np.array(
                [[[2, 4, 2], [5, 5, 1], [9, 2, 1]],
                 [[2, 4, 2], [5, 5, 1], [9, 2, 2]]]
            )

            mock_frame2.image = np.array(
                [[[2, 4, 2], [5, 5, 1], [10, 2, 1]],
                 [[2, 4, 2], [5, 5, 1], [9, 2, 2]]]
            )

            delta = FrameDeltaDetector.calculate_delta(mock_frame1, mock_frame2)

            self.assertEqual(delta, 0.05555555555555555)
