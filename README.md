# A corpus of Spanish political speeches from 1937 to 2019
 
A corpus of political speeches delivered by the head of state of Spain from 1937 to 2019. The corpus consists of 77 speeches (206,937 tokens) written in European Spanish that were delivered on Christmas by the different heads of state of Spain from 1937 to 2019 (dictator Francisco Franco, king Juan Carlos I and king Felipe VI). 

This repo contains the corpus files, the corpus interface and the visualization scripts. 

* For the main page of the project (with visualizations, etc) please visit the [website of the project](https://lirondos.github.io/discursos-de-navidad/) (in Spanish).
* For information about the Christmas speech see [Wikipedia's page about the Christmas Eve National Speech](https://en.wikipedia.org/wiki/Christmas_Eve_National_Speech). 
* A previous version of this project (with speeches only from 1975 on) can be found [here](https://github.com/lirondos/orgulloysatisfaccion).
* This project was featured in Spanish newspaper *eldiario.es* on December 2019. [See the article (in Spanish)](https://www.eldiario.es/sociedad/Comunismo-Union-Europea-evolucionado-Navidad_0_977452464.html) 

This repo includes: 
1. the texts of the speeches
2. a Python interface using `NLTK` and `spaCy` to query the corpus 
3. a set of HTML visualizations using `scattertext` libraries. (see [HTML visualizations](https://lirondos.github.io/discursos-de-navidad/) [in Spanish]).

The repo contains the following files: 
* The `data` folder contains the files with the Christmas speeches from 1937 to 2018 in `txt` format and the metadata associated with every speech (year, speaker, URL were it was retrieved).
* The `Speech` class creates the object Speech with the information for a given speech.
* The `Corpus` class creates the corpus object that contains the speeches to be analyzed. This class uses the files inside the `speeches` folder. This file also contain the methods to perform the lexical analysis of the created corpus.
* The `visualize.py` script creates interactive HTML visualization from TF-IDF measures using `scattertext` library. The visualization files are stored inside the visualization folder.

The files that have a main method than can be executed are: 
* `corpus.py` (creates several corpus objects for different time periods of time and calls the radiography method in order to get their lexical analysis)
* `visualize.py` (creates an instance of the corpus class and generates several visualization files with TF-IDF measures using the scattertext library)

The file `requirements.txt` contains the libraries required to run the program. After installing the repo, just run the following command: 
`pip install -r requirements.txt`


