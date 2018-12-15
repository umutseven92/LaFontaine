import numpy as np

from lafontaine.feature_director.feature.single_frame_feature import SingleFrameFeature
from lafontaine.feature_director.feature_result.single_frame_feature_result import SingleFrameFeatureResult
from lafontaine.helpers.frame import Frame


class ColorCounter(SingleFrameFeature):

    def __init__(self, color_count, frames):
        self.color_count = color_count
        super().__init__('ColorCounter', frames)

    @staticmethod
    def get_unique_colors(frame):
        return np.unique(frame.image.reshape(-1, frame.image.shape[2]), axis=0)

    def check_feature(self, frame: Frame):
        unique_colors = self.get_unique_colors(frame)
        frame_color_count = len(unique_colors)
        return SingleFrameFeatureResult(frame_color_count >= self.color_count, self.frames, self.feature_id)
