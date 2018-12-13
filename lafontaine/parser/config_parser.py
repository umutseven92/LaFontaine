import json
from datetime import timedelta

from feature_detector.feature_director import FeatureDirector
from feature_detector.image.face_recognizer import FaceRecognizer
from feature_detector.sound.sound_peak_detector import SoundPeakDetector
from feature_detector.subtitle.subtitle_density_detector import SubtitleDensityDetector
from feature_detector.subtitle.subtitle_intensity_detector import SubtitleIntensityDetector


class ConfigParser:
    @staticmethod
    def get_director_from_config(config: str) -> FeatureDirector:
        all_features = []

        loaded = json.loads(config)
        features = loaded['features']
        genre = loaded['genre']
        max_length = int(loaded['max_length'])

        for feature in features:
            feature_id = feature['id']

            if feature_id == 'FaceRecognizer':
                face_count = feature['face_count']
                frames = feature['frames']
                all_features.append(FaceRecognizer(face_count, frames))

            elif feature_id == 'SoundPeakDetector':
                audio_threshold = feature['audio_threshold']
                frames = feature['frames']
                all_features.append(SoundPeakDetector(audio_threshold, frames))

            elif feature_id == 'SubtitleDensityDetector':
                char_count = feature['char_count']
                frames = feature['frames']
                all_features.append(SubtitleDensityDetector(char_count, frames))

            elif feature_id == 'SubtitleIntensityDetector':
                char_count = feature['char_count']
                intensity_char = feature['intensity_char']
                frames = feature['frames']
                all_features.append(SubtitleIntensityDetector(intensity_char, char_count, frames))

        director = FeatureDirector(genre, timedelta(seconds=max_length), all_features)
        return director
