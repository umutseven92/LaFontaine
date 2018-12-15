from lafontaine.feature_detector.feature.single_frame_feature import SingleFrameFeature
from lafontaine.feature_detector.feature_result.single_frame_feature_result import SingleFrameFeatureResult
import numpy as np

from lafontaine.parser.frame import Frame


class ColorCounter(SingleFrameFeature):

    def __init__(self, color_count, frames):
        self.color_count = color_count
        self.frames = frames
        super().__init__('ColorCounter')

    def check_feature(self, frame: Frame):
        unique_colors = np.unique(frame.image.reshape(-1, frame.image.shape[2]), axis=0)
        frame_color_count = len(unique_colors)
        return SingleFrameFeatureResult(frame_color_count >= self.color_count, self.frames, self.feature_id)
