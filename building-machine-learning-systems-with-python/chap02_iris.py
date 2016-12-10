# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
# import numpy as np

# http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
from sklearn.datasets import load_iris

# Bunch: Dictionary-like object
# ['DESCR', 'data', 'feature_names', 'target', 'target_names']
data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']


# plot feature 0, feature 1
for t, marker, c in zip(xrange(3), '>ox', 'rgb'):
    plt.scatter(features[target == t, 0],
                features[target == t, 1],
                marker=marker,
                c=c)

plt.show()
