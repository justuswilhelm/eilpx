"""."""
import numpy as np

from eilpx import sort


def test_consecutive_values():
    inp = [
        [True, True, False],
        [False, True, False],
    ]
    assert sort.find_consecutive_values(inp) == [
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
    sort.sort_img(
        img,
        spots,
    )
    assert img.tolist() == [
        [1, 1, 2, 0],
    ]
