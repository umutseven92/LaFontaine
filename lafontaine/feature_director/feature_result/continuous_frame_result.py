from typing import List

from lafontaine.helpers.feature_types import FeatureType
from lafontaine.feature_director.feature_result.base_feature_result import BaseFeatureResult
from lafontaine.helpers.frame import Frame


class ContinuousFrameResult(BaseFeatureResult):
    def __init__(self, result: bool, frames: int, feature: str, candidate_frames: List[Frame]):
        super().__init__(result, frames, feature, FeatureType.ContinuousFrameFeature)
        self.candidate_frames = candidate_frames
