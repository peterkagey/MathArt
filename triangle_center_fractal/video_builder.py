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

  def make_frames(self, number_of_points=10_000, radius=10, opacity=0.25, print_progress=False):
    color_paths = [self.get_color_path() for _ in range(4)]
    def current_color(i):
      return [color_paths[j][i] for j in range(4)]
    padding = len(str(self.frame_count))
    for i in range(self.frame_count):
      barycenter_function = self.triangle_center(self.parameter_step_points[i])
      PatternDrawer(barycenter_function) \
        .draw_image(
          current_color(i),
          number_of_points=number_of_points,
          radius=radius,
          opacity=opacity,
          image_name=str(i).rjust(padding, "0")
        )
      if print_progress:
        print("Frame " + str(i).rjust(4, "0") + "/" + str(self.frame_count), end="\r")
