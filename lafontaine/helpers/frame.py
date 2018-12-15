from pysrt import SubRipItem


class Frame:
    def __init__(self, image, audio, timestamp, sub: SubRipItem = None):
        self.image = image
        self.audio = audio
        self.timestamp = timestamp
        self.sub = sub
