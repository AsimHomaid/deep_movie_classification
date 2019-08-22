

Deep Movie Classification
===


## Table of Contents

[TOC]

## Intro

Movie genres do not have a formal definition, but are rather based on human intiution. With a lack of any objective or formal method to label, genres become one of the more vague elements for a computer to grasp.

This project is a attempt to use a neural network to make accurate predictions on a movie genre when given a video trailer. By training it on roughly 4000 movie trailers labeled by genre.

Project Pipeline
---
* User inputs Youtube link for a movie trailer
* Download trailer on local disk
* Turn video file into a set of image frames, 1 frame for each second
* Store .png files as 3D numpy arrays shaped as [299, 299, 3]
* Exract deep features from a frame buy running it into a pre-trained Inception-V3 neural network.
* Use the output of 2048 deep features to make a prediction on movie genre using a random forest.



User Guide
---
* `movie_metadata.csv`: original file containing movie titles and labels found on [Kaggle](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
* `trailer_source.csv`: file with all links for trailers to download(total size is around 100gb)
* `movie_genre_matrix.csv`: one hot encoded gneres and movie titles
* `extract_deep_features_store_db.ipynb`: notebook with instruction to extract deep featurs and store them in mongo db for later use
* `build_and_export_model.ipynb`: notebook on how to build a random forest and pickle it to use for production pipeline
* `ffmpeg.py`: python script that takes all videos downlaoded and exports them into .png frames in order. movie_title_n.png
* `deployement.py`: production pipeline. Takes youtube link as std-in and prints out top 3 genres.

## Model Improvements
replace neural network with either a recurrent neural network, or residual neural network. Currently, the model only works on single frames without context, as a result, accuracy isn't where it should be. So far the model makes predictions based on object recognition on a frame by frame bases. Further work is needed to make a neural network comprehend a video.
