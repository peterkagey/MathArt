import math
from grid import SquareGrid
from polygon import Polygon

class SnubSquareTiling(SquareGrid):
    NAME = "snub_square"
    TILES = [
        Polygon(
            n=4,
            color=(200,222,255),
            x_scale=math.sqrt(2+math.sqrt(3)),
            x_shift=0,
            y_scale=math.sqrt(2+math.sqrt(3)),
            y_shift=0,
            rotate_degrees=30
        ),
        Polygon(
            n=4,
            color=(200,255,222),
            x_scale=math.sqrt(2+math.sqrt(3)),
            x_shift=math.sqrt(2+math.sqrt(3))/2,
            y_scale=math.sqrt(2+math.sqrt(3)),
            y_shift=math.sqrt(2+math.sqrt(3))/2,
            rotate_degrees=-30
        ),
        Polygon(
            n=3,
            color=(222,200,255),
            x_scale=math.sqrt(2+math.sqrt(3)),
            x_shift=1/math.sqrt(8)+1/math.sqrt(6),
            y_scale=math.sqrt(2+math.sqrt(3)),
            y_shift=1/math.sqrt(24),
            rotate_degrees=-15
        ),
        Polygon(
            n=3,
            color=(222,255,200),
            x_scale=math.sqrt(2+math.sqrt(3)),
            x_shift=1/math.sqrt(8)+2/math.sqrt(6),
            y_scale=math.sqrt(2+math.sqrt(3)),
            y_shift=1/math.sqrt(24)-1/math.sqrt(6),
            rotate_degrees=45
        ),
        Polygon(
            n=3,
            color=(255,200,255),
            x_scale=math.sqrt(2+math.sqrt(3)),
            x_shift=-1/math.sqrt(24),
            y_scale=math.sqrt(2+math.sqrt(3)),
            y_shift=1/math.sqrt(8)+1/math.sqrt(6),
            rotate_degrees=15
        ),
        Polygon(
            n=3,
            color=(255,255,200),
            x_scale=math.sqrt(2+math.sqrt(3)),
            x_shift= -1/math.sqrt(24) + 1/math.sqrt(6),
            y_scale=math.sqrt(2+math.sqrt(3)),
            y_shift=1/math.sqrt(8)+2/math.sqrt(6),
            rotate_degrees=75
        ),
    ]

SnubSquareTiling(side_length=300).draw(rows=6, columns=6)
