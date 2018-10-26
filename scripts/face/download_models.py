import os

#the following two lines allow this script to be called from the vid2vid repo root
#this is awkward. Discussion here: https://github.com/NVIDIA/vid2vid/issues/36#issuecomment-432907265
import sys
sys.path.insert(0, '/vid2vid/')

from scripts.download_gdrive import *

file_id = '10LvNw-2lrh-6sPGkWbQDfHspkqz5AKxb'
chpt_path = './checkpoints/'
if not os.path.isdir(chpt_path):
	os.makedirs(chpt_path)
destination = os.path.join(chpt_path, 'models_face.zip')
download_file_from_google_drive(file_id, destination) 
unzip_file(destination, chpt_path)
