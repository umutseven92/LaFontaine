import face_recognition
from lafontaine.feature_detector.feature.single_frame_feature import SingleFrameFeature
from lafontaine.feature_detector.feature_result.single_frame_feature_result import SingleFrameFeatureResult


class FaceRecognizer(SingleFrameFeature):

    def __init__(self, face_count, frames):
        self.face_count = face_count
        super().__init__('FaceRecognizer', frames)

    def check_feature(self, frame):
        face_locations = face_recognition.face_locations(frame.image)
        return SingleFrameFeatureResult(len(face_locations) >= self.face_count, self.frames, self.feature_id)
