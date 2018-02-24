#!/usr/bin/env python3
from argparse import ArgumentParser
from os import path

import numpy as np
from PIL import Image
from tqdm import tqdm


def read_file(in_path):
    return np.asarray(Image.open(in_path), dtype=np.uint8)


def sort_img(img, args):
    if args.light:
        spots = np.mean(img, axis=2) > args.threshold
    else:
        spots = np.mean(img, axis=2) < args.threshold

    for y, y_row in tqdm(enumerate(spots), total=img.shape[0]):
        for x, x_row in enumerate(y_row):
            if not x_row:
                continue
            img[y, x:x + args.sort_len].sort(axis=0)
            img[y:y + args.sort_len, x].sort(axis=0)


def write_file(out_path, img, args):
    if args.jpeg_bork:
        kwargs = {
            'quality': 10,
        }
    else:
        kwargs = {}
    Image.fromarray(img).save(out_path, "JPEG", **kwargs)


def main(args):
    in_path = args.in_path
    file_name, ext = path.splitext(in_path)
    out_path = "{}_out{}".format(file_name, ext)
    img = read_file(in_path).copy()
    sort_img(img, args)
    write_file(out_path, img, args)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('in_path')
    parser.add_argument('--threshold', default=100, type=int)
    parser.add_argument('--sort-len', default=100, type=int)
    parser.add_argument('--light', default=False, action='store_true')
    parser.add_argument('--jpeg-bork', default=False, action='store_true')
    args = parser.parse_args()
    main(args)
