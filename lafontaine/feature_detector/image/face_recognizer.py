import face_recognition
from lafontaine.feature_detector.feature import Feature
from lafontaine.feature_detector.feature_result import FeatureResult


class FaceRecognizer(Feature):
    RESULT_FRAMES = 100
    FEATURE_ID = 'FaceRecognizer'

    def __init__(self, face_count):
        self.face_count = face_count

    def check_feature(self, frame):
        face_locations = face_recognition.face_locations(frame.image)
        return FeatureResult(len(face_locations) >= self.face_count, self.RESULT_FRAMES, self.FEATURE_ID)
