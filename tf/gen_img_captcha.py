# -*- coding: utf-8 -*-
import random
from captcha.image import ImageCaptcha
from PIL import Image
import numpy as np


def gen_captcha(num):
    code = ''.join(map(lambda x: str(random.randint(0, 9)), range(num)))
    image = ImageCaptcha()
    filename = 'img/%s.png' % code
    image.write(str(code), filename)
    return code, filename


def load_img(img_filename):
    data = np.array(Image.open(img_filename).convert('L'))
    w, h = data.shape
    one_d = data.reshape((1, w * h))
    return one_d


def num_to_one_hot(number):
    one_hot = np.zeros((10,))
    one_hot[int(number) - 1] = 1
    return one_hot


def read_data(count, length):
    for i in range(count):
        code, filename = gen_captcha(length)

        code_vec = num_to_one_hot(code)
        im = load_img(filename)
        yield code_vec, im


def load_inputs(count=77, length=1):
    codes = []
    imgs = []
    for code, im in read_data(count, length):
        codes.append(code)
        imgs.append(im)

    return np.vstack(imgs), np.vstack(codes)


if __name__ == '__main__':
    print load_inputs()
