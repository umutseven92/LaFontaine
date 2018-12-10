from lafontaine.parser.scene import Scene
from lafontaine.parser.frame import Frame
from lafontaine.parser.video_stats import VideoStats
from moviepy.editor import *


class VideoParser:
    def __init__(self, video_path):
        self.video = VideoFileClip(video_path)
        self.audio = self.video.audio
        self.duration = self.video.duration
        self.video_stats = VideoStats(self.video.fps, self.video.w, self.video.h)

    def get_scenes(self, feature_director):
        scenes = []
        current_scene = None

        step = 0.1
        for t in range(int(self.duration / step)):
            t = t * step
            if t > self.audio.duration or t > self.duration:
                break

            audio_frame = self.audio.get_frame(t)
            video_frame = self.video.get_frame(t)

            percent = (100/self.duration) * t
            print(f"Processing frame at {t}. {percent:.2f}%")

            frame = Frame(video_frame, audio_frame, 0)
            result = feature_director.check_for_image_features(frame)

            if result:
                if current_scene is None:
                    current_scene = Scene()

                current_scene.add_frame(frame)
            else:
                if current_scene is not None:
                    scenes.append(current_scene)
                    current_scene = None

        if current_scene is not None:
            scenes.append(current_scene)

        return scenes
