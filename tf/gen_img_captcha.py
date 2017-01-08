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
    return np.array(Image.open(img_filename).convert('L'))


# data = data.reshape(num_images, rows, cols, 1)


def main(n):
    code, filename = gen_captcha(n)
    im = load_img(filename)

    print code
    print im.shape


if __name__ == '__main__':
    main(4)
