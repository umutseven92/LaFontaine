import face_recognition
from feature_detector.feature import Feature


class FaceRecognizer(Feature):
    def __init__(self, face_count):
        self.face_count = face_count

    def check_feature(self, frame):
        face_locations = face_recognition.face_locations(frame.image)
        return len(face_locations) >= self.face_count
