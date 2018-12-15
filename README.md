# LaFontaine
LaFontaine is a automatic movie trailer generator.

## Description
In this project, you are asked to implement a
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

## Features Selected

## Usage
```bash
-f res/videos/gunshot.mp4 -c res/config/action.lf -t "North by Northwest"
```

## Dependencies
* ImageMagick is required to create end titles.