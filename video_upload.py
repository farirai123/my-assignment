import streamlit as st
import cv2 as cv
import tempfile
import os
import cv2
import classify as cs
import split_video
import io
from PIL import Image
import tempfile
import cv2
import streamlit as st
import io 
import video_upload as vd
import split_video as sv
import classify as cs
from keras.preprocessing.image import load_img
from os import listdir
from os.path import isfile, join

#############################################################################################
def video_upload(file):
	if file is not None:
          mace = io.BytesIO(file.read())   
          temporary_location = "simple4.mp4"# the uploaded video will be saved using this name
          with open(temporary_location, 'wb') as out:  
              out.write(mace.read())  
            # close file
          out.close()
          split_video.split_videos_to_frames(temporary_location)
          return cs.classifyImages()
        
    ##############################################################################
                   #Farirai Masocha and Godknows Aresho
    ##############################################################################



    
        



    
