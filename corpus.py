from speech import Speech
import nltk
from nltk.corpus import PlaintextCorpusReader
import os


class Corpus:
    """
    The Corpus class creates a corpus, that is a set of speeches to be analyzed.
    The constructor takes a list of files from the speeches folder as parameter.
    Example. ["1977.txt", "1980.txt"]
    If the list is empty, the corpus is created with the complete collection of speeches (from 1975 to 2017)
    """
    def __init__(self, files):
        if not files:
            self.corpus = PlaintextCorpusReader('./data/speeches', '.*')
        else:
            self.corpus = PlaintextCorpusReader('./data/speeches', files)
        self.speech = Speech(self.corpus.raw(), self.corpus.words(), self.corpus.sents(),self.corpus.paras(), None, None, None, None)
        self.speeches = build_speeches_dict(self.corpus)
        self.years = [int(year.split('.')[0]) for year in self.corpus.fileids()]
        complementary_years = list(set(os.listdir("./data/speeches")) - set([str(years) + '.txt' for years in self.years]))
        if not files:
            self.complementary = None
            self.unique_words = None
        else:
            self.complementary = ComplementaryCorpus(complementary_years)
            self.unique_words = [word for word in self.speech.tokens if word not in self.complementary.speech.tokens]

    def to_speeches_list(self):
        speeches_list = []
        for key,speech in self.speeches.items():
            speeches_list.append(speech.speech_to_dict())
        return speeches_list

    def print_graph(self, my_words):
        """
        :param my_words: list of words whose frequency is to be plotted
        :return: a frequency plot
        """
        cfd = nltk.ConditionalFreqDist((target, fileid) for fileid in self.speeches.keys() for w in self.speeches[fileid].tokens for target in my_words if w.lower() == target)
        cfd.plot()

    def get_files(self):
        """
        :return: list of files in the Corpus object
        """
        return self.corpus.fileids()

    def unique_words_freq(self):
        """
        :return: the words in the corpus object that are unique to that corpus
        (i.e., these words dont appear in the rest of the speeches)
        """
        if self.unique_words is None:
            return "The corpus contains all speeches, so no comparison can be made"
        else:
            return nltk.FreqDist(self.unique_words).most_common(50)

    def radiography(self):
        """
        The method that returns the lexical radiography of the corpus
        :return: prints lexical analysis from the corpus
        """
        print("Lexical data for period from " + str(self.years[0]) + " to " + str(self.years[-1]))
        print(str(len(self.years)) + " total speeches")
        print(str(len(self.corpus.words())) + " total words")
        print(str(len(self.corpus.words()) / len(self.get_files())) + " words per speech")
        print("Frequency distribution:")
        print(self.speech.frequencies())
        print("Content words frequency distribution:")
        print(self.speech.most_frequent_content_words())
        print("Unique words frequency distribution:")
        print(self.unique_words_freq())
        print("Most frequent content bigrams:")
        print(self.speech.most_frequent_bigrams())
        print("Most frequent content trigrams:")
        print(self.speech.most_frequent_trigrams())
        print("#######################################")


class ComplementaryCorpus(Corpus):
    """
    The ComplementaryCorpus is a type of corpus.
    The ComplementaryCorpus is created when the corpus only contains a selection of speeches (not all of them)
    The Complementary Corpus is a corpus that contains the speeches not included in the current corpus.
    """
    def __init__(self, files):
        Corpus.corpus = PlaintextCorpusReader('./data/speeches', files)
        Corpus.speech = Speech(self.corpus.raw(), self.corpus.words(), self.corpus.sents(), self.corpus.paras(), None, None, None, None)
        Corpus.speeches = None
        Corpus.years = [int(year.split('.')[0]) for year in self.corpus.fileids()]
        Corpus.complementary = None


def build_speeches_dict(corpus):
    """
    Transform a corpus into a dictionary of speeches. This method is used in the visualization process
    :param corpus:
    :return: speeches dictionary
    """
    speeches = dict()
    for fileid in corpus.fileids():
        text = corpus.raw(fileid)
        words = corpus.words(fileid)
        sents = corpus.sents(fileid)
        par = corpus.paras(fileid)
        year = int(fileid.split('.')[0])
        head_of_state = get_head_of_state(year)
        half = get_half(year)
        period = get_period(year)
        my_speech = Speech(text, words, sents, par, year, head_of_state, half, period)
        speeches[year] = my_speech
    return speeches


def get_head_of_state(year):
    """
    Sets the head_of_state of the speech based on the year the speech was delivered.
    :param year:
    :return: name of the head_of_state
    """
    if year<1975:
        return "Francisco Franco"
    if year>= 1975 and year < 2014 :
        return "Juan Carlos"
    else:
        return "Felipe"

def get_half(year):
    """
    Sets the half of time when the speech was delivered.
    :param year:
    :return: 1 (for first half) and 2 (second half)
    """
    if (year < 1978):
        return "Dictatorship"
    else:
        return "Democracy"


def get_period(year):
    """
    Sets the historical period of the speech based on the year it was delivered
    :param year:
    :return: Historical period
    """
    if year <= 1939:
        return "Civil War"
    elif (year >= 1940 and year < 1960):
        return "Early-Francoism"
    elif (year >= 1960 and year < 1975):
        return "Late-Francoism"
    elif (year >= 1975 and year < 1982):
        return "Transition"
    elif (year>=1982 and year<1996):
        return "Socialism"
    elif(year >= 1996 and year < 2008):
        return "Bubble"
    elif(year>=2008 and year < 2020):
        return "Recession"
    elif(year>=2020):
        return "2020"


def create_corpus(first_year, last_year):
    """
    Method to call the corpus constructor to build a corpus for a consecutive set of years
    :param first_year:
    :param last_year: included
    :return: the created corpus
    """
    files = []
    for year in range(first_year, last_year + 1):
        file_name = str(year) + '.txt'
        if os.path.isfile("data/speeches/"+file_name):
            files.append(file_name)
        else:
            print("No speech for year " + str(year))
    corpus = Corpus(files)
    return corpus

if __name__ == '__main__':
    """
    This main method:
    - creates a corpus with all the speeches in the folder
    - calls the radiography method to get lexical information from the created corpus
    
    After that, a corpus object is created for every historical period of the corpus (four corpus, one for every period)
    The radiography method is called on each of them. 
    The result for this main method can be found on the output.txt file
    """
    general = Corpus([])
    general.radiography()

    my_corpora = [create_corpus(1937, 1974), create_corpus(1975, 2013), create_corpus(2014, 2019), create_corpus(2020, 2020)]
    for corpus in my_corpora:
        corpus.radiography()




