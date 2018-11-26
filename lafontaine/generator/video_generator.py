import cv2


class VideoGenerator:

    def generate_from_opencv_images(self, images, path):
        height, width, layers = images[1].shape
        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        video = cv2.VideoWriter(path, fourcc, 24.0, (width, height))

        for j in range(0, len(images)):
            video.write(images[j])

        cv2.destroyAllWindows()
        video.release()

    def generate_from_image_paths(self, image_paths, path):

        images = []

        for i in image_paths:
            image = cv2.imread(i)
            images.append(image)

        self.generate_from_opencv_images(images, path)

