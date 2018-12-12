from feature_detector.feature import Feature
from feature_detector.feature_result import FeatureResult
from parser.frame import Frame
from moviepy.editor import AudioFileClip
import numpy


class SoundPeakDetector(Feature):
    RESULT_FRAMES = 100
    FEATURE_ID = 'SoundPeakDetector'

    def __init__(self, path_to_video):
        audioclip = AudioFileClip(path_to_video)
        self.average_level = self._get_average_sound_level(audioclip.to_soundarray())

    def _get_average_sound_level(self, sound_array: numpy.ndarray):
        mean = numpy.sqrt((sound_array*1.0)**2).mean()
        return mean

    def check_feature(self, frame: Frame):
        frame_mean = numpy.sqrt((frame.audio*1.0)**2).mean()
        result = frame_mean > 0.25
        if result:  # We have to do this because numpy bool_ is True will return false
            return FeatureResult(True, self.RESULT_FRAMES, self.FEATURE_ID)
        else:
            return FeatureResult(False, self.RESULT_FRAMES, self.FEATURE_ID)

