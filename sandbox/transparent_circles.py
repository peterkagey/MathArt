from PIL import Image, ImageDraw
import random

img = Image.new("RGBA", (600,500), (0,0,0,255))  # create new Image
draw = ImageDraw.Draw(img)  # create drawing context

def draw_at(pt, radius = None, color=None):
  layer = Image.new("RGBA", (600,500), (255,255,255,0))  # create new Image
  ctx = ImageDraw.Draw(layer)
  (x,y) = pt
  s = radius or 5
  (r,g,b) = color or (255, 255, 255)
  ctx.ellipse(((x-s,y-s), (x+s, y+s)), fill=(r,g,b,128))
  return Image.alpha_composite(img, layer)

(x, y) = (72, 250)
wt = 0.5
color = (255, 255, 255)
last = (False, False)
for _ in range(5000):
  img = draw_at((x,y), radius=2, color=color)
  x_choice = random.random() < 1/2
  y_choice = random.random() < 1/2
  if x_choice:
    x = x/(wt + 1)
  else:
    x = (x+wt*600)/(wt + 1)
  if y_choice:
    y = y/(wt + 1)
  else:
    y = (y+wt*500)/(wt + 1)
  if (x_choice^y_choice, y_choice&x_choice) == last:
    color = (255,0,0)
  elif (x_choice, y_choice^x_choice) == last:
    color = (0,255,0)
  else:
    color = (0,0,255)
  last = (x_choice, y_choice)

img.save("/Users/pk/personal/art/sandbox/tmp/tmp.png")

