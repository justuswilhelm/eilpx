"""."""
import numpy as np

import eilpx


def test_consecutive_values():
    inp = [
        [True, True, False],
        [False, True, False],
    ]
    assert eilpx.find_consecutive_values(inp) == [
        (0, 0, 1),
        (1, 1, 1),
    ]


def test_sort_img():
    img = np.array(
        [
            [1, 2, 1, 0],
        ],
    )
    spots = [
        [True, True, True, False],
    ]
    eilpx.sort_img(
        img,
        spots,
    )
    assert img.tolist() == [
        [1, 1, 2, 0],
    ]
