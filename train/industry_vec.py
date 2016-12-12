# -*- coding: utf-8 -*-
import os

import numpy as np


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


def main():
    train_data = fetch_data('379', 'train', mlcomp_root=MLCOMP_DIR, categories=groups)
    # test_data = load_data('379', 'test', mlcomp_root=MLCOMP_DIR, categories=groups)

    dataset = []
    targets = []

    for target_name, data in train_data:
        dataset.append(data)
        targets.append(target_name.endswith('hardware'))

    Y = np.asarray(targets)

    print Y


if __name__ == '__main__':
    main()
