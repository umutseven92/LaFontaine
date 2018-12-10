
import argparse
import time

from feature_detector.feature_director import FeatureDirector
from lafontaine.generator.video_generator import VideoGenerator
from lafontaine.parser.video_parser import VideoParser

parser = argparse.ArgumentParser(description='Generate trailers from movies')
parser.add_argument('-f', '--file', help='Path for the video', required=True)
args = vars(parser.parse_args())

path_to_video = args['file']

# Features
feature_director = FeatureDirector()

# Parsers
video_parser = VideoParser(path_to_video)

video_stats = video_parser.video_stats
print(f'Loaded {video_stats.width}x{video_stats.height} video with {video_stats.fps} FPS.')

start = time.time()
print('Started processing..')

# Parse scenes
scenes = video_parser.get_scenes(feature_director)

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
2018-12-10, Iterating with 1/10th of a second, processing a 30 second, 1024*768 video takes 140 seconds.
"""
