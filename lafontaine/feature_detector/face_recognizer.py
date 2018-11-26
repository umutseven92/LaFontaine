import face_recognition


class FaceRecognizer:
    def check_for_faces(self, image):
        face_locations = face_recognition.face_locations(image)
        return face_locations
