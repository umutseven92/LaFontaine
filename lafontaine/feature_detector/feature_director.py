from lafontaine.feature_detector.feature_result import FeatureResult
from typing import Optional

from parser.frame import Frame


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

    def check_for_all_features(self, frame) -> Optional[FeatureResult]:
        image_features = self.check_for_image_features(frame)

        if image_features:
            return image_features

        audio_features = self.check_for_audio_features(frame)

        if audio_features:
            return audio_features

        subtitle_features = self.check_for_subtitle_features(frame)

        if subtitle_features:
            return subtitle_features

        return None

    def check_for_image_features(self, frame):
        return self._check_for_features(frame, self.__image_features)

    def check_for_audio_features(self, frame):
        return self._check_for_features(frame, self.__sound_features)

    def check_for_subtitle_features(self, frame: Frame):
        if frame.sub:
            return self._check_for_features(frame, self.__subtitle_features)
        return None

    def _check_for_features(self, frame, feature_list) -> Optional[FeatureResult]:
        for f in feature_list:
            result: FeatureResult = f.check_feature(frame)

            if result.result:
                return result

        return None
