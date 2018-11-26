import sys
import argparse
from lafontaine.video_parser.video_parser import VideoParser
from lafontaine.feature_detector.face_recognizer import FaceRecognizer

parser = argparse.ArgumentParser(description='Generate trailers from movies')
parser.add_argument('-f', '--file', help='Path for the video', required=True)
args = vars(parser.parse_args())

path_to_video = args['file']

# Features
face_recognizer = FaceRecognizer()

# Parser
video_parser = VideoParser(path_to_video)

image_limit = 1000
count = 0

for frame in video_parser.parse_video():
    faces = face_recognizer.check_for_faces(frame.image)
    if len(faces) > 0:
        print(f'Found {len(faces)} faces in frame {frame.count}, saving..')
        video_parser.save_image(frame.image, count, 'res/frames')
        count += 1

        if count > image_limit:
            print('Image limit reached, exiting..')
            sys.exit(0)
