# -*- coding: utf-8 -*-
import os
# import chardet

import numpy as np
from sklearn import neighbors

from sklearn.naive_bayes import MultinomialNB

from stemmed_vec import StemmedCountVectorizer


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

    print '-----------------------------'
    print X.shape, Y.shape
    print '-----------------------------'

    classifier = MultinomialNB()
    classifier.fit(X, Y)
    return classifier


def build_model(X, Y):
    return knn_model(X, Y)
    # return naive_bayes_model(X, Y)


def extract_features_from_body(s):
    # [[len(text), text.count('\n')] for text in s]
    data = [text.decode('ISO-8859-2') for text in s]

    vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english')
    x = vectorizer.fit_transform(data)
    print type(x)
    print x.shape
    return x


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

    # train_X, train_Y = load_data('train')
    # test_X, test_Y = load_data('test')

    data_x, data_y = load_data('raw')

    train_X, train_Y = data_x[:4119], data_y[:4119]
    test_X, test_Y = data_x[4119:], data_y[4119:]

    model = build_model(train_X, train_Y)

    print '-----------------------------'
    print test_X.shape, test_Y.shape
    print '-----------------------------'

    # print model.predict(test_X)
    print model.score(test_X, test_Y)


if __name__ == '__main__':
    main()
