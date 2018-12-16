from lafontaine.helpers.feature_types import FeatureType
from lafontaine.feature_director.feature_result.base_feature_result import BaseFeatureResult


class SingleFrameFeatureResult(BaseFeatureResult):
    def __init__(self, result: bool, frames: int, feature: str):
        super().__init__(result, frames, feature, FeatureType.SingleFrameFeature)
