import math
from grid import TriangularGrid
from polygon import Polygon

class ElongatedTriangularTiling(TriangularGrid):
    NAME = "elongated_triangular"
    TILES = [
        Polygon(
            n=4,
            color=(255,255,200),
            x_scale=1,
            x_shift=0,
            y_scale=1+math.sqrt(3)/2,
            y_shift=0,
            rotate_degrees=45
        ),
        Polygon(
            n=3,
            color=(255,200,255),
            x_scale=1,
            x_shift=0,
            y_scale=1+math.sqrt(3)/2,
            y_shift=1/2+math.sqrt(3)/6,
            rotate_degrees=30
        ),
        Polygon(
            n=3,
            color=(200,255,255),
            x_scale=1,
            x_shift=-1/2,
            y_scale=1+math.sqrt(3)/2,
            y_shift=1/2+math.sqrt(3)/3,
            rotate_degrees=90
        ),
    ]

ElongatedTriangularTiling(side_length=300).draw(columns=11, rows=6)
