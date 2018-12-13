from lafontaine.feature_detector.feature_result import FeatureResult
from lafontaine.feature_detector.feature import Feature
from lafontaine.parser.frame import Frame


class SubtitleConversationCount(Feature):
    FEATURE_ID = 'SubtitleConversationCount'

    def __init__(self, conversation_count, frames):
        self.conversation_count = conversation_count
        self.frames = frames

    def check_feature(self, frame: Frame):
        if frame.sub:
            sub_text = frame.sub.text
            how_many = sub_text.count("-")
            return FeatureResult(how_many >= self.conversation_count, self.frames, self.FEATURE_ID)
        return FeatureResult(False, self.frames, self.FEATURE_ID)

