"""Sorting related methods."""
from tqdm import tqdm
import numpy as np

import eilpx


def find_consecutive_values(img):
    """Find consecutive values in a two dimensional boolean array."""
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


def main(args):
    in_path = args.in_path
    img = eilpx.read_file(in_path).copy()

    spots = get_spots(img, args)
    sort_img(img, spots, args)

    img = eilpx.transpose_img(img)

    spots = get_spots(img, args)
    sort_img(img, spots, args)

    img = eilpx.transpose_img(img)

    eilpx.write_file(eilpx.to_out_path(in_path), img, args)
