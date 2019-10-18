import numpy as np
import matplotlib.pyplot as plt


class load_file:
    def __init__(self, file):
        self.file = file

    def get_data(self):
        hal = np.load(self.file)
        basic_train, basic_test, non_train, non_test = [hal[f] for f in hal.files]
        return basic_train, basic_test, non_train, non_test


df = load_file('halloween_classes.npz')
basic_train, basic_test, non_train, non_test = df.get_data()

print(basic_test[0])