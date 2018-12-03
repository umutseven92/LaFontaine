"""
Automatic Trailer Generation for Movies: In this project, you are asked to implement a
software that automatically extract trailer from a given movie with any genre. Firstly, you will
divide the movie to smaller frames and sound fragments. From these sound and images, you will
extract distinctive features which indicates the excitement of the fragment. You will classify the
scenes by using machine learning algorithms. After classification, all scenes that are found
important will be combined and trailer will be created from these scenes. Mandatory features:
select three features for sound, three features from frame(image) and three features from subtitle.
Apply at least two machine learning algorithms for classification of scenes. Combine important
scenes into one video which is the trailer.
"""

import argparse
from lafontaine.video_parser.video_parser import VideoParser
from lafontaine.generator.video_generator import VideoGenerator
from feature_detector.feature_director import FeatureDirector
from lafontaine.video_parser.scene import Scene

parser = argparse.ArgumentParser(description='Generate trailers from movies')
parser.add_argument('-f', '--file', help='Path for the video', required=True)
args = vars(parser.parse_args())

path_to_video = args['file']

# Features
feature_director = FeatureDirector()

# Parser
video_parser = VideoParser(path_to_video)

video_stats = video_parser.video_stats
print(f'Loaded {video_stats.width}x{video_stats.height} video with {video_stats.fps} FPS.')

scenes = []
current_scene = None

for frame in video_parser.parse_video():
    result = feature_director.check_for_image_features(frame)
    if result:
        if current_scene is None:
            current_scene = Scene()

        current_scene.add_frame(frame)
    else:
        if current_scene is not None:
            scenes.append(current_scene)
            current_scene = None

    percent = (frame.count * 100)/video_stats.frame_count
    print(f'Processed frame {frame.count} of {video_stats.frame_count}\t ({percent:.2f}%)')

# Generator
video_generator = VideoGenerator()

count = 0
for s in scenes:
    video_generator.generate_from_scene(s, f'out/scene{count}.avi')
    count += 1
