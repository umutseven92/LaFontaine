from lafontaine.feature_detector.feature.single_frame_feature import SingleFrameFeature
from lafontaine.feature_detector.feature_result.single_frame_feature_result import SingleFrameFeatureResult
from lafontaine.parser.frame import Frame
import numpy


class SoundPeakDetector(SingleFrameFeature):

    def __init__(self, audio_threshold, frames):
        self.audio_threshold = audio_threshold
        self.frames = frames
        super().__init__('SoundPeakDetector')

    def check_feature(self, frame: Frame):
        frame_mean = numpy.sqrt((frame.audio*1.0)**2).mean()
        result = frame_mean > self.audio_threshold
        if result:  # We have to do this because numpy bool_ is True will return false
            return SingleFrameFeatureResult(True, self.frames, self.feature_id)
        else:
            return SingleFrameFeatureResult(False, self.frames, self.feature_id)

