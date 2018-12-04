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
import time

from feature_detector.feature_director import FeatureDirector
from lafontaine.generator.video_generator import VideoGenerator
from lafontaine.video_parser.video_parser_handler import VideoParserHandler

parser = argparse.ArgumentParser(description='Generate trailers from movies')
parser.add_argument('-f', '--file', help='Path for the video', required=True)
args = vars(parser.parse_args())

path_to_video = args['file']

# Features
feature_director = FeatureDirector()

# Parser
video_parser_handler = VideoParserHandler(path_to_video, 5)

video_stats = video_parser_handler.video_stats
print(f'Loaded {video_stats.width}x{video_stats.height} video with {video_stats.fps} FPS.')

start = time.time()
print('Started processing..')

#  Parse scenes
scenes = video_parser_handler.get_scenes(feature_director)

end = time.time()
print(f'Finished processing. Took {end - start} seconds.')

# Generator
video_generator = VideoGenerator()

count = 0
for s in scenes:
    video_generator.generate_from_scene(s, f'out/scene{count}.avi')
    count += 1

"""
Benchmarks
2018-12-03, No optimizations: Processing 30 second, 1024*768 video takes 292 seconds.
"""
