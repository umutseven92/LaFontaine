from feature_detector.image.face_recognizer import FaceRecognizer
from feature_detector.sound.sound_peak_detector import SoundPeakDetector


class FeatureDirector:

    def __init__(self, image_features=None, sound_features=None, subtitle_features=None):
        if subtitle_features is None:
            subtitle_features = []
        if sound_features is None:
            sound_features = []
        if image_features is None:
            image_features = []

        self.__image_features = image_features
        self.__sound_features = sound_features
        self.__subtitle_features = subtitle_features

    @classmethod
    def default_features(cls):
        return cls([FaceRecognizer(2)], [SoundPeakDetector()], [])

    def check_for_all_features(self, frame):
        image_features = self.check_for_image_features(frame)

        if image_features:
            return True

        audio_features = self.check_for_audio_features(frame)

        if audio_features:
            return True

        subtitle_features = self.check_for_subtitle_features(frame)

        if subtitle_features:
            return True

        return False

    def check_for_image_features(self, frame):
        return self.__check_for_features(frame, self.__image_features)

    def check_for_audio_features(self, frame):
        return self.__check_for_features(frame, self.__sound_features)

    def check_for_subtitle_features(self, frame):
        return self.__check_for_features(frame, self.__subtitle_features)

    def __check_for_features(self, frame, feature_list):
        for f in feature_list:
            result = f.check_feature(frame)

            if result:
                return True

        return False
