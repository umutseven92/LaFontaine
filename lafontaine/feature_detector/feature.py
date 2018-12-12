import abc
from lafontaine.feature_detector.feature_result import FeatureResult


class Feature(abc.ABC):
    @abc.abstractmethod
    def check_feature(self, frame) -> FeatureResult:
        pass
