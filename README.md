# LaFontaine [![Build Status](https://travis-ci.org/umutseven92/LaFontaine.svg?branch=master)](https://travis-ci.org/umutseven92/LaFontaine)
LaFontaine is an automatic movie trailer generator.

## Description
>In this project, you are asked to implement a
software that automatically extract trailer from a given movie with any genre. Firstly, you will
divide the movie to smaller frames and sound fragments. From these sound and images, you will
extract distinctive features which indicates the excitement of the fragment. You will classify the
scenes by using machine learning algorithms. After classification, all scenes that are found
important will be combined and trailer will be created from these scenes. Mandatory features:
select three features for sound, three features from frame(image) and three features from subtitle.
Apply at least two machine learning algorithms for classification of scenes. Combine important
scenes into one video which is the trailer.

## Etymology
LaFontaine is named after the legendary [Don LaFontaine](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=11&cad=rja&uact=8&ved=2ahUKEwjQlZuukp_fAhUHAhAIHWVCBhgQFjAKegQIDBAB&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FDon_LaFontaine&usg=AOvVaw2YIu6qpVzQw3Gy-5dWpWdK), who was the voice of more than 5000 movie trailers. 
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

#### Subtitle Intensity Detector

#### Subtitle Conversation Counter


## Dependencies

* Python 3+.
* ImageMagick is required to create end titles.
* If CUDA is going to be enabled for better performance, *dlib* needs to be compiled with CUDA support.

## Usage
```bash
python lafontaine.py -f res/videos/gunshot.mp4 -c res/config/action.lf -t "North by Northwest" -d 480 -cd
```

