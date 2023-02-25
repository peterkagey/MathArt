from argparse import ArgumentError
from PIL import Image, ImageDraw
import random
import math

class BirdzierCurves():
    def __init__(self):
        self.scale = 5
        self.r = 3 * self.scale
        self.x_max = 1000 * self.scale
        self.y_max = 1000 * self.scale
        self.x_range = [self.x_max,0]
        self.y_range = [self.y_max,0]
        self.img = Image.new("RGBA", (self.x_max, self.y_max), (255,255,255,0))
        self.draw = ImageDraw.Draw(self.img)
        self.colors = self.random_color_spectrum(cycle=True)
        self.matrix = self.four_by_four()
        self.make_curves()

    def curve_points(self, fx, fy):
        points = []
        for i in range(1001):
            t = i / 1000
            points += [(int(fx(t)), int(fy(t)))]
            self.x_range[0] = min(self.x_range[0], fx(t))
            self.x_range[1] = max(self.x_range[1], fx(t))
            self.y_range[0] = min(self.y_range[0], fy(t))
            self.y_range[1] = max(self.y_range[1], fy(t))
        return points

    def curve_from_points(self, points):
        if len(points) != 4:
            raise ArgumentError
        dimension = len(points[0])
        fs = []
        for i in range(dimension):
            def f(t, i=i): # https://stackoverflow.com/a/3431699
                s = 0
                for k in range(4):
                    s += self.binomial(3,k) * (1-t)**(3-k) * t**k * points[k][i]
                return s
            fs.append(f)
        return fs

    def make_curves(self):
        curve_list = []
        for i in range(4):
            curve_list.append(self.curve_from_points([self.matrix[0][i], self.matrix[1][i], self.matrix[2][i], self.matrix[3][i]]))
        self.curves = curve_list

    def binomial(self, n, k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

    def four_by_four(self):
        self.all_points = []
        for _ in range(4):
            self.all_points.append([])
            for _ in range(4):
                self.all_points[-1].append(self.random_point())
        return self.all_points

    def draw_bezier_curve(self, points, color="red"):
        (f, g) = self.curve_from_points(points)
        for (x, y) in self.curve_points(f, g):
            self.draw.ellipse((x-self.r, y-self.r, x+self.r, y+self.r), fill=color)

    def random_point(self):
        return (random.randrange(0,self.x_max), random.randrange(0,self.y_max))

    def random_color(self):
        red = random.randrange(0,255)
        return (red, random.randrange(0,255), random.randrange(0,255))

    def random_color_spectrum(self, cycle=False):
        color_points = []
        for _ in range(4):
            color_points.append(self.random_color())
        if cycle:
            color_points[3] = color_points[0]
        return self.curve_from_points(color_points)

    def color_step(self, t):
        red = int(self.colors[0](t))
        green = int(self.colors[1](t))
        blue = int(self.colors[2](t))
        return (red, green, blue)

    def draw_the_thing(self, t):
        def apply(fs, t):
            return fs[0](t),fs[1](t)
        list_of_points = [apply(self.curves[0], t), apply(self.curves[1], t), apply(self.curves[2], t), apply(self.curves[3], t)]
        self.draw_bezier_curve(list_of_points, color=self.color_step(t))

    def save_as(self, name="example"):
        self.img.resize((900,900)).save("/Users/peter/Programming/birdzier/" + name + ".png")

for image_number in range(10):
    bezier_curve_drawer = BirdzierCurves()
    n = 500
    for i in range(n+1):
        bezier_curve_drawer.draw_the_thing(i/n)
    bezier_curve_drawer.save_as("birds9/bird" + str(image_number))
    print("Finished #" + str(image_number))
