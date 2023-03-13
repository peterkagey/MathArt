from bezier_connect_the_dots import ConnectTheDots

from PIL import Image, ImageDraw
import random
import math

WIDTH = 8000
HEIGHT = 8000
VERTICES = [(0,0), (0,HEIGHT-1),(WIDTH-1,HEIGHT-1),(WIDTH,0)]

def draw_at(pt, radius = None, color=None, opacity=0.5):
  s = radius or 5
  layer = Image.new("RGBA", (2*s, 2*s), (0,0,0,0))  # create new Image
  ctx = ImageDraw.Draw(layer)
  (x,y) = pt
  (r,g,b) = color or (255, 255, 255)
  ctx.ellipse(((0,0), (2*s-1, 2*s-1)), fill=(r,g,b,int(opacity*255)))
  try:
    return img.paste(layer, (int(x-s),int(y-s)), layer)
  except:
    print("Ahhhhhhhh!!!!!")
    print(x, y)
    raise ValueError(1)

def centroid(pt, side):
  (x1,y1) = pt
  (p2,p3) = side
  (x2,y2) = p2
  (x3,y3) = p3
  x = (x1+x2+x3)/3
  y = (y1+y2+y3)/3
  return (x, y)

def norm(p1, p2):
  (x1, y1) = p1
  (x2, y2) = p2
  return ((x1-x2)**2 + (y1-y2)**2)**0.5

def lengths(pts):
  [p1, p2, p3] = pts
  return (norm(p2, p3), norm(p1, p3), norm(p1, p2))

def barycentric(pt, side, f):
  (p2,p3) = side
  pts = [pt, p2, p3]
  (a, b, c) = lengths(pts)
  projective_barycenter = [f(a,b,c), f(b,c,a), f(c,a,b)]
  try:
    denominator = sum(projective_barycenter)
    barycenter = list(map(lambda c: c/denominator, projective_barycenter))
  except:
    print("~~~ denominator ~~~")
    print((a,b,c))
    print(projective_barycenter)
    raise ValueError(2)
  center = [0,0]
  for i in [0,1,2]:
    (x_i, y_i) = pts[i]
    s = barycenter[i]
    center[0] += x_i * s
    center[1] += y_i * s
  return center

def x244(_,b,c):
  return (b**2-c**2)**2

def x41(a, b, c):
  return a**2*(b + c - a)

def x58(a,b,c):
  return a/(b + c)

def parameterized_circle(params):
  [p1, p2, p3, p4, p5, p6] = params
  def f(a,b,c):
    x = a.real + 10**-8*random.random()
    y = b.real + 10**-8*(1+random.random())
    z = c.real + 10**-8*(1+random.random())
    try:
      # a^x_1
      # (b+c-a)^x_2
      # (bc)^x_3
      # (b^x_4 - c^x_4)^2
      # (b^x_5 + c^x_5)^x_6
      # (b^x_5 + c^x_5)^x_6
      parts = [
        x**p1               + 10**-10,
        (y+z-x)**p2         + 10**-10,
        (y*z)**p3           + 10**-10,
        (y**p4 - z**p4)**2   + 10**-10,
        (y**p5 + z**p5)**p6 + 10**-10,
      ]
      return math.prod(parts)
    except:
      print(x,y,z)
      raise ValueError(4)
  return f

def random_side():
  [v1,v2,v3,v4] = VERTICES
  return random.choice([(v1,v2), (v2,v3), (v3,v4), (v4,v1)])

def opposite_side(s1,s2):
  (v1,_) = s1
  (v2,_) = s2
  if v1 == VERTICES[0]:
    return v2 == VERTICES[2]
  if v1 == VERTICES[1]:
    return v2 == VERTICES[3]
  if v1 == VERTICES[2]:
    return v2 == VERTICES[0]
  if v1 == VERTICES[3]:
    return v2 == VERTICES[1]

def right_side(s1,s2):
  vs = []
  (v1,_) = s1
  (v2,_) = s2
  if v1 == VERTICES[0]:
    return v2 == VERTICES[1]
  if v1 == VERTICES[1]:
    return v2 == VERTICES[2]
  if v1 == VERTICES[2]:
    return v2 == VERTICES[3]
  if v1 == VERTICES[3]:
    return v2 == VERTICES[0]

