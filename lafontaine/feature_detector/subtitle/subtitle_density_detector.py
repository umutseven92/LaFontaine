from feature_detector.feature_result import FeatureResult
from lafontaine.feature_detector.feature import Feature
from lafontaine.parser.frame import Frame


class SubtitleDensityDetector(Feature):
    RESULT_FRAMES = 100
    FEATURE_ID = 'SubtitleDensityDetector'

    def __init__(self, char_count):
        self.char_count = char_count

    def check_feature(self, frame: Frame):
        sub_length = len(frame.sub.text)
        return FeatureResult(sub_length >= self.char_count, self.RESULT_FRAMES, self.FEATURE_ID)
