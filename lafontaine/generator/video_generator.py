from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

from parser.frame import Frame
from typing import List


class VideoGenerator:

    def generate_from_scene(self, scene, path, fps):
        self._generate_from_frames(scene.frames, path, fps)

    def _generate_from_frames(self, frames: List[Frame], path, fps):
        images = []

        for f in frames:
            images.append(f.image)

        clip = ImageSequenceClip(images, fps=fps)

        clip.write_videofile(path)
