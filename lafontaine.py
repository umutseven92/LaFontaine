import argparse
import os
import pathlib
import time
from pathlib import Path

from lafontaine.generator.video_generator import VideoGenerator
from lafontaine.parser.config_parser import ConfigParser
from lafontaine.parser.video_parser import VideoParser


def main():
    parser = argparse.ArgumentParser(description='LaFontaine is an automatic movie trailer generator.')
    parser.add_argument('-f', '--file', help='Path for the video.', required=True)
    parser.add_argument('-c', '--config', help='Path for the configuration file.', required=True)
    parser.add_argument('-s', '--sub', help='Path for the subtitle file.', required=False)
    parser.add_argument('-d', '--downscale', help='Which width to downscale the video to.', required=False)
    parser.add_argument('-t', '--title', help='Title screen to put in the end of the trailer.', required=False)
    parser.add_argument('-cd', '--cuda', help='Enable CUDA support.', action='store_true')
    parser.add_argument('-sp', '--spoiler', help='Do not spoil the movie.', action='store_true')
    args = vars(parser.parse_args())

    path_to_video = args['file']
    path_to_config = args['config']
    path_to_sub = args['sub']
    optimize = args['downscale']
    title = args['title']
    cuda = args['cuda']
    spoiler = args['spoiler']

    # Parsers
    config_contents = Path(path_to_config).read_text()

    director = ConfigParser.get_director_from_config(config_contents, cuda)

    video_parser = VideoParser(path_to_video, path_to_sub, optimize)

    video_stats = video_parser.video_stats
    print(f'Loaded {video_stats.width}x{video_stats.height} video with {video_stats.fps} FPS.')

    start = time.time()
    print('Started processing..')

    # Process scenes
    scenes = video_parser.get_scenes(director, spoiler)

    end = time.time()

    print(f'Finished processing. Took {end - start} seconds.')
    print(f'Found {len(scenes)} scenes.')

    # Generator
    video_name = os.path.basename(path_to_video)
    base_path = f'out/{video_name}'
    pathlib.Path(base_path).mkdir(exist_ok=True)

    video_generator = VideoGenerator(path_to_video, director.max_length, f'{base_path}/{video_name}_trailer.mp4', title)
    video_generator.generate_from_scenes(scenes, video_stats.fps)


if __name__ == '__main__':
    main()
