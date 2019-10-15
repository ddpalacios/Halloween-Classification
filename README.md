# Halloween-Classification

Computer Vision model using Convolutional Neural Networks to 
classify guest's efforts on their costumes idea and be able to identify weather or not this costumes reaches the 
halloween expectations.  

# Plan #1 Retrive image dataset of good and bad halloween coustumes --

To a person's eye, there are many biases that determines what is determined to be 'basic'. This issue was put into perepective and the definition of being "basic" in Haloween is diffrentiated by different subgroups.  

As you can see within the 'dataset' directory, we have two subdirectories labeld 'basic' and 'non-basic'. 
Within the 'basic' folder, you can observe how each characteristic and stereotype is labeled and classied within their own folder. (ie. Cats, Nurses, Angels, etc). Same with the non-basic folder (ie. bad costumes, amazing costumes, couples, etc). The definition itself is clearly biased, but it can be improved by putting everyone else's persepctive into the test however, in theory, this is good set for diffrentiation between what is clearly 'basic' and what is not. 

Using **image_loader2.py**, we are able to download our images and label them into our specific directories as follows -- 

To obtain images, head to google images and search **(scroll down untill there are no more images) --> open JS terminal** **(ctrl+shift+I)** and type in: 

**urls = Array.from(document.querySelectorAll('.rg_di .rg_meta')).map(el=>JSON.parse(el.textContent).ou);**

This will provide you an array for the URL of every image that is within the page. 

Next, type in this command to DOWNLOAD the .txt file of the urls 

**window.open('data:text/csv;charset=utf-8,' + escape(urls.join('\n')));**

extract this file to your path of your IDE.

open your terminal and run the following command: 

**python3 image_loader2.py --urls "FILENAME".txt --output datasets/"SUBDIRECTORY"** 

after exceution, you will see each url being downloaded and saved under the specifed subdirectory. 

**Note: You must replace what is within the quotation marks with your own .txt file name as well as where you plan on saving these images.** 

(This will take a while to download. Be Patient)


# Plan #2 Image-PreProcess






Plan #3 Build model -- pending

Plan #4 Train

Plan #5 allow access to camera,  use set weights to allow accurate classification when predicting

