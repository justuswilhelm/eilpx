"""Functions for shift."""
import numpy
import tqdm

import eilpx


def do(img, size=100, step=3, iterations=100, amount=10):
    """Shift image color axis by 'by'."""
    x_points = numpy.random.randint(0, img.shape[1] - 1, amount)
    y_points = numpy.random.randint(0, img.shape[0] - 1, amount)
    for mx, my in tqdm.tqdm(list(zip(x_points, y_points))):
        dx, dy = numpy.random.choice([-step, step], size=2)
        src_x1, src_y1 = mx - size // 2, my - size // 2
        src_x2, src_y2 = mx + size // 2, my + size // 2
        for i in tqdm.trange(1, iterations + 1):
            step_x = dx * i
            step_y = dy * i
            dst_x1 = mx + step_x - size // 2
            dst_y1 = my + step_y - size // 2
            dst_x2 = mx + step_x + size // 2
            dst_y2 = my + step_y + size // 2
            try:
                img[dst_y1:dst_y2, dst_x1:dst_x2] = img[
                    src_y1:src_y2, src_x1:src_x2
                ]
            except ValueError:
                break

    return img


def main(args):
    in_path = args.in_path
    img = eilpx.read_file(in_path).copy()

    img = do(img, amount=args.amount, size=args.size)
    eilpx.write_file(eilpx.to_out_path(in_path), img)
