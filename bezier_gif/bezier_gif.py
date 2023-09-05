import sys
sys.path.append("/Users/peter/Programming/MathArt/bezier_chain/")
from bezier_chain import BezierChain
from PIL import Image, ImageDraw
import random
import math

def random_point(min_x, max_x, min_y, max_y):
  x = random.randint(min_x, max_x)
  y = random.randint(min_y, max_y)
  return (x,y)

def random_points(number_of_points):
  return [random_point(0.1*4000, 0.9*4000, 0.1*4000, 0.9*4000) for _ in range(number_of_points)]

def circle_points(number_of_points, r=1500, offset=None):
  n = number_of_points
  def root_of_unity_multiple(i):
    return (2000 + r*math.cos(2*3.1415926*(i%n)/n), 2000 + r*math.sin(2*3.1415926*(i%n)/n))
  if offset is None:
    offset = random.randint(0,n-1)
  return [root_of_unity_multiple(i + offset) for i in range(n)]

def star_points(number_of_points, r, k=2, offset=0):
  if number_of_points % 2 == 0:
    raise ValueError(number_of_points)
  if k % number_of_points == 0:
    raise ValueError(k)
  circle = circle_points(number_of_points, r, offset)
  return [circle[(k*i) % number_of_points] for i in range(number_of_points)]

random.seed(1)

m = 7

anchor_points_list = [
  star_points(m,    0, k=2, offset=0),
  star_points(m,  200, k=2, offset=1),
  star_points(m,  400, k=2, offset=2),
  star_points(m,  600, k=2, offset=3),
  star_points(m,  800, k=2, offset=4),
  star_points(m, 1000, k=2, offset=5),
  star_points(m, 1200, k=2, offset=6),
  star_points(m, 1200, k=2, offset=0),
  star_points(m, 1000, k=2, offset=1),
  star_points(m,  800, k=2, offset=2),
  star_points(m,  600, k=2, offset=3),
  star_points(m,  400, k=2, offset=4),
  star_points(m,  200, k=2, offset=5),
  star_points(m,    0, k=2, offset=6),
  star_points(m,    0, k=3, offset=0),
  star_points(m,  200, k=3, offset=1),
  star_points(m,  400, k=3, offset=2),
  star_points(m,  600, k=3, offset=3),
  star_points(m,  800, k=3, offset=4),
  star_points(m, 1000, k=3, offset=5),
  star_points(m, 1200, k=3, offset=6),
  star_points(m, 1200, k=3, offset=0),
  star_points(m, 1000, k=3, offset=1),
  star_points(m,  800, k=3, offset=2),
  star_points(m,  600, k=3, offset=3),
  star_points(m,  400, k=3, offset=4),
  star_points(m,  200, k=3, offset=5),
  star_points(m,    0, k=3, offset=6),
]

# colors_list = [[random.randint(85, 170) for _ in range(3)] for _ in anchor_points_list]

colors_list = [
  (0xEB,0xEB,0xEB),
  (0xCA,0xD2,0xC5),
  (0x84,0xA9,0x8C),
  (0x59,0xC3,0xC3),
  (0x52,0x48,0x9C),
  (0xF4,0xC4,0x52),
  (0xFF,0x8C,0x42),
]
colors_list += colors_list[::-1]
colors_list += colors_list

anchor_points_list += anchor_points_list
colors_list        += colors_list



img = Image.new("RGBA", (4000,4000), (0,0,0,255))  # create new Image
draw = ImageDraw.Draw(img)  # create drawing context
one_curve_per_frame = False

number_of_scenes = len(anchor_points_list)
bezier_chains = [BezierChain([anchor_points[i] for anchor_points in anchor_points_list]) for i in range(m)]

color_chain = BezierChain(colors_list)
frames_per_cycle = 24
number_of_frames = frames_per_cycle*number_of_scenes
for i in range(number_of_frames):
  t = i/frames_per_cycle # from [0,number_of_scenes)
  anchor_points_at_time_t = [chain.position(t) for chain in bezier_chains]
  cycle_bezier_curve = BezierChain(anchor_points_at_time_t)
  color = tuple([int(h) for h in color_chain.position(t)])
  if one_curve_per_frame:
    img = Image.new("RGBA", (4000,4000), (0,0,0,255))  # create new Image
    draw = ImageDraw.Draw(img)  # create drawing context
  for j in range(m*500):
    s = j/500
    (x,y) = cycle_bezier_curve.position(s)
    draw.ellipse((x-20, y-20, x+20, y+20), fill=color)
  if i >= number_of_frames/2:
    img.resize((2160,2160)).save("/Users/peter/Programming/MathArt/bezier_gif/tmp/videos_6/frame_" + str(i).rjust(4,"0") + ".png")
  print("Frame " + str(i).rjust(4, " ") + "/" + str(number_of_frames), end="\r")
