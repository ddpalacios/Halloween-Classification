# Halloween-Classification

 *For Testing:* 
 - Please head to "Saved_Models" directory and RUN script *RUN_ME_halloween_testing.py* This may take a minute to load the model but it will give you results.**
 
 *For Evaluation:*
 
- Head to directory --> "Model_Design & Testing"**

- Check out model_78. ipynd **This notebook is where you will see how I prepared my dataset as well as the resulted predictions with their corresponding pictures**

- Check out the other notebooks which are two different model architectures and how I dealt with over/underfitting. This was a big issue and it is necessary to view the differences.  

- View model_80.ipynd & model_73.ipynd There are outputs already given for you within each shell

*Graphs & Saved models & Saved Data*

 - Check out Directory "Saved_Models" as you will find subfolders for each corresponding model. You will find:  Confusion matrix,  Accuracy graph results, and loss results (training & validation) ALL in PNG file, as well as the model architecture, used that received the following results**

 --Python file "google_image_extractor.py" is the script I used to extract all images from google images

 --This project was evaluated using ACCURACY, however, other metrics were used as well for viewing. (again, check out the other two ipynd files)


# For plan & description:

Computer Vision model using Convolutional Neural Networks to 
classify guest's efforts on their costumes idea and be able to identify whether or not this costumes reaches the 
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

Once we have the images within both directories **(Class 1 & Class 0**) We are now ready to **split the data 70% training images and 30% testing images**. There are several ways to do this, however, this process was done manually. Both Class directories have **separate folders of testing and training**. We need to **read these images, resize, convert them it NumPy array, and save.** 

to read these images,  use **CV2** (when reading images, the computer reads them as a matrix of values depending on its color hue). We need to save these values into our list, then **take that list and use NumPy.savez_compressed()** to save the NumPy array for later use during training. The values are saved under **.npz file** which is then loaded in *load_data.py.* When loaded, we have 4 variables, **X_train, X_test, y_train, and y_test**. X_train are the training images and its associated labels are the variable y_train (this **contains 1’s and 0’s** to indicate which class does the image in X_train belong to). This works the same way with the testing variables, except it is used as validation to see how well our potential model is so we can **further tune our model for best accuracy.** 


# Plan #3 Build model
Now that we have gotten this far within this project, it is time for us to start building this model.

To start, I will be using **KERAS** to build my network. We are building a **Convolutional Neural Network** since the data (or images) we will be dealing with consists of specific patterns that we need to be able to differentiate between. For example, someone who is "Basic" could be wearing bunny ears or a devil costume while a non-basic person would be a very bad costume or as well as well thought out one. The size of our model depends on our intuition on how well we will be able to identify every pattern that is given via image.



# Plan #4 Train
For training, this was a bit more tricky. Our goal is to minimize our cost and increase our validation accuracy, however, during training, I have stumbled across the problem of overfitting. This was a common issue since our training accuracy was a significantly higher percentage than the validation accuracy. However, this is mostly dealt with normalizing & max-pooling my data to decrease this. I also experimented with the resolution size, strides, etc. In the end, our final accuracy came to be **78%** which at first glance it is not that great. However, we must understand that defining who is basic or not is such a bias topic. Our model can say that this person IS basic, but in someone else's eyes, it could be the exact opposite. I believe 78% was a great validation accuracy to catch any bias when predicting new test data. 


# Plan #5 allow access to the camera
There were two options for this... Using my phone camera to take pictures of people's costumes and then feed it through my model or use the nvidea jetson camera to take the pictures. I found that the phone camera came out to have better results than the jetson nano.  Possibilities:  The camera is a wide-open lens, both cameras take in different perspectives and effects when predicting the final result.


# Outcome
After I had many people test out my model, there have been many discoveries I have made for the various costumes from guests. The model looked for poses, what you were wearing, and how much you were wearing. 

Someone who is making a "Sensual" pose is more likely to be in the basic category.  

Someone who has a well-thought costume could be more likely to be in the non-basic category.

Again, this classification extremely biases. However, many (or all) guests seemed to enjoy it either way, so I call this project a success. It could be better. The dataset itself can be more thoroughly cleaned and in their correct categories and the model could be expanded. Nevertheless, it still worked the way it supposed to.  

