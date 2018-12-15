from typing import List

from lafontaine.feature_detector.feature_result.base_feature_result import BaseFeatureResult
from lafontaine.parser.frame import Frame


class ContinuousFrameResult(BaseFeatureResult):
    def __init__(self, result: bool, frames: int, feature: str, candidate_frames: List[Frame]):
        super().__init__(result, frames, feature)
        self.candidate_frames = candidate_frames
