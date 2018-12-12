from feature_detector.feature_result import FeatureResult
from lafontaine.feature_detector.feature import Feature
from lafontaine.parser.frame import Frame


class SubtitleIntensityDetector(Feature):
    RESULT_FRAMES = 100
    FEATURE_ID = 'SubtitleIntensityDetector'

    def __init__(self, intensity_char, char_count):
        self.char_count = char_count
        self.intensity_char = intensity_char

    def check_feature(self, frame: Frame):
        sub_text = frame.sub.text
        how_many = sub_text.count(self.intensity_char)
        return FeatureResult(how_many >= self.char_count, self.RESULT_FRAMES, self.FEATURE_ID)
