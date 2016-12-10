# -*- coding: utf-8 -*-
import sys

# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy as sp
import nltk.stem


english_stemmer = nltk.stem.SnowballStemmer('english')


class StemmedCountVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(StemmedCountVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))


# vectorizer = CountVectorizer(min_df=1, stop_words='english')
vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')

content = [
    'This is a toy post about machine learning. Actually, it contains not much interesting stuff.',
    'Imaging database can get huge.',
    'Most imaging databases safe images permanently.',
    'Imaging databases store data.',
    'Imaging databases store data. Imaging databases store data. Imaging databases store data.',
]

x = vectorizer.fit_transform(content)

num_samples, num_features = x.shape

print 'samples: %s, features: %s' % (num_samples, num_features)

# print vectorizer.get_feature_names()

new_post = 'imaging databases'
new_post_vec = vectorizer.transform([new_post])

# print new_post_vec
# print new_post_vec.toarray()


def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())


def dist_norm(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())
    delta = v1_normalized - v2_normalized
    return sp.linalg.norm(delta.toarray())


def dist_alg(v1, v2):
    return dist_norm(v1, v2)


best_post = None
best_dist = sys.maxint
best_i = None


for i in range(num_samples):
    post = content[i]

    if post == new_post:
        # leave one out alg.
        continue

    post_vec = x.getrow(i)

    d = dist_alg(post_vec, new_post_vec)

    print '=== Post %s with dist=%.2f: %s' % (i, d, post)

    if d < best_dist:
        best_dist = d
        best_i = i
        best_post = post

print 'Best Post is %s with dist=%.2f: %s' % (best_i, best_dist, best_post)
