from lafontaine.feature_detector.feature_result import FeatureResult
from typing import Optional


class FeatureDirector:

    def __init__(self, all_features):
        self.all_features = all_features

    def check_for_all_features(self, frame) -> Optional[FeatureResult]:
        return self._check_for_features(frame)

    def _check_for_features(self, frame) -> Optional[FeatureResult]:
        for f in self.all_features:
            result: FeatureResult = f.check_feature(frame)

            if result.result:
                return result

        return None
