# -*- coding: utf-8 -*-
import os

import sklearn.datasets
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk.stem

_home_path = os.path.expanduser('~')
MLCOMP_DIR = os.path.join(_home_path, 'data')

groups = [
    'comp.graphics',
    'comp.os.ms-windows.misc',
    'comp.sys.ibm.pc.hardware',
    # 'comp.sys.mac.hardware',
    'comp.windows.x',
    'sci.space',
]

train_data = sklearn.datasets.load_mlcomp('20news-18828', 'train', mlcomp_root=MLCOMP_DIR, categories=groups)
test_data = sklearn.datasets.load_mlcomp('20news-18828', 'test', mlcomp_root=MLCOMP_DIR, categories=groups)

# print len(train_data.filenames)
# print len(test_data.filenames)


english_stemmer = nltk.stem.SnowballStemmer('english')


class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))


vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=0.5, stop_words='english', decode_error=u'ignore')

x = vectorizer.fit_transform(train_data.data)

num_samples, num_features = x.shape

print 'train_data samples: %s, features: %s' % (num_samples, num_features)
