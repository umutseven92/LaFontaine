import abc


class BaseFeature(abc.ABC):

    def __init__(self, feature_id):
        self.feature_id = feature_id
