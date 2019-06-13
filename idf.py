from stringmanip import clean_sentence
from math import log
from collections import defaultdict

def get_idf_words(words, words_count, words_len, len_sentences):
    """
    Returns idf value of each word.
    idf[word] = log(total sentences / number of times the word appears)
    """
    idf = defaultdict(float)
    for word in words_count:
        idf[word] = log(len_sentences/words_count[word], 10)
    return idf

def get_idf_sentences(sentences, idf_words):
    """
    Returns idf of each sentence.
    idf[sentence] = sum(idf of each word in sentence) / total words in sentence
    """
    idf = defaultdict(float)
    for sentence in sentences:
        words_in_s = clean_sentence(sentence)
        idf[sentence] = sum(idf_words[word] for word in words_in_s)/len(words_in_s)
    return idf
