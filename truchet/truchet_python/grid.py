import random
from truchet_tile import TruchetTile
from PIL import Image

class Grid():
    def __init__(self, side_length=100):
        self.side_length = side_length

    def draw_polygon(self, base, polygon, position, scale=100):
        (c_i, r_j) = position
        truchet = TruchetTile(polygon.n, side_length=scale, color=polygon.color, scale=1)
        truchet.draw_random_arcs("black")

        x_raw = self.x_position(c_i, r_j)
        x = int(scale*(polygon.x_scale*x_raw + polygon.x_shift))
        y = int(scale*(polygon.y_scale*r_j + polygon.y_shift))
        truchet.draw_at(base, (x, y), theta=polygon.rotate_degrees)

    def draw(self, columns=5, rows=5, canvas_width=3000, canvas_height=3000):
        random.seed(919)
        base = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))
        for c_i in range(columns):
            for r_j in range(rows):
                for tile in self.TILES:
                    self.draw_polygon(base,tile,(c_i, r_j),scale=self.side_length)

        base.save("/Users/peter/Programming/trihexagonal_truchet_python/images/" + self.NAME + ".png")

class SquareGrid(Grid):
    def x_position(self, c_i, _):
        return c_i

class TriangularGrid(Grid):
    def x_position(self, c_i, r_j):
        return c_i + (r_j % 2)/2
