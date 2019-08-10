import glob
import subprocess

all_trailer_files = glob.glob('trailer_test/*')

for movie in all_trailer_files:
    movie_with_no_fileend = movie.split('.')
    subprocess.run(['ffmpeg', '-i', movie, '-vf','fps=1, scale=299:299', movie_with_no_fileend[0]+"%04d.png"])