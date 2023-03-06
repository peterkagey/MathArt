import math
from grid import TriangularGrid
from polygon import Polygon

class SnubTrihexagonalTiling(TriangularGrid):
    NAME = "snub_trihexagonal"
    # theta_radians = 19.1066/360*2*3.1415926
    # r_x = math.cos(theta_radians)
    # r_y = -math.sin(theta_radians)
    # g_x = math.cos(theta_radians + 3.1415926/3)
    # g_y = -math.sin(theta_radians + 3.1415926/3)
    TILES = [
        Polygon(
            n=6,
            color=(200,255,255),
            x_scale=math.sqrt(7),
            x_shift=0,
            y_scale=math.sqrt(21)/2,
            y_shift=0,
            rotate_degrees=19.1066
        ),
        Polygon( # ((-2*r + g) + (-2*r + 2*g) + (-r + g))/3
            n=3,
            color=(255,200,255),
            x_scale=math.sqrt(7),
            x_shift=-math.sqrt(7)/2,
            y_scale=math.sqrt(21)/2,
            y_shift=-math.sqrt(7/12),
            rotate_degrees=19.1066-30
        ),
        Polygon( # (g + (r+g) + (2*g))/3
            n=3,
            color=(255,255,200),
            x_scale=math.sqrt(7),
            x_shift=3/14*math.sqrt(7),
            y_scale=math.sqrt(21)/2,
            y_shift=-13/2/math.sqrt(21),
            rotate_degrees=19.1066-30
        ),
        Polygon( # (g + (-r+g) + (-r+2*g))/3
            n=3,
            color=(200,222,255),
            x_scale=math.sqrt(7),
            x_shift=-1/math.sqrt(7),
            y_scale=math.sqrt(21)/2,
            y_shift=-5/math.sqrt(21),
            rotate_degrees=19.1066-30
        ),
        Polygon( # (2*g + (-r+2*g) + (-r+3*g))/3
            n=3,
            color=(200,255,222),
            x_scale=math.sqrt(7),
            x_shift=-math.sqrt(7)/14,
            y_scale=math.sqrt(21)/2,
            y_shift=-19/2/math.sqrt(21),
            rotate_degrees=19.1066-30
        ),
        Polygon( # (g + (r) + (r+g))/3
            n=3,
            color=(222,200,255),
            x_scale=math.sqrt(7),
            x_shift=2/math.sqrt(7),
            y_scale=math.sqrt(21)/2,
            y_shift=-4/math.sqrt(21),
            rotate_degrees=19.1066+30
        ),
        Polygon( # (2*g + (g) + (-r+2*g))/3
            n=3,
            color=(222,255,200),
            x_scale=math.sqrt(7),
            x_shift=0,
            y_scale=math.sqrt(21)/2,
            y_shift=-math.sqrt(7/3),
            rotate_degrees=19.1066+30
        ),
        Polygon( # (-r + (-2*r+g) + (-r+g))/3
            n=3,
            color=(255,200,222),
            x_scale=math.sqrt(7),
            x_shift=-3/math.sqrt(7),
            y_scale=math.sqrt(7)*math.sqrt(3)/2,
            y_shift=-1/math.sqrt(21),
            rotate_degrees=19.1066+30
        ),
        Polygon( # (-g + (r-g) + (r-2*g))/3
            n=3,
            color=(255,222,200),
            x_scale=math.sqrt(7),
            x_shift=1/math.sqrt(7),
            y_scale=math.sqrt(21)/2,
            y_shift=5/math.sqrt(21),
            rotate_degrees=19.1066+30
        ),

    ]

SnubTrihexagonalTiling(side_length=300).draw(columns=5, rows=6)
