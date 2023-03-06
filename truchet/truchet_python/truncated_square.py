import math
from grid import SquareGrid
from polygon import Polygon

class TruncatedSquareTiling(SquareGrid):
    NAME = "truncated_square"
    TILES = [
        Polygon(
            n=8,
            color=(255,255,200),
            x_scale=2.4142136081148453, # cot(pi/8)
            x_shift=0,
            y_scale=2.4142136081148453,
            y_shift=0,
            rotate_degrees=45/2
        ),
        Polygon(
            n=4,
            color=(255,200,255),
            x_scale=2.4142136081148453,
            x_shift=2.4142136081148453/2,
            y_scale=2.4142136081148453,
            y_shift=2.4142136081148453/2,
            rotate_degrees=0
        ),
    ]

TruncatedSquareTiling(side_length=300).draw(rows=5,columns=5)
