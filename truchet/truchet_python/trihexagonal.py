import math
from grid import TriangularGrid
from polygon import Polygon

class TrihexagonalTiling(TriangularGrid):
    NAME = "trihexagonal"
    TILES = [
        Polygon(
            n=6,
            color=(255,255,200),
            x_scale=2,
            x_shift=0,
            y_scale=math.sqrt(3),
            y_shift=0,
            rotate_degrees=0
        ),
        Polygon(
            n=3,
            color=(255,200,255),
            x_scale=2,
            x_shift=-1,
            y_scale=math.sqrt(3),
            y_shift=math.sqrt(3)/3,
            rotate_degrees=-30
        ),
        Polygon(
            n=3,
            color=(200,255,255),
            x_scale=2,
            x_shift=0,
            y_scale=math.sqrt(3),
            y_shift=math.sqrt(3)*2/3,
            rotate_degrees=30
        )
    ]

TrihexagonalTiling(side_length=300).draw(columns=6, rows=7)
