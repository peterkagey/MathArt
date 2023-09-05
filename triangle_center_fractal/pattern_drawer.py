from PIL import Image, ImageDraw
import random
import os

class PatternDrawer():
  def __init__(self, barycenter_function, size=8000):
    self.width = size
    self.height = size
    self.vertices = [(0,0), (0,self.height-1),(self.width-1,self.height-1),(self.width,0)]
    self.img = Image.new("RGB", (self.width, self.height), (0,0,0))
    self.draw = ImageDraw.Draw(self.img)
    self.center_function = barycenter_function

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
    filepath = current_directory + "/frames/tmp/x11/frame_" + image_name + ".png"
    self.img.resize((2160,2160)).save(filepath)
