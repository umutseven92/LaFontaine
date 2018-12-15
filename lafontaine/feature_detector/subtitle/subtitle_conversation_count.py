from lafontaine.feature_detector.feature_result.single_frame_feature_result import SingleFrameFeatureResult
from lafontaine.feature_detector.feature.single_frame_feature import SingleFrameFeature
from lafontaine.parser.frame import Frame


class SubtitleConversationCount(SingleFrameFeature):

    def __init__(self, conversation_count, frames):
        self.conversation_count = conversation_count
        super().__init__('SubtitleConversationCount', frames)

    def check_feature(self, frame: Frame):
        if frame.sub:
            sub_text = frame.sub.text
            how_many = sub_text.count("-")
            return SingleFrameFeatureResult(how_many >= self.conversation_count, self.frames, self.feature_id)
        return SingleFrameFeatureResult(False, self.frames, self.feature_id)

