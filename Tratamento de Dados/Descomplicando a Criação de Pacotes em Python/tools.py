from PIL import Image
import numpy as np
from collections import Counter


def open_img(img):
    """
    :return: An :py:class:`~PIL.Image.Image` object.

    read an image
    """
    img = Image.open(img)
    return img


def equal(img1, img2):
    """
    :return: bool

    equality between two images
    """
    img1 = img1.resize((1920, 1080))
    img2 = img2.resize((1920, 1080))
    array1 = np.asarray((img1))
    array2 = np.asarray((img2))
    array1 = Counter(array1.flatten())
    array2 = Counter(array2.flatten())
    if array1 == array2:
        return True
    else:
        return False
