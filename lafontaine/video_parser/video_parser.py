import cv2
from lafontaine.video_parser.scene import Scene
from lafontaine.video_parser.frame import Frame


class VideoParser:
    def __init__(self, video, start, end):
        self.video = video
        self.start = start
        self.video.set(cv2.CAP_PROP_POS_FRAMES, start)
        self.end = end

    def parse_frames(self):
        count = self.start
        while count < self.end:
            count += 1
            success, image = self.video.read()
            if success:
                yield Frame(image, count)

    def parse_scenes(self, feature_director, frame_count):
        scenes = []
        current_scene = None

        for frame in self.parse_frames():
            result = feature_director.check_for_image_features(frame)
            if result:
                if current_scene is None:
                    current_scene = Scene()

                current_scene.add_frame(frame)
            else:
                if current_scene is not None:
                    scenes.append(current_scene)
                    current_scene = None

            percent = (frame.count * 100) / frame_count
            print(f'Processed frame {frame.count} of {frame_count}\t ({percent:.2f}%)')

        if current_scene is not None:
            scenes.append(current_scene)

        return scenes
