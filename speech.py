import nltk
import spacy
from nltk.collocations import ngrams
from spacy.lang.es.stop_words import STOP_WORDS

# stop-words to be added to the spaCy STOP_WORDS set
STOP_WORDS.remove('arriba')
STOP_WORDS.add('a')
STOP_WORDS.add('y')
STOP_WORDS.add('e')
STOP_WORDS.add('o')
STOP_WORDS.add('que')
STOP_WORDS.add('el')
STOP_WORDS.add('la')
STOP_WORDS.add('nos')
STOP_WORDS.add('todos')
STOP_WORDS.add('hemos')
STOP_WORDS.add('estos')
STOP_WORDS.add('pero')
STOP_WORDS.add('cuando')
STOP_WORDS.add('otro')
STOP_WORDS.add('dentro')
STOP_WORDS.add('he')
STOP_WORDS.add('cada')
STOP_WORDS.add('tal')
STOP_WORDS.add('cuyo')
STOP_WORDS.add('cuya')


nlp = spacy.load('es_core_news_sm', disable=['parser', 'ner', 'textcat'])
nlp.max_length = 1500000


class Speech:
    """
    The Speech class creates a speech object that contains relevant info of a given speech
    """
    def __init__(self, text, words, sents, par, year, head_of_state, half, period):
        self.raw_text = text
        self.tokens = [word.lower() for word in words if word.isalpha()]
        self.types = list(set(self.tokens))
        self.sents = sents
        self.par = par
        self.tagged_text, self.lemmatized_text = tag_text(text)
        self.text = nltk.Text([word.lower() for word in words])
        self.year = year
        self.head_of_state = head_of_state
        self.half = half
        self.period = period

    def length(self):
        """
        :return: length of token list (only alphabetic words are considered, not punctuation or numbers)
        """
        return len(self.text.tokens)
    
    def content_words(self):
        """
        :return: content words in the corpus
        """
        return [word.lower() for word in self.tokens if word.isalpha() and word.lower() not in STOP_WORDS]

    def bigrams(self):
        """
        :return: bigrams in the corpus
        """
        return list(nltk.bigrams(self.tokens))
    
    def content_bigrams(self):
        """
        :return: content bigrams in the corpus
        """
        bigrams = self.bigrams()
        return [(x, y) for (x, y) in bigrams if x.isalpha() and x.lower() not in STOP_WORDS and y.isalpha() and y.lower() not in STOP_WORDS]

    def trigrams(self):
        """
        :return: trigrams in the corpus
        """
        return ngrams(self.tokens, 3)
        
    def content_trigrams(self):
        """
        :return: content trigrams in the corpus. The middle word (word2) can be a stopword.
        """
        trigrams = self.trigrams()
        return [(x, y, z) for (x, y, z) in trigrams if
                                 x.isalpha() and x.lower() not in STOP_WORDS and y.isalpha() and z.isalpha() and z.lower() not in STOP_WORDS]

    def longest_words(self):
        """
        :return: alphabetized list of the longest word(s) in this corpus.
        """
        longest_len = max(len(word) for word in self.tokens)
        longest_list = [word for word in set(self.tokens) if len(word) == longest_len]
        longest_list.sort()
        return longest_list

    def frequencies(self):
        """
        :return: frequency distribution of all words in the corpus
        """
        fd = nltk.FreqDist(self.text)
        return fd.most_common(50)

    def most_frequent_content_words(self):
        """
        :return: Frequency distribution of words in the corpus.
        """
        content_words = self.content_words()
        freqdist = nltk.FreqDist(content_words)
        return freqdist.most_common(50)

    def most_frequent_bigrams(self):
        """
        :return: Frequency distribution of content bigrams in the corpus
        """
        content_bigrams = self.content_bigrams()
        freqdist = nltk.FreqDist(content_bigrams)
        return freqdist.most_common(50)

    def most_frequent_trigrams(self):
        """
        :return: Frequency distribution of content trigrams in the corpus
        """
        content_trigrams = self.content_trigrams()
        freqdist = nltk.FreqDist(content_trigrams)
        return freqdist.most_common(50)

    def hapaxes(self):
        """
        :return: hapaxes in the corpus
        """
        fd = nltk.FreqDist(self.text)
        return fd.hapaxes()


    def frequency(self, word):
        """
        :param word:
        :return: frequency of a given word in the corpus
        """
        fd = nltk.FreqDist(self.text)
        return fd[word]


    def word_appearances(self, word):
        """
        :param word:
        :return: number of times the word appears in the corpus
        """
        return self.tokens.count(word)

    def concordance(self, word):
        """
        :param word:
        :return: concordances for the given word in the corpus
        """
        return self.text.concordance(word)

    def similar(self, word):
        """
        :param word:
        :return: words in the corpus that appear in similar contexts
        """
        return self.text.similar(word)

    def dispersion_plot(self, my_words):
        """
        :param my_words:
        :return: dispersion plot for a set of words in the corpus
        """
        self.text.dispersion_plot(my_words)

    def speech_to_dict(self):
        """
        :return: turns speech to dictionary element.
        """
        speech_dict = dict()
        speech_dict['year'] = self.year
        speech_dict['half'] = self.half
        speech_dict['king'] = self.head_of_state
        speech_dict['period'] = self.period
        speech_dict['text'] = self.raw_text
        return speech_dict


def tag_text(text):
    """
    tags and lemmatizes text using the spaCy library
    :param text:
    :return: tagged_text, lemmatized_text
    """
    doc = nlp(text.encode('utf-8').decode('utf-8'))
    lemmas = [token.lemma_ for token in doc]
    tagged_words = [token.text + '/' + token.pos_ for token in doc]
    lemmatized_text = str(" ".join(lemmas))
    tagged_text = " ".join(tagged_words)
    return tagged_text, lemmatized_text


