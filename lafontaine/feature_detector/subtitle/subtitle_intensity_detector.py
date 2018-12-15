from lafontaine.feature_detector.feature_result.single_frame_feature_result import SingleFrameFeatureResult
from lafontaine.feature_detector.feature.single_frame_feature import SingleFrameFeature
from lafontaine.parser.frame import Frame


class SubtitleIntensityDetector(SingleFrameFeature):

    def __init__(self, intensity_char, char_count, frames):
        self.char_count = char_count
        self.intensity_char = intensity_char
        super().__init__('SubtitleIntensityDetector', frames)

    def check_feature(self, frame: Frame):
        if frame.sub:
            sub_text = frame.sub.text
            how_many = sub_text.count(self.intensity_char)
            return SingleFrameFeatureResult(how_many >= self.char_count, self.frames, self.feature_id)
        return SingleFrameFeatureResult(False, self.frames, self.feature_id)

