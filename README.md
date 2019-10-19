# Halloween-Classification

Computer Vision model using Convolutional Neural Networks to 
classify guest's efforts on their costumes idea and be able to identify weather or not this costumes reaches the 
Halloween expectations.  

# Plan #1 Retrieve image dataset of good and bad Halloween costumes --

To a person's eye, many biases determine what is determined to be 'basic'. This issue was put into perspective and the definition of being "basic" in Haloween is differentiated by different subgroups.  

As you can see within the 'dataset' directory, we have two subdirectories labeled 'basic' and 'non-basic'. 
Within the 'basic' folder, you can observe how each characteristic and stereotype is labeled and classified within their folder. (ie. Cats, Nurses, Angels, etc). Same with the non-basic folder (ie. bad costumes, amazing costumes, couples, etc). The definition itself is biased, but it can be improved by putting everyone else's perspective into the test, however, in theory, this is a good set for differentiation between what is 'basic' and what is not. 

Using **image_loader2.py**, we can download our images and label them into our specific directories as follows -- 

To obtain images, head to google images and search **(scroll down untill there are no more images) --> open JS terminal** **(ctrl+shift+I)** and type in: 

*urls = Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou);*

This will provide you an array for the URL of every image that is within the page. Next, type in this command to **DOWNLOAD** the .txt file of the URLs 

*window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));*

Extract this file to the path of your IDE. open your terminal and run the following command: 

*python3 image_loader2.py --URLs "FILENAME".txt --output datasets/"SUBDIRECTORY"* 

After execution, you will see each URL being downloaded and saved under the specified subdirectory. **Note: You must replace what is within the quotation marks with your .txt file name as well as where you plan on saving these images.**

(This will take a while to download. Be Patient)


# Plan #2 Image-PreProcess
**preprocess.py**

Once we have the images within both directories **(Class 1 & Class 0**) We are now ready to **split the data 70% training images and 30% testing images**. There are several ways to do this, however, this process was done manually. Both Class directories have **seperate folders of testing and training**. We need to **read these images, resize, convert them it numpy array, and save.** 

to read these images,  use **CV2** (when reading images, the computer reads them as a matrix of values depending on its color hue). We need to save these values into our own list, then **take that list and use numpy.savez_compressed()** to save the numpy array for later use during training. The values are saved under **.npz file** which is then loaded in *load_data.py.* When loaded, we have 4 variables, **X_train, X_test, y_train, and y_test**. X_train are the training images and its associated labels is the variable y_train (this **contains 1’s and 0’s** to indicate which class does the image in X_train belong to). This works the same way with the testing variables, except it is used as validation to see how well our potential model is so we can **further tune our model for best accuracy.** 


# Plan #3 Build model

Plan #4 Train

Plan #5 allow access to camera,  use set weights to allow accurate classification when predicting

