# -*- coding: utf-8 -*-
import os

import numpy as np
from sklearn import neighbors

from sklearn.naive_bayes import MultinomialNB


_home_path = os.path.expanduser('~')
MLCOMP_DIR = os.path.join(_home_path, 'data')

groups = [
    'comp.graphics',
    'comp.os.ms-windows.misc',
    'comp.sys.ibm.pc.hardware',
    'comp.sys.mac.hardware',
    'comp.windows.x',
    'sci.space',
]


def fetch_data(name, set_, mlcomp_root, categories=None):
    mlcomp_root = os.path.expanduser(mlcomp_root)
    mlcomp_root = os.path.abspath(mlcomp_root)
    mlcomp_root = os.path.normpath(mlcomp_root)

    dataset_path = os.path.join(mlcomp_root, name, set_)

    folders = [f for f in sorted(os.listdir(dataset_path))
               if os.path.isdir(os.path.join(dataset_path, f))]
    if categories is not None:
        folders = [f for f in folders if f in categories]

    for label, folder in enumerate(folders):
        folder_path = os.path.join(dataset_path, folder)

        documents = [os.path.join(folder_path, d)
                     for d in sorted(os.listdir(folder_path))]
        for filename in documents:
            with open(filename, 'rb') as f:
                yield folder, f.read()


def knn_model(X, Y):
    knn = neighbors.KNeighborsClassifier(n_neighbors=2)
    knn.fit(X, Y)
    return knn


def naive_bayes_model(X, Y):
    classifier = MultinomialNB()
    classifier.fit(X, Y)
    return classifier


def build_model(X, Y):
    return naive_bayes_model(X, Y)


def extract_features_from_body(s):
    return [[len(text), text.count('\n')] for text in s]


def load_data(set_):
    data = fetch_data('379', set_, mlcomp_root=MLCOMP_DIR, categories=groups)

    dataset = []
    targets = []

    for target_name, data in data:
        dataset.append(data)
        targets.append(target_name.endswith('hardware'))

    X = extract_features_from_body(dataset)
    Y = np.asarray(targets)
    return X, Y


def main():
    train_X, train_Y = load_data('train')
    test_X, test_Y = load_data('test')

    model = build_model(train_X, train_Y)

    print model.score(test_X, test_Y)


if __name__ == '__main__':
    main()
