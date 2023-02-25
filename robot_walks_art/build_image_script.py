from drawer import *
import random

def black_and_white(i):
  if i % 2 == 0:
    return (2*i+1, "black")
  else:
    return (2*i+1, "white")

def redder(i):
  return ((2*i+1)/50, (255-i, int((255-i)/2), 0))

def random_color(i):
  color = tuple([random.randint(0,255) for _ in range(3)])
  return (2*i+1, color)

def random_alternation(i):
  light_color = tuple([random.randint(150,200) for _ in range(3)])
  dark_color = tuple([random.randint(50,100) for _ in range(3)])
  if i % 2 == 0:
    return (2*i+1, dark_color)
  else:
    return (2*i+1, light_color)

def linear_interpolation(i, total, color1, color2):
  t = i/(total - 1)
  (r1,g1,b1) = color1
  (r2,g2,b2) = color2
  red = int((1 - t)*r1 + t*r2)
  green = int((1 - t)*g1 + t*g2)
  blue = int((1 - t)*b1 + t*b2)
  return ((2*i+1), (red,green,blue))

CircleSpiralDrawer(7, 10, random_alternation, 0b100111101110000111011110, resolution=400).draw_image(filename="robot_walk_7_10_10412510_random_alternation")
