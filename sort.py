#!/usr/bin/env python3
from argparse import ArgumentParser

from eilpx.sort import main


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('in_path')
    parser.add_argument('--threshold', default=100, type=int)
    parser.add_argument('--sort-len', default=100, type=int)
    parser.add_argument('--light', default=False, action='store_true')
    parser.add_argument('--iterations', default=1, type=int)
    args = parser.parse_args()
    main(args)
