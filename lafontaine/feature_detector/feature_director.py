from datetime import timedelta

from lafontaine.feature_detector.feature_result.single_frame_feature_result import SingleFrameFeatureResult
from typing import Optional


class FeatureDirector:

    def __init__(self, genre, max_length: timedelta, all_features):
        self.genre = genre
        self.max_length = max_length
        self.all_features = all_features

    def check_for_all_features(self, frame) -> Optional[SingleFrameFeatureResult]:
        return self._check_for_features(frame)

    def _check_for_features(self, frame) -> Optional[SingleFrameFeatureResult]:
        for f in self.all_features:
            result: SingleFrameFeatureResult = f.check_feature(frame)

            if result.result:
                return result

        return None
