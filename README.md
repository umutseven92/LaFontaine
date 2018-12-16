
# LaFontaine [![Build Status](https://travis-ci.org/umutseven92/LaFontaine.svg?branch=master)](https://travis-ci.org/umutseven92/LaFontaine) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/6b6a32080d154b9b910a804511fcf251)](https://app.codacy.com/app/umutseven92/LaFontaine?utm_source=github.com&utm_medium=referral&utm_content=umutseven92/LaFontaine&utm_campaign=Badge_Grade_Dashboard)
LaFontaine is an automatic movie trailer generator.

## Description

LaFontaine creates movie trailers for any genre using pre-defined features, like number of faces on screen, and loudness of volume. 
Scenes are extracted using these features and combined to create the final trailer.
There are three features for frame, three features for sound and three features for subtitles. Features are read from configurations and are fully configurable.

## Etymology
LaFontaine is named after the legendary [Don LaFontaine](https://en.wikipedia.org/wiki/Don_LaFontaine), who was the voice of more than 5000 movie trailers. 
He is the voice in the classic phrase "In a world...".

## Features

### Image Features

#### Face Recognizer
```json
{
  "id": "FaceRecognizer",
  "face_count": 3,
  "frames": 100
}
```
Records for *frames* amount of frames if the amount of faces in the screen is greater than *face_count*.

#### Frame Delta Detector
```json
{
  "id": "FrameDeltaDetector",
  "delta": 0.95,
  "frame_limit": 50,
  "scene_change_limit": 3,
  "frames": 75
}
```
Records for *frames* amount of frames if frame difference percentage is greater than *delta* at least *scene_change_limit* times continuously for at least *frame_limit* frames.

#### Frame Color Counter
```json
{
  "id": "ColorCounter",
  "color_count": 50000,
  "frames": 100
}
```
Records for *frames* amount of frames if the amount of unique colors is greater than *color_count*.

### Sound Features

#### Sound Peak Detector
```json
{
  "id": "SoundPeakDetector",
  "audio_threshold": 0.30,
  "frames": 50
}
```
Records for *frames* amount of frames if the volume is higher than *audio_threshold*.

#### High Volume Detector
```json
{
  "id": "HighVolumeDetector",
  "volume": 0.60,
  "frame_limit": 50,
  "frames": 70
}
```
Records for *frames* amount of frames if the volume is continuously higher than *volume* for *frame_limit* amount of frames.

#### Sound Delta Detector
```json
{
  "id": "SoundDeltaDetector",
  "delta": 3,
  "frame_limit": 50,
  "scene_change_limit": 3,
  "frames": 75
}
```
Records for *frames* amount of frames if audio difference percentage is greater than *delta* at least *scene_change_limit* times continuously for at least *frame_limit* frames.

### Subtitle Features

#### Subtitle Density Detector
```json
{
  "id": "SubtitleDensityDetector",
  "char_count": 60,
  "frames": 100
}
```
Records for *frames* amount of frames if the subtitle has more than *char_count* characters.

#### Subtitle Intensity Detector
```json
{
  "id": "SubtitleIntensityDetector",
  "intensity_char": "!",
  "char_count": 3,
  "frames": 100
}
```
Records for *frames* amount of frames if the subtitle has more than *char_count* *intensity_char* characters.

#### Subtitle Conversation Counter
```json
{
  "id": "SubtitleConversationCount",
  "conversation_count": 2,
  "frames": 100
}
```
Records for *frames* amount of frames if the subtitle has more than *conversation_count* characters speaking.

## Dependencies

* Python 3+.
* ImageMagick is required to create end titles.
* If CUDA is going to be enabled for better performance, *dlib* needs to be compiled with CUDA support.

## Configuration

Configuration files contain list of features and some other metadata. Each genre has its own configuration file. To create an action movie trailer, you use the *action.lf* file, to create a comedy movie trailer you use *comedy.lf* and vice versa.

Example configuration files are given in the *res/config/* folder, however you can create your own custom configurations.

*res/config/action.lf*
```json
{
  "genre": "action",
  "max_length": "120",
  "features": [
    .
    .
    (list of features)
  ]
}
```

Parameter|Description|Required
--- | ---| ---
genre | Name of the genre | True 
max_length | Max length of the trailer in seconds | True
features | List of features, listed in order of importance | True


## Usage
```bash
python lafontaine.py -f res/videos/northbynorthwest.mp4 -s res/subtitles/northbynorthwest.srt -c res/config/action.lf -t "North by Northwest" -d 480 -cd
```

Parameter|Description|Required
--- | ---| ---
-f, --file | Path to the video file | True 
-s, --sub | Path to the subtitle file<sup>1</sup> | False
-c, --config | Path to the feature configuration file | True
-t, --title | What to put on the title card in the end of the trailer | False
-d, --downscale | Which width to downscale the resolution to<sup>2</sup>| False
-cd, --cuda | Enable CUDA support | False

<sup>1</sup>: If this option is not given, subtitle features will be disabled.

<sup>2</sup>: Aspect ration will be preserved.

## Example Trailer
