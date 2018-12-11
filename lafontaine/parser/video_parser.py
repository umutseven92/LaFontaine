from lafontaine.parser.scene import Scene
from lafontaine.parser.frame import Frame
from feature_detector.feature_director import FeatureDirector
from lafontaine.parser.video_stats import VideoStats
from moviepy.editor import VideoFileClip


class VideoParser:
    def __init__(self, video_path):
        self.video = VideoFileClip(video_path)
        self.audio = self.video.audio
        self.duration = self.video.duration
        self.video_stats = VideoStats(self.video.fps, self.video.w, self.video.h)

    def get_scenes(self, feature_director: FeatureDirector):
        scenes = []
        current_scene = None
        countdown = None
        recording = False

        step = 0.1
        for t in range(int(self.duration / step)):
            t = t * step
            if t > self.audio.duration or t > self.duration:
                break

            audio_frame = self.audio.get_frame(t)
            video_frame = self.video.get_frame(t)

            percent = (100 / self.duration) * t
            print(f"Processing frame at {t:.2f}. {percent:.2f}%")

            frame = Frame(video_frame, audio_frame)

            result = feature_director.check_for_all_features(frame)

            if countdown and countdown < 0:
                recording = False
                scenes.append(current_scene)
                current_scene = None
                countdown = None

            if recording:
                current_scene.add_frame(frame)
                countdown -= 1
            else:
                if result and result.result is True:
                    if current_scene is None:
                        current_scene = Scene()
                    recording = True
                    countdown = result.frames
                    current_scene.add_frame(frame)

        if current_scene is not None:
            scenes.append(current_scene)

        return scenes
