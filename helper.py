from collections import Counter

def get_word_count(words):
    """
    Returns a counter of all the words
    and the total number of words.
    """
    #creating counter of words
    counter = Counter(words)
    #calculating total number of words using generators
    words_len = sum(counter[i] for i in counter)
    return (counter, words_len)
    
