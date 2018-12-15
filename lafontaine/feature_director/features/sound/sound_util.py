import numpy as np


class SoundUtil:
    @staticmethod
    def get_volume_of_frame(frame) -> bool:
        return np.sqrt((frame.audio * 1.0) ** 2).mean()
