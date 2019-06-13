# tf-idf
This repo is an implementation of TF-IDF algorithm for *document summarization*.
TF-IDF stands for Term Frequency - Inverse Document Frequency, it is a multiplication of two algorithms, term frequency and inverse document frequency.
To learn more about the algorithm, check out the following resources - 
* [Document summarization using TF-IDF](https://skerritt.blog/tfidf/)
* [Wikipedia TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
* [KD Nuggets](https://www.kdnuggets.com/2018/08/wtf-tf-idf.html)
* [Text Summarization using TF-IDF Easy implementation using Python and NLTK](https://towardsdatascience.com/text-summarization-using-tf-idf-e64a0644ace3)
--------------
TF-IDF is an algorithm applied over a set of documents, for document summarization, I considered every sentence as a separate sentence and the sentences with the highest TF-IDF score are the most informative one. 

```tf(word) = total count of word / total number of words```
```tf(sentence) = sum of tf of all non stopword words / number of non stopword words in the sentence```
```idf(word) = log(total number of sentences / total count of words)```
```idf(sentence) = sum of idf of all non stopword words / number of non stopword words in the sentence```

```tfidf(setence) = tf of sentence * idf of sentence```

To test the code, change the paragraph variable in tfidf.py, the program spits out all the sentences ranked in order of their tfidf scores, highest to lowest, i.e. most informative to least informative.
