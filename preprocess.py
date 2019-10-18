import warnings

warnings.filterwarnings("ignore")
from os import listdir
from PIL import Image
import os
import numpy as np

PATH = '/home/daniel/PycharmProjects/Halloween-Classification/datasets'
train_basic_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/BASIC/TRAIN-BASIC/"
test_basic_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/BASIC/TEST-BASIC/"

train_non_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC/TRAIN-NON/"
test_non_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC/TEST-NON/"

####################
# Image/classes count
####################
classes = []
for d in os.listdir(PATH):
    if os.path.isdir(os.path.join(PATH, d)) and not d.startswith('.'):
        classes.append(d)
print("There are ", len(classes), "classes:\n", classes)
path, dirs, trainbasic_files = next(os.walk(train_basic_path))
path, dirs, testBasic_files = next(os.walk(test_basic_path))
train = len(trainbasic_files)
test = len(testBasic_files)
print("There are {} Basic TRAIN Images\nThere are {} TEST Basic Images".format(train, test))

######################
# Check image validation
#######################
count = 0
paths = [train_basic_path, test_basic_path, train_non_path, test_non_path]
for img_path in paths:
    print("Checking...{}\n".format(img_path))
    for filename in listdir(img_path):
        if filename.endswith('.jpg'):
            try:
                img = Image.open(img_path + filename)  # open the image file
                img.verify()  # verify that it is, in fact an image

            except (IOError, SyntaxError) as e:
                print('Bad file:', filename)  # print out the names of corrupt files
                count += 1
                os.remove(img_path + filename)  # remove any bad files
print("there are {} bad file(s)".format(count))

#########################
# Turn image files to array
##########################
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

basic_train = []
basic_test = []

non_train = []
non_test = []

for filename in listdir(train_basic_path):
    img = mpimg.imread("/home/daniel/PycharmProjects/Halloween-Classification/datasets/BASIC/TRAIN-BASIC/" + filename)
    basic_train.append(img)

print(len(basic_train))
# elif img_path == "/home/daniel/PycharmProjects/Halloween-Classification/datasets/BASIC/TEST-BASIC/":
#     print("appending: {}".format(img_path))
#     for filename in listdir(img_path):
#         img = mpimg.imread(img_path + filename)
#         basic_test.append(img)
#
# elif img_path == "/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC/TRAIN-NON/":
#     print("appending: {}".format(img_path))
#     for filename in listdir(img_path):
#         img = mpimg.imread(img_path + filename)
#         non_train.append(img)
# elif img_path == "/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC/TEST-NON/":
#     print("appending: {}".format(img_path))
#     for filename in listdir(img_path):
#         img = mpimg.imread(img_path + filename)
#         non_test.append(img)
