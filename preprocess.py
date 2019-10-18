import warnings

warnings.filterwarnings("ignore")
from os import listdir
from PIL import Image
import os

PATH = '/home/daniel/PycharmProjects/Halloween-Classification/datasets'
train_basic_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/BASIC/TRAIN-BASIC"
test_basic_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/BASIC/TEST-BASIC"

train_non_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC/TRAIN-NON"
test_non_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC/TEST-NON"

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
img_path = "/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC/TEST-NON/"
for filename in listdir(img_path):
    if filename.endswith('.jpg'):
        try:
            img = Image.open(img_path + filename)  # open the image file
            img.verify()  # verify that it is, in fact an image

        except (IOError, SyntaxError) as e:
            print('Bad file:', filename)  # print out the names of corrupt files
            count += 1
            os.remove(img_path + filename)  # remove any bad files
print("there are {} bad files".format(count))
