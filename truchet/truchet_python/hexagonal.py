import math
from grid import TriangularGrid
from polygon import Polygon

class HexagonalTiling(TriangularGrid):
    NAME = "hexagonal"
    TILES = [
        Polygon(
            n=6,
            color=(200,222,255),
            x_scale=math.sqrt(3),
            x_shift=0,
            y_scale=3/2,
            y_shift=0,
            rotate_degrees=30
        )
    ]

HexagonalTiling(side_length=300).draw(columns=7, rows=8)
