from lafontaine.feature_detector.feature import Feature
from lafontaine.feature_detector.feature_result import FeatureResult
import numpy as np

from lafontaine.parser.frame import Frame


class ColorCounter(Feature):
    FEATURE_ID = 'ColorCounter'

    def __init__(self, color_count, frames):
        self.color_count = color_count
        self.frames = frames

    def check_feature(self, frame: Frame):
        unique_colors = np.unique(frame.image.reshape(-1, frame.image.shape[2]), axis=0)
        frame_color_count = len(unique_colors)
        return FeatureResult(frame_color_count >= self.color_count, self.frames, self.FEATURE_ID)
