# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem


english_stemmer = nltk.stem.SnowballStemmer('english')


class StemmedCountVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))
