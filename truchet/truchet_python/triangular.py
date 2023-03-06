import math
from grid import TriangularGrid
from polygon import Polygon

class TriangularTiling(TriangularGrid):
    NAME = "triangular"
    TILES = [
        Polygon(
            n=3,
            color=(255,255,200),
            x_scale=1,
            x_shift=0,
            y_scale=math.sqrt(3)/2,
            y_shift=math.sqrt(3)/6,
            rotate_degrees=90
        ),
        Polygon(
            n=3,
            color=(255,200,255),
            x_scale=1,
            x_shift=-1/2,
            y_scale=math.sqrt(3)/2,
            y_shift=0,
            rotate_degrees=-90
        )
    ]

TriangularTiling(side_length=300).draw(rows=12, columns=11)
