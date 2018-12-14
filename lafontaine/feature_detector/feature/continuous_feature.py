import abc

from lafontaine.feature_detector.feature_result.continuous_frame_result import ContinuousFrameResult


class ContinuousFeature:
    @abc.abstractmethod
    def check_feature(self, frame) -> ContinuousFrameResult:
        pass
