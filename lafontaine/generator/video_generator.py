from datetime import timedelta

from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import TextClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.editor import concatenate_videoclips
from lafontaine.parser.frame import Frame
from typing import List
import os

from lafontaine.parser.scene import Scene


class VideoGenerator:
    def __init__(self, path_to_video, max_length: timedelta, out_path, title):
        self.audio = AudioFileClip(path_to_video)
        self.max_length = max_length
        self.out_path = out_path

        self.title = title

    def generate_from_scenes(self, scenes: List[Scene], fps):
        clips = []
        total_duration = 0
        for scene in scenes:
            clip = self._generate_from_scene(scene, fps)
            total_duration += clip.duration

            if total_duration > self.max_length.seconds:
                break

            clips.append(clip)

        if clips:
            if self.title:
                title_clip = TextClip(self.title, color='white', bg_color='black', fontsize=60, size=(clips[0].w, clips[0].h)).set_duration(5)
                clips.append(title_clip)

            trailer = concatenate_videoclips(clips)

            if os.path.exists(self.out_path):
                os.remove(self.out_path)

            trailer.write_videofile(self.out_path)

    def _generate_from_scene(self, scene, fps) -> ImageSequenceClip:
        return self._generate_from_frames(scene.frames, fps)

    def _generate_from_frames(self, frames: List[Frame], fps):
        images = []

        for f in frames:
            images.append(f.image)

        clip = ImageSequenceClip(images, fps=fps)
        audio_clip = self.audio.subclip(frames[0].timestamp, frames[-1].timestamp)
        new_clip = clip.set_audio(audio_clip)

        return new_clip
