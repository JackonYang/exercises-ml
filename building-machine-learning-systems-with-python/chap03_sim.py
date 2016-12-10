# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)

content = [
    'How to format my hard disk',
    'hard disk format problems',
]

x = vectorizer.fit_transform(content)

print vectorizer.get_feature_names()

print x.toarray().transpose()
