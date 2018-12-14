from lafontaine.feature_detector.feature_result.feature_result import FeatureResult
from lafontaine.feature_detector.feature.feature import Feature
from lafontaine.parser.frame import Frame


class SubtitleIntensityDetector(Feature):
    FEATURE_ID = 'SubtitleIntensityDetector'

    def __init__(self, intensity_char, char_count, frames):
        self.char_count = char_count
        self.intensity_char = intensity_char
        self.frames = frames

    def check_feature(self, frame: Frame):
        if frame.sub:
            sub_text = frame.sub.text
            how_many = sub_text.count(self.intensity_char)
            return FeatureResult(how_many >= self.char_count, self.frames, self.FEATURE_ID)
        return FeatureResult(False, self.frames, self.FEATURE_ID)

