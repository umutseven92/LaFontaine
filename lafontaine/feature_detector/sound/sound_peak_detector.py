from feature_detector.feature import Feature

"""
ffmpeg -i test.mp4 -ab 160k -ac 2 -ar 44100 -vn audio.wav
ffmpeg -i test.mp3 -ss 00:00:00 -to 00:00:30 -c copy -y temp.mp3
"""
class SoundPeakDetector(Feature):
    def check_feature(self, frame):
        pass