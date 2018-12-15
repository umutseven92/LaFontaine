from feature_detector.feature.continuous_feature import ContinuousFeature
from feature_detector.feature_result.continuous_frame_result import ContinuousFrameResult


class HighVolumeDetector(ContinuousFeature):

    def check_feature(self, frame) -> ContinuousFrameResult:
        pass