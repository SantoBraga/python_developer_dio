from random import randrange
from PIL import Image, ImageChops
from dreamFilter import tools


def dream_filter(img1, img2, final_img_name):
    """
    :param final_img_name: str
    :return: An :py:class:`~PIL.Image.Image` object.

    applies the dream filter to an image
    """

    r = randrange(0, 266)
    g = randrange(0, 266)
    b = randrange(0, 266)
    color = (r, g, b)
    flag = ''
    img1 = img1.resize((1920, 1080))
    img2 = img2.resize((1920, 1080))
    if tools.equal(img1, img2) is True:
        img2 = ImageChops.invert(img2)
        flag = True
    img2 = img2.rotate(180)
    img2 = img2.transpose(0)
    mask = Image.new("L", img1.size, 120)
    final_image = Image.composite(img1, img2, mask)
    mask2 = Image.new(mode="RGB", size=img1.size, color=color)
    final_image = Image.blend(final_image, mask2, alpha=0.4)
    mask3 = ImageChops.difference(img1, img2)
    final_image = Image.blend(final_image, mask3, alpha=0.2)
    if flag is True:
        final_mask = ImageChops.overlay(final_image, final_image.rotate(90, expand=True))
        final_mask = ImageChops.overlay(final_image, final_image.rotate(180))
        final_mask = ImageChops.overlay(final_image, final_image.rotate(270, expand=True))
        final_mask = final_mask.resize((1920, 1080))
        final_image = Image.blend(final_image, final_mask, 0.4)
        final_image.rotate(180)
    final_image.save(f'{final_img_name}.jpg')
    final_image.show()
