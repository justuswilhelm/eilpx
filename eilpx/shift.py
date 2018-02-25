"""Functions for shift."""
import numpy
import tqdm

import eilpx
from eilpx import sort


def shift_by(img, threshold=128):
    """Shift image color axis by 'by'."""
    a, b = 1, 128
    span = 127
    x = len(img) // b * a
    y = x + len(img) // b * span

    part = img[x:y].reshape(span, -1)
    spots = part < threshold
    sort.sort_img(part, spots)
    img[x:y] = part.flatten()

    return img


def main(args):
    in_path = args.in_path
    img = numpy.fromfile(in_path, dtype='uint8')

    thresholds = numpy.linspace(100, 200, args.iterations, dtype='uint8')
    for threshold in tqdm.tqdm(thresholds):
        img = shift_by(img, threshold)

    img.tofile(eilpx.to_out_path(in_path))
