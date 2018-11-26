import cv2

from lafontaine.generator.video_generator import VideoGenerator


def test_can_generate_from_opencv_images():
    output_path = 'res/frames'
    images = []

    for i in range(0, 152):
        path = f'../../{output_path}/frame{i}.jpg'
        image = cv2.imread(path)
        images.append(image)

    video_generator = VideoGenerator()
    video_generator.generate_from_images(images, '../../out/result.avi')
