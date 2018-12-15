import abc


class BaseFeature(abc.ABC):
    def __init__(self, feature_id, frames):
        self.feature_id = feature_id
        self.frames = frames
