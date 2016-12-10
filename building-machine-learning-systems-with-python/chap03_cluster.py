# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp

vectorizer = CountVectorizer(min_df=1)

content = [
    'This is a toy post about machine learning. Actually, it contains not much interesting stuff.',
    'Imaging database can get huge.',
    'Most imaging databases safe images permanently.',
    'Imaging databases store images.',
    'Imaging databases store images. Imaging databases store images. Imaging databases store images.',
]

x = vectorizer.fit_transform(content)

num_samples, num_features = x.shape

print 'samples: %s, features: %s' % (num_samples, num_features)

print vectorizer.get_feature_names()

new_post = 'imaging databases'
new_post_vec = vectorizer.transform([new_post])

print new_post_vec
print new_post_vec.toarray()


def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())
