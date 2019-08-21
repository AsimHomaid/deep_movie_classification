import pickle
import subprocess
import glob
import cv2
import sys
import numpy as np

from keras.applications.inception_v3 import InceptionV3
user_input = sys.argv[1]
def get_link(link):
    subprocess.run(['youtube-dl', link, '-o',  'input_files/user_input_file'])

def run_ffmpeg():
    file_location = glob.glob('input_files/*')
    subprocess.run(['ffmpeg', '-i', file_location[0], '-vf', 'fps=1, scale=299:299', "input_files/"+"frame"+"%04d.png"])
def get_frames():
    frames = glob.glob('input_files/*.png')
    return frames
def png_to_numpy(files):
    files.sort()
    files = files[len(files)//3:-len(files)//3]
    
    return [cv2.imread(frame) for frame in files]
def get_deep_features_nn(frame_arrays):
    nn_model = InceptionV3(include_top=False, weights='imagenet', input_shape=(299,299,3), pooling='avg')
    features_array = np.empty((len(frame_arrays), 2048))
    
    for i, frame in enumerate(frame_arrays):
        feature = nn_model.predict(frame.reshape((-1, 299, 299, 3)))
        features_array[i] = feature
    return features_array
def get_predict_proba(deep_features):
    rfc_model = pickle.load(open('finalized_model.sav', 'rb'))
    return rfc_model.predict_proba(deep_features)
def take_top_results(predict_proba):
    
    mean_genre_proba = [genre[:,1].mean() for genre in predict_proba]
    np.argsort(mean_genre_proba)[-3:]
    genres = np.array(['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir','Game-Show','History','Horror','Music','Musical','Mystery','News','Reality-TV','Romance','Sci-Fi','Short','Sport','Thriller','War','Western'])
    return genres[np.argsort(mean_genre_proba)[:-4:-1]]

def genre_prediction(youtube_link):
    get_link(youtube_link)
    
    run_ffmpeg()
    frame_files = get_frames()
    frame_arrays = png_to_numpy(frame_files)
    
    deep_features = get_deep_features_nn(frame_arrays)
    
    results_proba = get_predict_proba(deep_features)
    
    
    top_results = take_top_results(results_proba)
    
    return top_results
def delete_files():
    subprocess.Popen('rm input_files/*',shell=True)
    
print(genre_prediction(user_input))

delete_files()

