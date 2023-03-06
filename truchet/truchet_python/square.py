import math
from grid import SquareGrid
from polygon import Polygon

class SquareTiling(SquareGrid):
    NAME = "square"
    TILES = [
        Polygon(
            n=4,
            color=(200,222,255),
            x_scale=1,
            x_shift=0,
            y_scale=1,
            y_shift=0,
            rotate_degrees=45
        )
    ]

SquareTiling(side_length=200).draw(columns=11, rows=11, canvas_width=2000, canvas_height=2000)
