import warnings
import simpleaudio as sa
warnings.filterwarnings("ignore")
from os import listdir
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
import cv2
from keras.models import load_model
from keras.preprocessing.image import img_to_array
#from CAM import From_cam

image = os.listdir('pic_cv2/')
non_result = 'non'
basic_result = 'basic'
non_result = sa.WaveObject.from_wave_file(non_result)
basic_result = sa.WaveObject.from_wave_file(basic_result)

def classify_from_cam(model):
    image = os.listdir('pic_cv2/')
#     os.chdir(directory)
    use = From_cam()
    use.cam()
    image_ = cv2.imread(image[0])
    image_ = np.array(image_)
    prediction = get_predictions(image_, model)
    declare_result_from(prediction,image_)
    

def classify_from_phone(model):
    image = get_image()
    prediction = get_predictions(image, model)
    declare_result_from(prediction, image)
    do_again(model)
    
def do_again(model):
    again = int(input("Another Victim? (1/0)\n> "))
    if again:
        classify_from_phone(model)
    else:
        exit()
    
def do_again_from_cam(model):
    again = int(input("Another Victim? (1/0)\n> "))
    if again:
        classify_from_cam(model)
    else:
        exit()
    
def speak():
    filename = 'intro'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing
    


def load():
    play = False
    model = load_model('basic_witch2.h5')
    print("\t\t\t----MODEL LOADED---")
    play = int(input("\n\n\nAllow Intro? (1/0)\n> "))
    
    if play:
        speak()
        return model
    else:
        
        return model
        

def get_image():
    x = '/run/user/1000/gvfs/'
    idx = 0
    pic = 0
    SHAPE = 50
    try:
        path = listdir(x)[idx]
        print("Trying index 0")
        true_path = x+path+'/DCIM/100APPLE/'

        filename = listdir(true_path)
        filename = filename[pic]
        print(filename)
        image = cv2.imread(true_path +filename)
        return image
    except:
        path = listdir(x)[idx+1]
        print("Trying index 1")
        true_path = x+path+'/DCIM/100APPLE/'
        filename = listdir(true_path) 
     
        filename = filename[pic]
        print(filename)
        image = cv2.imread(true_path +filename)
        return image
    
def phone(model):
    input("\t\t\tHIT ENTER WHEN PICTURE IS READY----")
    classify_from_phone(model)
    

def get_predictions(image, model):
  
    image = cv2.resize(image, (50, 50))
    image = image.astype("float")
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    pred = model.predict_classes(image)
    return pred


def declare_result_from(prediction,image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if prediction == 1:

        basic_result.play()
        
        
    else:


        non_result.play()

   
    

def main():
    
    again = False
    cam = False
    model= load()
    cam = int(input("\t\t\tUSE CAMERA?(1/0):\n> "))
    if cam:
        classify_from_cam(model)
       # phone(model)
        
        #main()
       
        do_again_from_cam(model)
       #print(os.listdir('pic_cv2/'))
       # exit()
        
    else:
        phone(model)
        
   
    
    do_again(model)
        


main()


