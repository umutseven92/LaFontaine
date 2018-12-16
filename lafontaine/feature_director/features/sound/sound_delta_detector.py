import numpy as np

from lafontaine.helpers.frame import Frame
from lafontaine.feature_director.feature.continuous_feature import ContinuousFeature
from lafontaine.feature_director.feature_result.continuous_frame_result import ContinuousFrameResult


class SoundDeltaDetector(ContinuousFeature):

    def __init__(self, delta, frame_change_limit, frame_limit, frames):
        self.delta = delta
        self.previous_frame = None
        self.counting = False
        self.candidate_frames = []
        self.frame_limit = frame_limit
        self.count = frame_limit
        self.frame_change_limit = frame_change_limit
        self.frame_change_amount = frame_change_limit
        super().__init__('SoundDeltaDetector', frames)

    @staticmethod
    def calculate_delta(frame1: Frame, frame2: Frame):
        return np.mean(frame1.audio != frame2.audio)

    def check_feature(self, frame):
        if self.previous_frame is None:
            self.previous_frame = frame
            return ContinuousFrameResult(False, self.frames, self.feature_id, self.candidate_frames)

        if self.counting:
            self.candidate_frames.append(frame)
            delta = self.calculate_delta(self.previous_frame, frame)

            if delta >= self.delta:
                self.frame_change_amount -= 1

                if self.frame_change_amount <= 0:
                    self.frame_change_amount = self.frame_change_limit
                    self.counting = False
                    frames = self.candidate_frames
                    self.candidate_frames = []
                    return ContinuousFrameResult(True, self.frames, self.feature_id, frames)

            self.count -= 1

            if self.count <= 0:
                self.counting = False
                self.candidate_frames = []

            self.previous_frame = frame
            return ContinuousFrameResult(False, self.frames, self.feature_id, self.candidate_frames)

        delta = self.calculate_delta(self.previous_frame, frame)

        if delta >= self.delta:
            self.candidate_frames.append(frame)
            self.counting = True
            self.count = self.frame_limit

        self.previous_frame = frame
        return ContinuousFrameResult(False, self.frames, self.feature_id, self.candidate_frames)
