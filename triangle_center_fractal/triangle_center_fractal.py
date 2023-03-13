from bezier_connect_the_dots import ConnectTheDots

from PIL import Image, ImageDraw
import random
import math
import os

class TriangleCenterPatternDrawer():
  def __init__(self, trilinear_function, size=8000):
    self.width = size
    self.height = size
    self.vertices = [(0,0), (0,self.height-1),(self.width-1,self.height-1),(self.width,0)]
    self.img = Image.new("RGB", (self.width, self.height), (0,0,0))
    self.draw = ImageDraw.Draw(self.img)
    self.center_function = trilinear_function

  def draw_at(self, pt, radius = None, color=None, opacity=0.5):
    s = radius or 5
    layer = Image.new("RGBA", (2*s, 2*s), (0,0,0,0))
    ctx = ImageDraw.Draw(layer)
    (x,y) = pt
    (r,g,b) = color or (255, 255, 255)
    ctx.ellipse(((0,0), (2*s-1, 2*s-1)), fill=(r,g,b,int(opacity*255)))
    return self.img.paste(layer, (int(x-s),int(y-s)), layer)

  def norm(self, p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

  def lengths(self, pts):
    [p1, p2, p3] = pts
    return (self.norm(p2, p3), self.norm(p1, p3), self.norm(p1, p2))

  def barycentric(self, pt, side, f):
    (p2,p3) = side
    pts = [pt, p2, p3]
    (a, b, c) = self.lengths(pts)
    projective_barycenter = [f(a,b,c), f(b,c,a), f(c,a,b)]
    denominator = sum(projective_barycenter)
    barycenter = list(map(lambda c: c/denominator, projective_barycenter))
    center = [0,0]
    for i in [0,1,2]:
      (x_i, y_i) = pts[i]
      s = barycenter[i]
      center[0] += x_i * s
      center[1] += y_i * s
    return center

  def random_side(self):
    [v1,v2,v3,v4] = self.vertices
    return random.choice([(v1,v2), (v2,v3), (v3,v4), (v4,v1)])

  def opposite_side(self, s1, s2):
    (v1,_) = s1
    (v2,_) = s2
    if v1 == self.vertices[0]:
      return v2 == self.vertices[2]
    if v1 == self.vertices[1]:
      return v2 == self.vertices[3]
    if v1 == self.vertices[2]:
      return v2 == self.vertices[0]
    if v1 == self.vertices[3]:
      return v2 == self.vertices[1]

  def right_side(self, s1, s2):
    (v1,_) = s1
    (v2,_) = s2
    if v1 == self.vertices[0]:
      return v2 == self.vertices[1]
    if v1 == self.vertices[1]:
      return v2 == self.vertices[2]
    if v1 == self.vertices[2]:
      return v2 == self.vertices[3]
    if v1 == self.vertices[3]:
      return v2 == self.vertices[0]

  def draw_image(self, colors, number_of_points=100_000, image_name="tmp", radius=10, opacity=0.25):
    random.seed(919)
    [color1, color2, color3, color4] = colors
    x = random.randrange(0,self.width-1)
    y = random.randrange(0,self.height-1)
    last_side = self.random_side()
    # Iterate through ten points to reduce number of stray points.
    for _ in range(10):
      (x,y) = self.barycentric((x,y), self.random_side(), self.center_function)

    for _ in range(number_of_points):
      next_side = self.random_side()
      (x,y) = self.barycentric((x,y), next_side, self.center_function)
      if next_side == last_side:
        color = color1
      elif self.right_side(next_side, last_side):
        color = color2
      elif self.opposite_side(next_side, last_side):
        color = color3
      else:
        color = color4
      last_side = next_side
      self.draw_at((x,y), radius, color=color, opacity=opacity)
    current_directory = os.path.dirname(os.path.realpath(__file__))
    filepath = current_directory + "/frames/tmp/frame_" + image_name + ".png"
    self.img.resize((2160,2160)).save(filepath)

class TriangleCenterFrameMaker():
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
      TriangleCenterPatternDrawer(trilinear_function) \
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
random.seed(919)
random.shuffle(param_points)

TriangleCenterFrameMaker(param_points, frames_per_point=1).make_frames(number_of_points=1_000_000, radius=5)
