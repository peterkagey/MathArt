import math
from grid import TriangularGrid
from polygon import Polygon

class TruncatedTrihexagonalTiling(TriangularGrid):
    NAME = "truncated_trihexagonal"
    TILES = [
        Polygon(
            n=12,
            color=(200,222,255),
            x_scale=1+2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=0,
            y_scale=4.09808, # math.sqrt(3)/2*(1 + math.sqrt(7 + 4*math.sqrt(3)))
            y_shift=0,
            rotate_degrees=15
        ),
        Polygon(
            n=4,
            color=(200,255,222),
            x_scale=1+2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=-(1+2*math.sqrt(7/4 + math.sqrt(3)))/2,
            y_scale=4.09808, # math.sqrt(3)/2*(1 + math.sqrt(7 + 4*math.sqrt(3)))
            y_shift=0,
            rotate_degrees=45
        ),
        Polygon(
            n=4,
            color=(222,200,255),
            x_scale=1+2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=(1+2*math.sqrt(7/4 + math.sqrt(3)))/4,
            y_scale=4.09808, # math.sqrt(3)/2*(1 + math.sqrt(7 + 4*math.sqrt(3)))
            y_shift=4.09808/2,
            rotate_degrees=-15
        ),
        Polygon(
            n=4,
            color=(222,255,200),
            x_scale=1+2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=-(1+2*math.sqrt(7/4 + math.sqrt(3)))/4,
            y_scale=4.09808, # math.sqrt(3)/2*(1 + math.sqrt(7 + 4*math.sqrt(3)))
            y_shift=4.09808/2,
            rotate_degrees=15
        ),
        Polygon(
            n=6,
            color=(255,200,222),
            x_scale=1+2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=-(1+2*math.sqrt(7/4 + math.sqrt(3)))/2,
            y_scale=4.09808, # math.sqrt(3)/2*(1 + math.sqrt(7 + 4*math.sqrt(3)))
            y_shift=4.09808/3,
            rotate_degrees=0
        ),
        Polygon(
            n=6,
            color=(255,222,200),
            x_scale=1+2*math.sqrt(7/4 + math.sqrt(3)), # scaling factor for 12-gon
            x_shift=-(1+2*math.sqrt(7/4 + math.sqrt(3)))/2,
            y_scale=4.09808, # math.sqrt(3)/2*(1 + math.sqrt(7 + 4*math.sqrt(3)))
            y_shift=-4.09808/3,
            rotate_degrees=0
        ),
    ]

TruncatedTrihexagonalTiling(side_length=300).draw(rows=3, columns=3)
