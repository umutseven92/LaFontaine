import abc

from feature_detector.feature.base_feature import BaseFeature
from lafontaine.feature_detector.feature_result.single_frame_feature_result import SingleFrameFeatureResult


class SingleFrameFeature(BaseFeature):
    @abc.abstractmethod
    def check_feature(self, frame) -> SingleFrameFeatureResult:
        pass
