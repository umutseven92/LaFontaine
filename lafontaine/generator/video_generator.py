from moviepy.audio.AudioClip import AudioArrayClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import numpy as np

from parser.frame import Frame
from typing import List
import os


class VideoGenerator:

    def generate_from_scene(self, scene, path, fps):
        if os.path.exists(path):
            os.remove(path)
        self._generate_from_frames(scene.frames, path, fps)

    def _generate_from_frames(self, frames: List[Frame], path, fps):
        images = []
        audio = []
        rate = 44100

        for f in frames:
            images.append(f.image)
            audio.append(f.audio)

        clip = ImageSequenceClip(images, fps=fps)
        audio_array = np.asarray(audio)

        audio_clip = AudioArrayClip(audio_array, fps=rate)
        #audio_clip.write_audiofile('out/test.mp3')
        #clip.set_audio(audio_clip)
        #clip.write_videofile(path)

        #data_stereo = np.random.uniform(-1, 1, (44100*4,2))
        data_stereo = np.random.uniform(-1, 1, (100, 2))

        audio_stereo = AudioArrayClip(data_stereo, fps=len(data_stereo)/4)
        audio_stereo.write_audiofile('out/test.mp3')
