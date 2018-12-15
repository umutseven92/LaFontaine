from typing import Optional

import pysrt
from moviepy.editor import VideoFileClip
from pysrt import SubRipFile

from lafontaine.feature_director.feature_director import FeatureDirector
from lafontaine.helpers.frame import Frame
from lafontaine.helpers.scene import Scene
from lafontaine.helpers.video_stats import VideoStats


class VideoParser:
    def __init__(self, video_path, srt_path, downscale):
        self.video = VideoFileClip(video_path)

        if downscale:
            self.video = self.video.resize(height=int(downscale))

        self.audio = self.video.audio
        self.duration = self.video.duration

        if srt_path:
            self.subs: Optional[SubRipFile] = pysrt.open(srt_path, encoding='iso-8859-1')
        else:
            self.subs = None

        self.video_stats = VideoStats(self.video.fps, self.video.w, self.video.h)

    def get_scenes(self, feature_director: FeatureDirector):
        scenes = []
        current_scene = None
        countdown = None
        recording = False

        for t, raw_img in self.video.iter_frames(with_times=True):
            audio_frame = self.audio.get_frame(t)

            percent = (100 / self.duration) * t

            if self.subs:
                sub = self.subs.at(seconds=t)
                frame = Frame(raw_img, audio_frame, t, sub)
            else:
                frame = Frame(raw_img, audio_frame, t)

            result = feature_director.check_for_all_features(frame)

            if result and result.result and hasattr(result, 'candidate_frames') and result.candidate_frames:
                scene = Scene()
                scene.add_frames(result.candidate_frames)
                scenes.append(scene)

                recording = False
                current_scene = None
                countdown = None
            else:
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
                        print(f'Activating {result.feature} for {result.frames} frames.')
                        if current_scene is None:
                            current_scene = Scene()
                        recording = True
                        countdown = result.frames
                        current_scene.add_frame(frame)

            info = f'Processed frame at {t:.2f}. {percent:.2f}%'
            print(info)

        if current_scene is not None:
            scenes.append(current_scene)

        return scenes
