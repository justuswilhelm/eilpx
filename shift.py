#!/usr/bin/env python3
from argparse import ArgumentParser

from eilpx.shift import main


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('in_path')
    parser.add_argument('--iterations', type=int, default=1)
    args = parser.parse_args()
    main(args)
