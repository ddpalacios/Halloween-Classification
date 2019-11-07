import warnings

warnings.filterwarnings("ignore")
from os import listdir
from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
import cv2
# Lets Start implementing our model for cnn using keras.
# We will start by importing the important libraries
import warnings
warnings.filterwarnings("ignore")

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential 
from keras.layers import Conv2D, MaxPooling2D 
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization 
from keras import backend as K
from sklearn import preprocessing
from keras.utils import to_categorical
from keras import optimizers




class load_file:
    def __init__(self, file):
        self.file = file

    def get_data(self):
        hal = np.load(self.file)
        X_train, y_train, X_test, y_test,X_val, y_val = [hal[f] for f in hal.files]
        return X_train, y_train, X_test, y_test,X_val, y_val 
    
df = load_file('halloween_classes.npz')
X_train, y_train, X_test, y_test,X_val, y_val  = df.get_data()


#Now that we have our dataset in our dispose, we have to shuffle our dataset

#Lets first shuffle our training data
indices = np.arange(X_train.shape[0])
np.random.shuffle(indices)

X_train= X_train[indices]
y_train = y_train[indices]


# Now our testing data
test_indices = np.arange(X_test.shape[0])

np.random.shuffle(test_indices)
X_test= X_test[test_indices]
y_test = y_test[test_indices]



val_indices = np.arange(X_val.shape[0])
np.random.shuffle(val_indices)
X_val = X_val[val_indices]
y_val = y_val[val_indices]





input_shape = (80,80,3)
kernel_size = (1,1)
batch_size = 16

epochs = 50
model = Sequential()
model.add(Conv2D(64, 
                 kernel_size=(5, 5), 
                 strides=(2, 2),
                 padding = 'same', 
                 activation='relu', 
                 input_shape=input_shape))

model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
model.add(Dropout(0.15))

model.add(Conv2D(64, 
                kernel_size=(5,5),
                strides = (2,2),
                padding='same',
                activation='relu',
                input_shape=input_shape))
          
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
model.add(Dropout(0.25))
          
model.add(Conv2D(128, 
                kernel_size=(3,3),
                strides = (1,1),
                padding='same',
                activation='relu',
                input_shape=input_shape))
          
# model.add(BatchNormalization())
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))
# model.add(Dropout(0.50))
model.add(Flatten())
          
# model.add(Dense(224, activation='relu'))
# model.add(BatchNormalization())
# model.add(Dropout(0.50))         
# model.add(Dense(128, activation='relu'))
# model.add(BatchNormalization())
# model.add(Dropout(0.50))
# model.add(Dense(64, activation='relu'))
# model.add(BatchNormalization())
# model.add(Dropout(0.50))
model.add(Dense(1,activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])





train_datagen = ImageDataGenerator( 
                        rescale=0.0/255
                        )
   

train_generator = train_datagen.flow(x=X_train, y=y_train, batch_size=batch_size)

history = model.fit_generator(train_generator, validation_data=(X_val,y_val), 
                   steps_per_epoch=len(X_train)//batch_size, epochs=epochs)


model.save("basic_witch80x80.h5")
print("Saved model to disk")
loss,acc = model.evaluate(X_test, y_test, batch_size=batch_size)

print("Results:\nERROR LOSS:{}\nACC: {}%".format(loss, round(acc*100)))


from sklearn.metrics import confusion_matrix
import itertools 
import matplotlib.pyplot as plt


# list all data in history
print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
# summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
