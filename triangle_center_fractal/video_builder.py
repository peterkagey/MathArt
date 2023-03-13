from bezier_connect_the_dots import ConnectTheDots
from pattern_drawer import PatternDrawer
import random
import math

class VideoBuilder():
  def __init__(self, parameter_points, frames_per_point):
    self.parameter_anchor_points = parameter_points
    self.frame_count = frames_per_point * len(parameter_points)
    self.parameter_step_points = self.get_parameter_step_points()

  def get_color_path(self):
    return ConnectTheDots(dimension=3) \
      .all_points(self.frame_count, self.get_color_anchor_points(), transform=int)

  def get_color_anchor_points(self):
    color_points = []
    for _ in self.parameter_anchor_points: # one for each anchor point
      c1 = random.randint(222, 255)
      c2 = random.randint(200, 222)
      c3 = random.randint(100,200)
      colors = [c1, c2, c3]
      random.shuffle(colors)
      color_points.append(tuple(colors))
    return color_points

  def get_parameter_step_points(self):
    return ConnectTheDots(dimension=5) \
      .all_points(self.frame_count, self.parameter_anchor_points)

  def triangle_center(self, parameters):
    [p1, p2, p3, p4, p5] = parameters
    def f(a,b,c):
      x = a.real + 10**-8*random.random()
      y = b.real + 10**-8*(1+random.random())
      z = c.real + 10**-8*(1+random.random())
      # a^x_1
      # (b+c-a)^x_2
      # (bc)^x_3
      # (b^x_4 + c^x_4)^x_5
      parts = [
        x**p1               + 10**-10,
        (y+z-x)**p2         + 10**-10,
        (y*z)**p3           + 10**-10,
        (y**p4 + z**p4)**p5 + 10**-10,
      ]
      return math.prod(parts)
    return f

  def make_frames(self, number_of_points=10_000, radius=10, opacity=0.25):
    color_paths = [self.get_color_path() for _ in range(4)]
    def current_color(i):
      return [color_paths[j][i] for j in range(4)]
    for i in range(self.frame_count):
      trilinear_function = self.triangle_center(self.parameter_step_points[i])
      PatternDrawer(trilinear_function) \
        .draw_image(
          current_color(i),
          number_of_points=number_of_points,
          radius=radius,
          opacity=opacity,
          image_name=str(i)
        )

# --------------------------------------------------
# a^x_1
# (b + c - a)^x_2
# (bc)^x_3
# (b^x_4 + c^x_4)^x_5
# (b^x_4 + c^x_4)^x_5
param_points = [
    ( 0,  0, 0, 0,  0), # X(1)   => 1
    (-1,  0, 0, 0,  0), # X(2)   => a^-1
    ( 0, -1, 1, 0,  0), # X(7)   => bc * (b+c-a)^-1
    ( 0,  0, 1, 1,  1), # X(10)  => bc * (b+c)
    ( 0,  0, 0, 1,  1), # X(37)  => b+c
    ( 0,  0, 0, 2,  1), # X(38)  => b^2 + c^2
    ( 1,  0, 0, 2,  1), # X(39)  => a * (b^2+c^2)
    ( 2,  1, 0, 0,  0), # X(41)  => a^2 * (b+c-a)
    ( 1,  0, 0, 1,  1), # X(42)  => a * (b+c)
    ( 1,  1, 0, 0,  0), # X(55)  => a * (b+c-a)
    ( 1, -1, 0, 0,  0), # X(56)  => a * (b+c-a)^-1
    ( 0, -1, 0, 0,  0), # X(57)  => (b+c-a)^-1
    ( 1,  0, 0, 1, -1), # X(58)  => a * (b+c)^-1
    (-3,  0, 0, 0,  0), # X(76)  => a^-3
    ( 0,  0, 0, 1, -1), # X(81)  => (b+c)^-1
    ( 0,  0, 0, 2, -1), # X(82)  => (b^2 + c^2)^-1
    ( 0, -1, 2, 0,  0), # X(83)  => (bc)^2 * (b+c-a)^-1
    ( 0,  0, 1, 1, -1), # X(86)  => (bc) * (b+c)^-1
    ( 0,  0, 1, 2,  1), # X(141) => bc*(b^2 + c^2)
]
random.seed(726)
random.shuffle(param_points)

VideoBuilder(param_points, frames_per_point=1).make_frames(number_of_points=1_000_000, radius=5)
