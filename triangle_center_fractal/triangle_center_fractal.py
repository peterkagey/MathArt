from PIL import Image, ImageDraw
import random

# The fast version of this code is hanging out in a Mathematica worksheet.

WIDTH = 2000
HEIGHT = 2000
VERTICES = [(0,0), (0,HEIGHT-1),(WIDTH-1,HEIGHT-1),(WIDTH,0)]
img = Image.new("RGB", (WIDTH,HEIGHT), (0,0,0))  # create new Image
draw = ImageDraw.Draw(img)  # create drawing context

def draw_at(pt, radius = None, color=None):
  s = radius or 5
  layer = Image.new("RGBA", (2*s, 2*s), (0,0,0,0))  # create new Image
  ctx = ImageDraw.Draw(layer)
  (x,y) = pt
  (r,g,b) = color or (255, 255, 255)
  ctx.ellipse(((0,0), (2*s-1, 2*s-1)), fill=(r,g,b,128))
  return img.paste(layer, (int(x-s),int(y-s)), layer)

def centroid(pt, side):
  (x1,y1) = pt
  (p2,p3) = side
  (x2,y2) = p2
  (x3,y3) = p3
  x = (x1+x2+x3)/3
  y = (y1+y2+y3)/3
  return (x, y)

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
  denominator = sum(projective_barycenter)
  barycenter = list(map(lambda c: c/denominator, projective_barycenter))
  center = [0,0]
  for i in [0,1,2]:
    (x_i, y_i) = pts[i]
    s = barycenter[i]
    center[0] += x_i * s
    center[1] += y_i * s
  return center

def f(a,b,c):
  if a < 0.01:
    return 10**10
  else:
    return (b**2-c**2)**2

def center(pt, side):
  return barycentric(pt, side, f)
  # return centroid(pt, side)

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

(x,y) = (random.randrange(0,599), random.randrange(0,499))
last_side = random_side()
for _ in range(10):
  (x,y) = center((x,y), random_side())

streak = 0
for _ in range(1_000_000):
  next_side = random_side()
  (x,y) = center((x,y), next_side)
  if next_side == last_side:
    color = (255,255,255)
  elif right_side(next_side, last_side):
    color = (0,0,255)
  elif opposite_side(next_side,last_side):
    color = (255,0,0)
  else:
    color = (0,255,0)
  last_side = next_side
  draw_at((x,y), radius = 1, color=color)

img.save("/Users/pk/personal/art/triangle_center_fractal/tmp.png")
