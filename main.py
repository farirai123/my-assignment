   ##############################################################################
                   #Farirai Masocha and Godknows Aresho
    ##############################################################################
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
################################################################################
st.title("MACHINE_L_IMAGE_CLASSIFIER")
st.info("Pliz upload 2mb video below")
st.header("upload video below")
uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])
vd.video_upload(uploaded_file)
classifications = cs.classifyImages()

###############################################################################

# def split_process():
#     st.info("Split process started")
#     sv.split_videos_to_frames("")
    
    
################################################################################
def searchInFrames(object_):
    indeces = []
    # classifications = cs.classifyImages()
    if object_ in classifications:
        index = classifications.index(object_)
        st.write(f"{user_input} has been found in frames {index}")
        frames = [ join('.\\data', f) for f in listdir('.\\data') if isfile(join('.\\data', f)) ]
        image = Image.open(frames[index])
        st.image(image, caption=object_)

    #   for i in range(len(classifications)):
    #       if classifications[i] == object_:
    #           index = classifications.index(object_)
    #           indeces.append(index)
    #           filePath = frames[index]
    #           img = load_img(filePath, target_size = (224, 224))
    #           detected_paths.append(filePath)
    #   for i in range(len(indeces)):
    #               st.image(frames[i], width=224)
    else:
        st.write("Object not available in video!")
        
   ###############################################################################     
        
        
user_input = st.text_input("Enter object to search: ")
if st.button('Search'): 
    frames =[]
    detected_paths = []
    searchInFrames(user_input)
    st.write("")
    
    ##############################################################################
                   #Farirai Masocha and Godknows Aresho
    ##############################################################################



    
  

 