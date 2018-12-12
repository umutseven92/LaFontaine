from moviepy.audio.AudioClip import AudioArrayClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import numpy as np

from lafontaine.parser.frame import Frame
from typing import List
import os


class VideoGenerator:
    def __init__(self, path_to_video):
        self.audio = AudioFileClip(path_to_video)

    def generate_from_scene(self, scene, path, fps):
        if os.path.exists(path):
            os.remove(path)
        self._generate_from_frames(scene.frames, path, fps)

    def _generate_from_frames(self, frames: List[Frame], path, fps):
        images = []

        for f in frames:
            images.append(f.image)

        clip = ImageSequenceClip(images, fps=fps)
        audio_clip = self.audio.subclip(frames[0].timestamp, frames[-1].timestamp)
        new_clip = clip.set_audio(audio_clip)
        new_clip.write_videofile(path)
