import abc

from lafontaine.feature_detector.feature.base_feature import BaseFeature
from lafontaine.feature_detector.feature_result.continuous_frame_result import ContinuousFrameResult


class ContinuousFeature(BaseFeature):
    @abc.abstractmethod
    def check_feature(self, frame) -> ContinuousFrameResult:
        pass
