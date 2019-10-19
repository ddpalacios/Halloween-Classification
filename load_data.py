import numpy as np
import matplotlib.pyplot as plt
import cv2




class load_file:
    def __init__(self, file):
        self.file = file

    def get_data(self):
        hal = np.load(self.file)
        X_train, y_train, X_test, y_test = [hal[f] for f in hal.files]
        return X_train, y_train, X_test, y_test


df = load_file('halloween_classes.npz')
X_train, y_train, X_test, y_test = df.get_data()

for i in range(30, 80):
    image = cv2.cvtColor(X_train[i], cv2.COLOR_BGR2RGB)

    plt.imshow(image)
    plt.show()
