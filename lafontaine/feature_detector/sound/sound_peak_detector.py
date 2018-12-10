from feature_detector.feature import Feature
from parser.frame import Frame
from moviepy.editor import AudioFileClip
import numpy


class SoundPeakDetector(Feature):
    def __init__(self, path_to_video):
        audioclip = AudioFileClip(path_to_video)
        audioclip.max_volume()
        self.average_level = self._get_average_sound_level(audioclip.to_soundarray())

    def _get_average_sound_level(self, sound_array: numpy.ndarray):
        mean = sound_array.mean()
        return mean

    def check_feature(self, frame: Frame):
        frame_mean = frame.audio.mean()
        if frame_mean > self.average_level + 0.2:
            return True
        return False
