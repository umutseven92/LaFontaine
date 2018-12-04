import cv2


class VideoGenerator:

    def generate_from_scene(self, scene, path):
        self.__generate_from_frames(scene.frames, path)

    def __generate_from_frames(self, frames, path):
        height, width, layers = frames[1].image.shape
        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        video = cv2.VideoWriter(path, fourcc, 24.0, (width, height))

        for j in range(0, len(frames)):
            video.write(frames[j].image)

        cv2.destroyAllWindows()
        video.release()
