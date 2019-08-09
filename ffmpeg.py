import glob
import subprocess

all_trailer_files = glob.glob('trailer_test/*')

for movie in all_trailer_files:
    subprocess.run(['ffmpeg', '-i', movie, '-vf','fps=1, scale=299:299', movie+"%04d.png"])