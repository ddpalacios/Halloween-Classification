import cv2
import numpy as np

class load_classes:
    def __init__(self, file):
        self.file = file

    def get_data(self):
        hal = np.load(self.file)
        X_train, y_train, X_test, y_test,X_val, y_val = [hal[f] for f in hal.files]
        return X_train, y_train, X_test, y_test,X_val, y_val 
    
df = load_classes('halloween_classes.npz')
X_train, y_train, X_test, y_test,X_val, y_val  = df.get_data()

class load_models:
    def __init__(self, file):
        self.file = file

    def get_data(self):
        hal = np.load(self.file)
        model_80, model_73, model_78 = [hal[f] for f in hal.files]
        return model_80, model_73, model_78 
    
df = load_models('halloween_models.npz')
model_80, model_73, model_78 = df.get_data()


print(model_80.get_weights())









