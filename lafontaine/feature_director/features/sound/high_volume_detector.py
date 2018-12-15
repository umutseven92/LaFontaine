from lafontaine.feature_director.features.sound.sound_util import SoundUtil
from lafontaine.feature_director.feature.continuous_feature import ContinuousFeature
from lafontaine.feature_director.feature_result.continuous_frame_result import ContinuousFrameResult


class HighVolumeDetector(ContinuousFeature):
    def __init__(self, volume, frame_limit, frames):
        self.volume_limit = volume
        self.counting = False
        self.candidate_frames = []
        self.frame_limit = frame_limit
        self.count = frame_limit
        super().__init__('HighVolumeDetector', frames)

    def check_feature(self, frame) -> ContinuousFrameResult:
        frame_volume = SoundUtil.get_volume_of_frame(frame)
        if self.counting:
            if frame_volume >= self.volume_limit:
                if self.count <= 0:
                    self.counting = False
                    frames = self.candidate_frames
                    self.candidate_frames = []
                    return ContinuousFrameResult(True, self.frames, self.feature_id, frames)

                self.candidate_frames.append(frame)
                self.count -= 1

            else:
                self.counting = False
                self.candidate_frames = []
                self.count = self.frame_limit
                return ContinuousFrameResult(False, self.frames, self.feature_id, self.candidate_frames)

        if frame_volume >= self.volume_limit:
            self.candidate_frames.append(frame)
            self.counting = True
            self.count = self.frame_limit

        return ContinuousFrameResult(False, self.frames, self.feature_id, self.candidate_frames)
