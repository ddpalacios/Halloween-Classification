# Haloween-Classification

Computer Vision model using Convolutional Neural Networks to 
classify guest's efforts on their costumes idea and be able to identify weather or not this costumes reaches the 
Haloween expectations.  

# Plan #1 Retrieve image dataset of good and bad Haloween costumes --

To a person's eye, many biases determine what is determined to be 'basic'. This issue was put into perspective and the definition of being "basic" in Haloween is differentiated by different subgroups.  

As you can see within the 'dataset' directory, we have two subdirectories labeled 'basic' and 'non-basic'. 
Within the 'basic' folder, you can observe how each characteristic and stereotype is labeled and classified within their folder. (ie. Cats, Nurses, Angels, etc). Same with the non-basic folder (ie. bad costumes, amazing costumes, couples, etc). The definition itself is biased, but it can be improved by putting everyone else's perspective into the test, however, in theory, this is a good set for differentiation between what is 'basic' and what is not. 

Using **image_loader2.py**, we can download our images and label them into our specific directories as follows -- 

To obtain images, head to google images and search **(scroll down untill there are no more images) --> open JS terminal** **(ctrl+shift+I)** and type in: 

**urls = Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou);**

This will provide you an array for the URL of every image that is within the page. Next, type in this command to **DOWNLOAD** the .txt file of the URLs 

**window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));**

Extract this file to the path of your IDE. open your terminal and run the following command: 

**python3 image_loader2.py --URLs "FILENAME".txt --output datasets/"SUBDIRECTORY"** 

After execution, you will see each URL being downloaded and saved under the specified subdirectory. **Note: You must replace what is within the quotation marks with your .txt file name as well as where you plan on saving these images.**

(This will take a while to download. Be Patient)


# Plan #2 Image-PreProcess



Plan #3 Build model -- pending

Plan #4 Train

Plan #5 allow access to camera,  use set weights to allow accurate classification when predicting

