# -*- coding: utf-8 -*-
import sys

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

# print 'samples: %s, features: %s' % (num_samples, num_features)

# print vectorizer.get_feature_names()

new_post = 'imaging databases'
new_post_vec = vectorizer.transform([new_post])

# print new_post_vec
# print new_post_vec.toarray()


def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())


best_post = None
best_dist = sys.maxint
best_i = None


for i in range(num_samples):
    post = content[i]

    if post == new_post:
        # leave one out alg.
        continue

    post_vec = x.getrow(i)

    d = dist_raw(post_vec, new_post_vec)

    print '=== Post %s with dist=%.2f: %s' % (i, d, post)

    if d < best_dist:
        best_dist = d
        best_i = i
        best_post = post

print 'Best Post is %s with dist=%.2f: %s' % (best_i, best_dist, best_post)
