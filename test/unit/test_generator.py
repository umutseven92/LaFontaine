import cv2
import os
from lafontaine.generator.video_generator import VideoGenerator


FRAME_PATH = '../../res/frames/'

FRAME_AMOUNT = 152


def test_can_generate_from_opencv_images():
    output_path = '../../out/result_from_opencv.avi'

    if os.path.exists(output_path):
        os.remove(output_path)

    images = []

    for i in range(0, FRAME_AMOUNT):
        path = f'{FRAME_PATH}/frame{i}.jpg'
        image = cv2.imread(path)
        images.append(image)

    video_generator = VideoGenerator()
    video_generator.generate_from_opencv_images(images, output_path)

    cap = cv2.VideoCapture(output_path)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    assert video_length == FRAME_AMOUNT


def test_can_generate_from_image_paths():
    output_path = '../../out/result_from_image_paths.avi'

    if os.path.exists(output_path):
        os.remove(output_path)

    images = []

    for i in range(0, FRAME_AMOUNT):
        image_path = f'{FRAME_PATH}/frame{i}.jpg'
        images.append(image_path)

    video_generator = VideoGenerator()
    video_generator.generate_from_image_paths(images, output_path)

    cap = cv2.VideoCapture(output_path)
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    assert video_length == FRAME_AMOUNT
