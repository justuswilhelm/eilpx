"""Eilpx."""
from os import path

import numpy as np
from PIL import Image


def read_file(in_path):
    return np.asarray(Image.open(in_path), dtype=np.uint8)


def write_file(out_path, img, args):
    Image.fromarray(img).save(out_path, "PNG")


def to_out_path(in_path):
    file_name, ext = path.splitext(in_path)
    return "{}_out{}".format(file_name, ext)


def transpose_img(img):
    """Transpose an image."""
    return img.transpose(1, 0, 2)
