   ##############################################################################
                   #Farirai Masocha and Godknows Aresho
    ##############################################################################


import cv2
import numpy as np
import os
from keras.applications.vgg16 import preprocess_input
#####################################################################

def split_videos_to_frames(path:str):#function to split to frames
    cap = cv2.VideoCapture(path)  #cap variable
    if cap.isOpened():
        print("Video Opened")
    try:
        if not os.path.exists('data'):
            os.makedirs('data',exist_ok=True)
    except OSError:
        print ('Error: Creating directory of data')
    currentFrame = 0
    while(cap.isOpened()):
            status, frame = cap.read()# Capture frame-by-frame
            name = './data/frame' + str(currentFrame) + '.jpg'# Saves image of the current frame in jpg file
            print ('Creating...' + name)
            if status:
                cv2.imwrite(name, frame)
            currentFrame += 1  # To stop duplicate images
            if currentFrame == 90:
                break
    cap.release() # When everything done, release the capture
    cv2.destroyAllWindows()
    
##################################################################################################