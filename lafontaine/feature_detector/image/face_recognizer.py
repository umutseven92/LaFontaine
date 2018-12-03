import face_recognition
from feature_detector.feature import Feature


class FaceRecognizer(Feature):
    def __check_for_faces(self, image):
        face_locations = face_recognition.face_locations(image)
        return face_locations

    def check_feature(self, frame):
        faces = self.__check_for_faces(frame.image)
        return len(faces) > 0
