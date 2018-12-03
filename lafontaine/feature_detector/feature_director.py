from feature_detector.image.face_recognizer import FaceRecognizer


class FeatureDirector:

    def __init__(self):
        self.__image_features = [FaceRecognizer()]
        self.__sound_features = []
        self.__subtitle_features = []

    def check_for_image_features(self, frame):
        return self.__check_for_features(frame, self.__image_features)

    def check_for_sound_features(self, frame):
        return self.__check_for_features(frame, self.__sound_features)

    def check_for_subtitle_features(self, frame):
        return self.__check_for_features(frame, self.__subtitle_features)

    def __check_for_features(self, frame, feature_list):
        for f in feature_list:
            result = f.check_feature(frame)

            if result:
                return True

        return False
