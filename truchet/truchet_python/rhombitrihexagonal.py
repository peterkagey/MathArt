import math
from grid import TriangularGrid
from polygon import Polygon

class RhombitrihexagonalTiling(TriangularGrid):
    NAME = "rhombitrihexagonal"
    TILES = [
        Polygon(
            n=6,
            color=(200,222,255),
            x_scale=math.sqrt(3)+1,
            x_shift=0,
            y_scale=(3 + math.sqrt(3))/2,
            y_shift=0,
            rotate_degrees=30
        ),
        Polygon(
            n=4,
            color=(200,255,222),
            x_scale=math.sqrt(3)+1,
            x_shift=-(math.sqrt(3)+1)/2,
            y_scale=(3 + math.sqrt(3))/2,
            y_shift=0,
            rotate_degrees=45
        ),
        Polygon(
            n=4,
            color=(222,200,255),
            x_scale=math.sqrt(3)+1,
            x_shift=(math.sqrt(3)+1)/4,
            y_scale=(3 + math.sqrt(3))/2,
            y_shift=(3 + math.sqrt(3))/4,
            rotate_degrees=-15
        ),
        Polygon(
            n=4,
            color=(222,255,200),
            x_scale=math.sqrt(3)+1,
            x_shift=-(math.sqrt(3)+1)*1/4,
            y_scale=(3 + math.sqrt(3))/2,
            y_shift=(3 + math.sqrt(3))/4,
            rotate_degrees=15
        ),
        Polygon(
            n=3,
            color=(255,200,222),
            x_scale=math.sqrt(3)+1,
            x_shift=-(math.sqrt(3)+1)/2,
            y_scale=(3 + math.sqrt(3))/2,
            y_shift=(3 + math.sqrt(3))/6,
            rotate_degrees=30
        ),
        Polygon(
            n=3,
            color=(255,222,200),
            x_scale=math.sqrt(3)+1,
            x_shift=0,
            y_scale=(3 + math.sqrt(3))/2,
            y_shift=(3 + math.sqrt(3))/3,
            rotate_degrees=-30
        )
    ]

RhombitrihexagonalTiling(side_length=300).draw(columns=5, rows=5)
