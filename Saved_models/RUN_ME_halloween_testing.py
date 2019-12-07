import numpy as np
import cv2
from keras.models import load_model
import os

from keras.preprocessing.image import img_to_array

def get_predictions(image, model):
  
    image = cv2.resize(image, (50, 50))
    image = image.astype("float")
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    pred = model.predict_classes(image)
    return pred

def predict_images(model):
    IMAGES = []
    PATH = os.path.dirname(os.path.realpath(__file__))
    PATH = os.listdir(PATH+"/")
    penny = 'pennywise.jpg'
    fireman = 'fireman.jpeg'
    witch = 'witch.jpg'
    joker = 'joker.jpeg'
    IMAGES.extend((penny, fireman, witch, joker))
    for each_image in IMAGES:
        image = PATH.index(each_image)
        image = cv2.imread(os.path.dirname(os.path.realpath(__file__))+"/" + PATH[image])
        predictions = get_predictions(image, model)
        if predictions == 1:
            print("{} is BASIC".format(each_image))
        else:
            print("{} is NOT BASIC".format(each_image))
        




print("Loading model...\n")
model1 = load_model('Halloween_model_edition_78.h5')
print("\nModel is Loaded!")
predict_images(model1)
