![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg)![Tensorflow](https://aleen42.github.io/badges/src/tensorflow.svg)![stackoverflow](https://aleen42.github.io/badges/src/stackoverflow.svg)![Github](https://aleen42.github.io/badges/src/github.svg)

# Air-Writing-To-Speech
## Optical Character Recognition of HandWritten Characters using Tensorflow

Handwritten Text Recognition system is implemented using TensorFlow 2.x version and trained on the IAM off-line dataset. The Neural Network model recognizes the text that contain images of tight cropped images(Sample attached below). The model overview can be found below in the Model Overview section. 

![htr](https://github.com/developers-cosmos/Air-Writing-To-Speech/blob/feature_ocr/readme_data/htr.png)

- To directly, check the model working follow the steps in Running Demo section. 
- Otherwise, if you want to train the model from the scratch, continue reading from the Getting Started section. 
## Running Demo : 

- Go to **model** directory and unzip the **model.zip**(pre-trained on IAM dataset).
- Ensure that you extract the model.zip directly into the model directory.
- Now, change your directory to **src** and run `python maintf2.py` 
- Feel free to change the test image by changing the path in the `maintf2.py` file on line 18.
- After running, you'll get the recognized text and the probability of the recognized word.


## Getting Started:
- The design flow of the approach towards OCR is shown below.

![OCR_FLOW](https://github.com/developers-cosmos/Air-Writing-To-Speech/blob/feature_ocr/readme_data/ocr_flow.png)
## Prepare data:
### Steps to download the IAM dataset :
- Crash on the [IAM Dataset](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database) page.
- Please register yourself in their database in order to access the data.
- Scroll down to the Download section where you'll find **access the IAM Handwriting DB 3.0**, follow that link.
- Download words.tgz
- Download words.txt - This is available in data/ascii directory
- Put the words.txt file in data dir
- Create a directory **words** inside data directory and put the content of words.tgz into it.

<pre>
Check if dir structure looks like this:
data
--words.txt
--words
----a01
------a01-000u
--------a01-000u-00-00.png
--------...
------...
----a02
----...
</pre>


## Model Overview

![Model_Overview](https://github.com/developers-cosmos/Air-Writing-To-Speech/blob/feature_ocr/readme_data/nn_overview.png)