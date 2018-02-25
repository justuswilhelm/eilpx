"""."""
import numpy

from eilpx import shift


def test_shift_by():
    img = numpy.asarray([
        [
            [1, 2, 3],
            [1, 2, 4],
        ],
    ])
    assert numpy.array_equal(
        shift.shift_by(0, img),
        img,
    )

    expected = [
        [
            [1, 2, 4],
            [1, 2, 3],
        ],
    ]

    assert shift.shift_by(1, img, 2).tolist() == expected
