from lafontaine.feature_director.feature.single_frame_feature import SingleFrameFeature
from lafontaine.feature_director.feature_result.single_frame_feature_result import SingleFrameFeatureResult
from lafontaine.helpers.frame import Frame


class SubtitleDensityDetector(SingleFrameFeature):

    def __init__(self, char_count, frames):
        self.char_count = char_count
        super().__init__('SubtitleDensityDetector', frames)

    def check_feature(self, frame: Frame):
        if frame.sub:
            sub_length = len(frame.sub.text)
            return SingleFrameFeatureResult(sub_length >= self.char_count, self.frames, self.feature_id)
        return SingleFrameFeatureResult(False, self.frames, self.feature_id)
