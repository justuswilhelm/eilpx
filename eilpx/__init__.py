"""Eilpx."""
from os import path

import numpy as np
from PIL import Image
from tqdm import tqdm


def read_file(in_path):
    return np.asarray(Image.open(in_path), dtype=np.uint8)


def find_consecutive_values(img):
    ranges = []
    inside = False
    end = None
    for y, row in enumerate(img):
        for x, c in enumerate(row):
            if c:
                if not inside:
                    start = x
                    inside = True
                end = x
            elif inside:
                ranges.append((y, start, end))
                inside = False
    return ranges


def get_spots(img, args):
    mean = np.mean(img, axis=2)
    if args.light:
        return mean > args.threshold
    else:
        return mean < args.threshold


def sort_img(img, spots, args):
    """Sort an image at spots, in-place."""

    ranges = find_consecutive_values(spots)
    for (y, x_start, x_end) in tqdm(ranges):
        img[y, x_start:x_end + 1 + args.sort_len].sort(axis=0)


def write_file(out_path, img, args):
    Image.fromarray(img).save(out_path, "PNG")


def main(args):
    in_path = args.in_path
    file_name, ext = path.splitext(in_path)
    out_path = "{}_out{}".format(file_name, ext)
    img = read_file(in_path).copy()

    spots = get_spots(img, args)
    sort_img(img, spots, args)

    img = img.transpose(1, 0, 2)

    spots = get_spots(img, args)
    sort_img(img, spots, args)

    img = img.transpose(1, 0, 2)

    write_file(out_path, img, args)
