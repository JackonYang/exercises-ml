# -*- coding: utf-8 -*-
import random
from captcha.image import ImageCaptcha


def gen_captcha():
    code = random.randint(0, 10)
    image = ImageCaptcha()
    filename = 'img/%s.png' % code
    image.write(str(code), filename)
    return code, filename


# data = data.reshape(num_images, rows, cols, 1)


if __name__ == '__main__':
    print gen_captcha()
