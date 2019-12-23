# discursos-de-navidad
 
This project is a corpus analysis of the Christmas speeches delivered by the head of state from 1937 to 2018. It is built using `NLTK`, `spaCy`, `scattertext` and `markovify` libraries. 
  
- HTML visualizations available at: https://lirondos.github.io/discursos-de-navidad/ [in Spanish].
- For information about the traditional Christmas speech: https://en.wikipedia.org/wiki/Christmas_Eve_National_Speech.

This project contains the following files: 
* The `data` folder contains the files with the Christmas speeches from 1937 to 2018 in `txt` format and the metadata associated with every speech (year, speaker, URL were it was retrieved).
* The `Speech` class creates the object Speech with the information for a given speech.
* The `Corpus` class creates the corpus object that contains the speeches to be analyzed. This class uses the files inside the `speeches` folder. This file also contain the methods to perform the lexical analysis of the created corpus.
* The `visualize.py` script creates interactive HTML visualization from TF-IDF measures using `scattertext` library. The visualization files are stored inside the visualization folder.

The files that have a main method than can be executed are: 
* `corpus.py` (creates several corpus objects for different time periods of time and calls the radiography method in order to get their lexical analysis)
* `visualize.py` (creates an instance of the corpus class and generates several visualization files with TF-IDF measures using the scattertext library)

This project requires the following libraries: 
* `nltk`
* `spacy`
* `pandas`
* `scattertext`
* `markovify`
* `os`
* `re`
* `time`
* `newspaper`
* `matplotlib`

A previous version of this project (with speeches only from 1975 on and a markov speech generator) can be found at https://github.com/lirondos/orgulloysatisfaccion
