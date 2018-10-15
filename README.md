Simple project to count shortest word distance in a file.


## Install
It has been tested with Python 3.6.

    > pip install -r requirements.txt

## Run

    > python word_distance.py --help
    > python word_distance.py --filename word_distance.py  --word1 to --word2 word

## Test

    > py.test 

## TODO

* clarify if punctuation and letter case should be handled. Eg. 
"This is a sentence with a dot. What is the distance?" What should be the distance of 
- ('this', 'a')
- ('a', 'dot')
- ('this', 'distance')
Currently all these cases are not handled and it will return `None`.
