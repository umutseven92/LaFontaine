from feature_detector.feature_result import FeatureResult
from lafontaine.feature_detector.feature import Feature
from lafontaine.parser.frame import Frame


class SubtitleDensityDetector(Feature):
    FEATURE_ID = 'SubtitleDensityDetector'

    def __init__(self, char_count, frames):
        self.char_count = char_count
        self.frames = frames

    def check_feature(self, frame: Frame):
        if frame.sub:
            sub_length = len(frame.sub.text)
            return FeatureResult(sub_length >= self.char_count, self.frames, self.FEATURE_ID)
        return FeatureResult(False, self.frames, self.FEATURE_ID)
