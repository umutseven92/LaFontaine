import cv2
from lafontaine.video_parser.video_stats import VideoStats
from lafontaine.video_parser.video_parser import VideoParser


class VideoParserHandler:
    def __init__(self, video_path, split):
        video = cv2.VideoCapture(video_path)

        fps = video.get(cv2.CAP_PROP_FPS)
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.video_stats = VideoStats(fps, width, height, frame_count)
        parsers = []

        for i in range(0, split):
            start = i * (frame_count / split)
            end = start + (frame_count / split)
            parsers.append(VideoParser(video, start, end))

        self.parsers = parsers

    def get_scenes(self, feature_director):
        all_scenes = []

        for parser in self.parsers:
            all_scenes.extend(self.run_parser(parser, feature_director))

        return all_scenes

    def run_parser(self, parser, feature_director):
        scenes = parser.parse_scenes(feature_director, self.video_stats.frame_count)
        return scenes
