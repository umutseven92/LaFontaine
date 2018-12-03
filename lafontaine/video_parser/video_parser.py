import cv2
from lafontaine.video_parser.frame import Frame
from lafontaine.video_parser.video_stats import VideoStats


class VideoParser:
    def __init__(self, video_path):
        self.video = cv2.VideoCapture(video_path)
        fps = self.video.get(cv2.CAP_PROP_FPS)
        width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        frame_count = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))

        self.video_stats = VideoStats(fps, width, height, frame_count)

    def parse_video(self):
        success, image = self.video.read()
        count = 0
        while success:
            yield Frame(image, count)
            success, image = self.video.read()
            print(f'Read frame {count}: {success}')
            count += 1

    def save_image(self, image, count, dir):
        cv2.imwrite(f"{dir}/frame{count}.jpg", image)
