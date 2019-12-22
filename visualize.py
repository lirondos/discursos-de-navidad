from corpus import Corpus
import corpus
import pandas as pd
import scattertext as st
import spacy
from spacy.lang.es.stop_words import STOP_WORDS
nlp = spacy.load('es_core_news_sm', disable=['parser', 'ner', 'textcat'])
nlp.add_pipe(nlp.create_pipe('sentencizer'))
nlp.max_length = 1500000
#nlp = spacy.load('es')

"""
This scripts interact with Corpus class and scattertext library to produce html visualization of the corpus.
The produced html files can be found in the visualization folder.
This proccess can take a while to be done.
"""


def create_visual_corpus(category, speeches_df):
    """
    creates scattertext corpus from speeches dictionary
    :param category:
    :param speeches_df:
    :return:
    """
    corpus = st.CorpusFromPandas(speeches_df, category_col=category, text_col='text', nlp=nlp).build()
    update_stop = []
    STOP_WORDS.update(["»","—", "«", "cuyas", "cuyos", "100", "fué", "ido", "hubieran", "hagan", "–", "hubiera"])
    for term in STOP_WORDS:
        if term in corpus._term_idx_store:
            update_stop.append(term)
    corpus = corpus.remove_terms(update_stop)
    return corpus

def print_graph(corpus, speeches_df, category, type, not_type):
    """
    :param corpus:
    :param speeches_df:
    :param category:
    :param type:
    :param not_type:
    :return: produces html file with corpus visualization
    """
    if type == "1":
        type = "Dictatorship"
        not_type = "Democracy"
    if type == "2":
        type = "Democracy"
        not_type = "Dictatorship"
    if type == "Francisco Franco":
        not_type = "Borbones"
    html = st.produce_scattertext_explorer(corpus, category=type, category_name=type, not_category_name=not_type, width_in_pixels=1000, metadata=speeches_df[category])
    open("./visualization/visualization_" + type + ".html", 'wb').write(html.encode('utf-8'))

def get_type_list(category, speeches_dict):
    """
    :param category:
    :param speeches_dict:
    :return: list of the values for different categories (time, half, king)
    """
    values = []
    for dict in speeches_dict:
        value = dict.get(category)
        values.append(value)
    return list(set(values))

def get_visualization(category, my_corpus):
    """
    General method that takes a corpus and a category to divide the corpus and creates visualization files
    """
    speeches_dict = my_corpus.to_speeches_list()
    speeches_df = pd.DataFrame(speeches_dict)
    visual_corpus = create_visual_corpus(category, speeches_df)
    types = get_type_list(category, speeches_dict)
    if(len(types) == 2):
        print_graph(visual_corpus, speeches_df, category, types[0], types[1])
    else:
        for type in types:
            print_graph(visual_corpus, speeches_df, category, type, "Not " + type)


if __name__ == '__main__':
    """
    This main method creates a corpus instance from the corpus class.
    It then creates visualizations based on three features: period of time, king and half of the corpus
    (first half are speeches before 1977 (dictatorship period); second half are speeches after 1978 (democracy))

    """

    my_corpus = Corpus([])
    categories = ['period', 'king', 'half']
    for category in categories:
        get_visualization(category, my_corpus)