# --------------------------------------------------
# a^x_1
# (b + c - a)^x_2
# (bc)^x_3
# (b^x_4 - c^x_4)^2
# (b^x_5 + c^x_5)^x_6
# (b^x_5 + c^x_5)^x_6
param_points = [
    ( 0,   0, 0, 0,  0,  0), # X(1)   => 1
    (-1,   0, 0, 0,  0,  0), # X(2)   => a^-1
    ( 0,  -1, 1, 0,  0,  0), # X(7)   => bc * (b+c-a)^-1
    ( 0,   0, 1, 0,  1,  1), # X(10)  => bc * (b+c)
    ( 0,   0, 0, 0,  1,  1), # X(37)  => b+c
    ( 0,   0, 0, 0,  2,  1), # X(38)  => b^2 + c^2
    ( 1,   0, 0, 0,  2,  1), # X(39)  => a * (b^2+c^2)
    ( 2,   1, 0, 0,  0,  0), # X(41)  => a^2 * (b+c-a)
    ( 1,   0, 0, 0,  1,  1), # X(42)  => a * (b+c)
    ( 1,   1, 0, 0,  0,  0), # X(55)  => a * (b+c-a)
    ( 1,  -1, 0, 0,  0,  0), # X(56)  => a * (b+c-a)^-1
    ( 0,  -1, 0, 0,  0,  0), # X(57)  => (b+c-a)^-1
    ( 1,   0, 0, 0,  1, -1), # X(58)  => a * (b+c)^-1
    (-3,   0, 0, 0,  0,  0), # X(76)  => a^-3
    ( 0,   0, 0, 0,  1, -1), # X(81)  => (b+c)^-1
    ( 0,   0, 0, 0,  2, -1), # X(82)  => (b^2 + c^2)^-1
    ( 0,  -1, 2, 0,  0,  0), # X(83)  => (bc)^2 * (b+c-a)^-1
    ( 0,   0, 1, 0,  1, -1), # X(86)  => (bc) * (b+c)^-1
    # (This one seems to dominate everything)
    # ( 0,   0, 1, 2,  0,  0), # X(115) => bc*(b^2 - c^2)^2
    ( 0,   0, 1, 0,  2,  1), # X(141) => bc*(b^2 + c^2)
]
# X(45) => 2(b + c) - a
random.seed(919)
random.shuffle(param_points)

color_points1 = []
for _ in param_points:
  c1 = random.randint(222, 255)
  c2 = random.randint(200, 222)
  c3 = random.randint(100,200)
  colors = [c1, c2, c3]
  random.shuffle(colors)
  color_points1.append(tuple(colors))

color_points2 = []
for _ in param_points:
  c1 = random.randint(222, 255)
  c2 = random.randint(200, 222)
  c3 = random.randint(100,200)
  colors = [c1, c2, c3]
  random.shuffle(colors)
  color_points2.append(tuple(colors))

color_points3 = []
for _ in param_points:
  c1 = random.randint(222, 255)
  c2 = random.randint(200, 222)
  c3 = random.randint(100,200)
  colors = [c1, c2, c3]
  random.shuffle(colors)
  color_points3.append(tuple(colors))

color_points4 = []
for _ in param_points:
  c1 = random.randint(222, 255)
  c2 = random.randint(200, 222)
  c3 = random.randint(100,200)
  colors = [c1, c2, c3]
  random.shuffle(colors)
  color_points4.append(tuple(colors))


steps_count = len(param_points)*24*3

connect_the_dots3 = ConnectTheDots(dimension=3)
color_walk1 = connect_the_dots3.all_points(steps_count, color_points1, transform=int)
color_walk2 = connect_the_dots3.all_points(steps_count, color_points2, transform=int)
color_walk3 = connect_the_dots3.all_points(steps_count, color_points3, transform=int)
color_walk4 = connect_the_dots3.all_points(steps_count, color_points4, transform=int)

connect_the_dots6 = ConnectTheDots(dimension=6)
parameter_walk = connect_the_dots6.all_points(steps_count, param_points)

counter = 0
for i in range(steps_count):
  # The fast version of this code is hanging out in a Mathematica worksheet.
  img = Image.new("RGB", (WIDTH,HEIGHT), (0,0,0))  # create new Image
  draw = ImageDraw.Draw(img)  # create drawing context

  x999 = parameterized_circle(parameter_walk[i])
  random.seed(919)
  (x,y) = (random.randrange(0,599), random.randrange(0,499))
  last_side = random_side()
  for _ in range(10):
    (x,y) = barycentric((x,y), random_side(), x999)

  streak = 0
  for _ in range(100_000):
    next_side = random_side()
    (x,y) = barycentric((x,y), next_side, x999)
    if next_side == last_side:
      color = color_walk1[i]
    elif right_side(next_side, last_side):
      color = color_walk2[i]
    elif opposite_side(next_side,last_side):
      color = color_walk3[i]
    else:
      color = color_walk4[i]
    last_side = next_side
    draw_at((x,y), radius = 10, color=color, opacity=0.25)

  filepath = "/Users/peter/Programming/MathArt/triangle_center_fractal/GIF_frames/gif_frame_" + str(counter).rjust(4,"0") + ".png"
  img.resize((2160,2160)).save(filepath)
  print("Experiment " + str(counter).rjust(4), end="\r")
  counter += 1
