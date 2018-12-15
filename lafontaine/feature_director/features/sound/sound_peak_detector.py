from lafontaine.feature_director.features.sound.sound_util import SoundUtil
from lafontaine.feature_director.feature.single_frame_feature import SingleFrameFeature
from lafontaine.feature_director.feature_result.single_frame_feature_result import SingleFrameFeatureResult
from lafontaine.helpers.frame import Frame


class SoundPeakDetector(SingleFrameFeature):

    def __init__(self, audio_threshold, frames):
        self.audio_threshold = audio_threshold
        super().__init__('SoundPeakDetector', frames)

    def check_feature(self, frame: Frame):
        frame_volume = SoundUtil.get_volume_of_frame(frame)

        # We have to do this because numpy bool_ is True will return false
        if frame_volume >= self.audio_threshold:
            return SingleFrameFeatureResult(True, self.frames, self.feature_id)
        else:
            return SingleFrameFeatureResult(False, self.frames, self.feature_id)
