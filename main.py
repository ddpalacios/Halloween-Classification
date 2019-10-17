import warnings

warnings.filterwarnings("ignore")
import os

PATH = '/home/daniel/PycharmProjects/Halloween-Classification/datasets'
classes = []
for d in os.listdir(PATH):
    if os.path.isdir(os.path.join(PATH, d)) and not d.startswith('.'):
        classes.append(d)
print("There are ", len(classes), "classes:\n", classes)
path, dirs, basic_files = next(os.walk("/home/daniel/PycharmProjects/Halloween-Classification/datasets/BASIC"))
path, dirs, NonBasic_files = next(os.walk("/home/daniel/PycharmProjects/Halloween-Classification/datasets/NON-BASIC"))
basic_count = len(basic_files)
NonBasic_count = len(NonBasic_files)
print("There are {} Basic Images\nThere are {} Non-Basic Images".format(basic_count, NonBasic_count))
