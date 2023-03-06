import math
from grid import TriangularGrid
from polygon import Polygon

class TruncatedHexagonalTiling(TriangularGrid):
    NAME = "truncated_hexagonal"
    TILES = [
        Polygon(
            n=12,
            color=(200,255,255),
            x_scale=1.866*2, # FIXME, motivate the magic number.
            x_shift=0,
            y_scale=1.866*math.sqrt(3),
            y_shift=0,
            rotate_degrees=15
        ),
        Polygon(
            n=3,
            color=(255,200,255),
            x_scale=2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=-math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            y_scale=math.sqrt(3)*math.sqrt(7/4 + math.sqrt(3)),
            y_shift=math.sqrt(3)/3*math.sqrt(7/4 + math.sqrt(3)),
            rotate_degrees=-30
        ),
        Polygon(
            n=3,
            color=(255,255,200),
            x_scale=2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=0,
            y_scale=math.sqrt(3)*math.sqrt(7/4 + math.sqrt(3)),
            y_shift=2*math.sqrt(3)/3*math.sqrt(7/4 + math.sqrt(3)),
            rotate_degrees=30
        ),
    ]

TruncatedHexagonalTiling(side_length=300).draw(rows=4, columns=4)
