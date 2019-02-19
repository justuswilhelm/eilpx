#!/usr/bin/env python3
from argparse import ArgumentParser

from eilpx.move import main


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('in_path')
    parser.add_argument('--amount', type=int, default=10)
    parser.add_argument('--size', type=int, default=100)
    args = parser.parse_args()
    main(args)
