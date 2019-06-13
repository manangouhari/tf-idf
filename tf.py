
from collections import Counter, defaultdict

from stringmanip import clean_sentence


def get_tf_words(words, words_count, words_len):
    """
    Returns the tf value of all words.
    tf[word] = total appearances of the word / total words
    """
    tf = defaultdict(float)
    for word in words_count:
        tf[word] = words_count[word] / words_len
    return tf

def get_tf_sentences(sentences, tf_words):
    """
    Returns the tf value of each sentence.
    tf[sentence] = sum(tf of words in s) / total words in s
    """
    tf = defaultdict(float)
    for sentence in sentences:
        words_in_s = clean_sentence(sentence)
        tf[sentence] = sum(tf_words[word] for word in words_in_s)/len(words_in_s)
    return tf
