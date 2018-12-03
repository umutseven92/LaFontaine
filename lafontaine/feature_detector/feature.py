import abc


class Feature(abc.ABC):
    @abc.abstractmethod
    def check_feature(self, frame):
        pass
