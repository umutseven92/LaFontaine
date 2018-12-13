import face_recognition
from lafontaine.feature_detector.feature import Feature
from lafontaine.feature_detector.feature_result import FeatureResult


class FaceRecognizer(Feature):
    FEATURE_ID = 'FaceRecognizer'

    def __init__(self, face_count, frames):
        self.face_count = face_count
        self.frames = frames

    def check_feature(self, frame):
        face_locations = face_recognition.face_locations(frame.image)
        return FeatureResult(len(face_locations) >= self.face_count, self.frames, self.FEATURE_ID)
