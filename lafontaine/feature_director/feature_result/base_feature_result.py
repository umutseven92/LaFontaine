import abc

from lafontaine.helpers.feature_types import FeatureType


class BaseFeatureResult(abc.ABC):
    def __init__(self, result: bool, frames: int, feature: str, feature_type: FeatureType):
        self.result = result
        self.frames = frames
        self.feature = feature
        self.feature_type = feature_type
