import abc


class BaseFeatureResult(abc.ABC):
    def __init__(self, result: bool, frames: int, feature: str):
        self.result = result
        self.frames = frames
        self.feature = feature
