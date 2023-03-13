# The idea here it to make a list of points in n-dimensional space, and then
# create a cubic bezier curve that will connect the dots in a sensible way.
from PIL import Image, ImageDraw
import math

class ConnectTheDots():
    def __init__(self, dimension):
        self.scale = 5
        self.dimension = dimension
        self.r = 3 * self.scale
        self.x_max = 1000 * self.scale
        self.y_max = 1000 * self.scale
        self.img = Image.new("RGBA", (self.x_max, self.y_max), (255,255,255,0))
        self.draw = ImageDraw.Draw(self.img)

    def curve_points(self, fs):
        points = []
        for i in range(1001):
            t = i / 1000
            new_point = [f(t) for f in fs]
            points.append(new_point)
        return points

    # t better be between 0 and 1
    def curve_point(self, fs, t):
        return [f(t) for f in fs]

    def curve_from_points(self, points, transform = lambda x: x):
        if len(points) != 4:
            raise ValueError("The wrong number of points for `curve_from_points`")
        dimension = len(points[0])
        fs = []
        for i in range(dimension):
            def f(t, i=i): # https://stackoverflow.com/a/3431699
                s = 0
                for k in range(4):
                    s += self.binomial(3,k) * (1-t)**(3-k) * t**k * points[k][i]
                return transform(s)
            fs.append(f)
        return fs

    def binomial(self, n, k):
        return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))

    def draw_bezier_curve(self, points, color="red"):
        (f, g) = self.curve_from_points(points)
        for (x, y) in self.curve_points([f, g]):
            self.draw.ellipse((x-self.r, y-self.r, x+self.r, y+self.r), fill=color)

    def tangent_direction(self, p_before, p_next):
        return [(p_next[i] - p_before[i])/2 for i in range(self.dimension)]

    def before_and_after_steps(self, p_before, p_current, p_next):
        tangents = self.tangent_direction(p_before, p_next)
        before_step = [p_current[i] - tangents[i] for i in range(self.dimension)]
        after_step  = [p_current[i] + tangents[i] for i in range(self.dimension)]
        return [before_step, p_current, p_current, after_step]

    def make_chain(self, points):
        if len(points) < 2:
            raise ValueError("We can't `make_chain` with fewer than two anchor points!")
        point_count = len(points)
        steps = []
        for i in range(point_count):
            before_point = points[(i-1) % point_count]
            current_point = points[i]
            next_point = points[(i+1) % point_count]
            steps += self.before_and_after_steps(before_point, current_point, next_point)
        steps.append(steps[0])
        steps.append(steps[1])
        return steps[2:len(steps)]

    def all_points(self, number_of_plotted_points, anchor_points, transform = lambda x: x):
        chain = self.make_chain(anchor_points)
        step_size = len(anchor_points)/number_of_plotted_points
        pts = []
        for i in range(number_of_plotted_points):
            t = i*step_size
            current_bezier_points = chain[4*int(t):4*int(t)+4]
            fs = self.curve_from_points(current_bezier_points, transform)
            pt = self.curve_point(fs, t % 1)
            pts.append(pt)
        return pts
