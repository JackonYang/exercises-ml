# -*- coding: utf-8 -*-
import random
from captcha.image import ImageCaptcha
from PIL import Image
import numpy as np


def gen_captcha():
    code = random.randint(0, 10)
    image = ImageCaptcha()
    filename = 'img/%s.png' % code
    image.write(str(code), filename)
    return code, filename


def load_img(img_filename):
    return np.array(Image.open(img_filename).convert('L'))


# data = data.reshape(num_images, rows, cols, 1)


def main():
    code, filename = gen_captcha()
    im = load_img(filename)

    print im.shape


if __name__ == '__main__':
    main()
