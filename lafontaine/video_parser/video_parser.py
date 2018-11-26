import cv2
from lafontaine.video_parser.frame import Frame


class VideoParser:
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path

    def parse_video(self):
        vidcap = cv2.VideoCapture(self.video_path)
        success, image = vidcap.read()
        count = 0
        while success:
            yield Frame(image, count)
            success, image = vidcap.read()
            print(f'Read frame {count}: {success}')
            count += 1

    def save_image(self, image, count, dir):
        cv2.imwrite(f"{dir}/frame{count}.jpg", image)
