![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg)![Tensorflow](https://aleen42.github.io/badges/src/tensorflow.svg)![stackoverflow](https://aleen42.github.io/badges/src/stackoverflow.svg)![Github](https://aleen42.github.io/badges/src/github.svg)

# Air-Writing-To-Speech
## Optical Character Recognition of HandWritten Characters

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