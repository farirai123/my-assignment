   ##############################################################################
                   #Farirai Masocha and Godknows Aresho
    ##############################################################################
################################
import PIL
from pathlib import Path
from PIL import UnidentifiedImageError

path = Path(".//data").rglob("*.jpg")
for img_p in path:
    try:
        img = PIL.Image.open(img_p)
    except PIL.UnidentifiedImageError:
           
################################
from keras.applications import vgg16
# from keras.applications.vgg16 import VGG16
# from keras.applications.vgg16 import preprocess_input
# from keras.applications.vgg16 import decode_predictions
# from keras.preprocessing.image import img_to_array
# from keras.preprocessing.image import load_img

from os import listdir
from os.path import isfile, join
from PIL import Image


def classifyImages():
    model = vgg16.VGG16()
#     from keras.applications.vgg16 import decode_predictions
    classify = []
    frames = [ join('.//data', f) for f in listdir('.//data') if isfile(join('.//data', f)) ]
    for i in range(len(frames)):    
        image = vgg16.load_img(frames[i], target_size=(224, 224)) 
        image = vgg16.img_to_array(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        # prepare the image for the VGG model
        image = vgg16.preprocess_input(image)
        # predict the probability across all output classes   
        img_pred = model.predict(image)
        # convert the probabilities to class labels
        label = vgg16.decode_predictions(img_pred)    
        label = label[0][0]
        result =  label[1]
        classify.append(result)
    print(classify)
    return classify

if __name__ == "__main__":
    classifyImages()
    
    ##############################################################################
                   #Farirai Masocha and Godknows Aresho
    ##############################################################################



    
