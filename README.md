# Jaccard

This script use [Jaccard Index](https://es.wikipedia.org/wiki/%C3%8Dndice_Jaccard) to discover the topic name related to some top terms.

I used for my thesis project for my CS Degree. You can check it in [dblp-journals](https://github.com/Ajeo/dblp-journals).

# Dependencies

* Install [Python 3.7](https://www.python.org/downloads/)
* Install [Pipenv](https://pipenv.readthedocs.io/en/latest/)

# Development

1. Clone this project
2. Run `pipenv shell`
3. Run `pipenv install`
4. Edit jaccard.py

# How To Use

1. Update the values in `topics.csv`. The "Topic" column represent the name of the topic and the "TopTerms" represent the list of top terms to use with Jaccard
2. Use the output from [dblp-journals](https://github.com/Ajeo/dblp-journals) to replace the data in the `input` folder
3. Run `python jaccard.py`
