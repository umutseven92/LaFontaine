from lafontaine.feature_detector.feature.continuous_feature import ContinuousFeature
from lafontaine.feature_detector.feature_result.continuous_frame_result import ContinuousFrameResult
import numpy as np

from lafontaine.parser.frame import Frame


class FrameDeltaDetector(ContinuousFeature):

    def __init__(self, delta, frame_change_limit, frame_limit, frames):
        self.delta = delta
        self.frames = frames
        self.previous_frame = None
        self.counting = False
        self.candidate_frames = []
        self.frame_limit = frame_limit
        self.count = frame_limit
        self.frame_change_limit = frame_change_limit
        self.frame_change_amount = frame_change_limit
        super().__init__('FrameDeltaDetector')

    def _calculate_delta(self, frame1: Frame, frame2: Frame):
        return np.mean(frame1.image != frame2.image)

    def check_feature(self, frame):
        if self.previous_frame is None:
            self.previous_frame = frame
            return ContinuousFrameResult(False, self.frames, self.feature_id, self.candidate_frames)

        if self.counting:
            self.candidate_frames.append(frame)
            delta = self._calculate_delta(self.previous_frame, frame)

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

        delta = self._calculate_delta(self.previous_frame, frame)

        if delta >= self.delta:
            self.candidate_frames.append(frame)
            self.counting = True
            self.count = self.frame_limit

        self.previous_frame = frame
        return ContinuousFrameResult(False, self.frames, self.feature_id, self.candidate_frames)

