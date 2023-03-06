from PIL import Image, ImageDraw
import math
import random

random.seed(2)
# Image size (pixels)
line_width = 50
tile_size = 150

cells_wide = 20
cells_high = 20

WIDTH, HEIGHT = cells_wide * tile_size, cells_high * tile_size


# Create a blank image with a white background
image = Image.new("RGB", (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(image)

def draw_circle(xy, r, color):
    (x,y) = xy
    draw.ellipse((x-r,y-r,x+r,y+r), fill=color)

def fill_square_tile(x, y):
    draw.rectangle([(x-tile_size/2,y-tile_size/2),(x+tile_size/2,y+tile_size/2)], fill=random_color(128,196))

def draw_square_tile(x, y):
    lw = line_width/2
    tw = tile_size + lw
    s = tile_size/2
    if random.random() < 0.5:
        if random.random() < 0.5:
            draw.arc((x-lw,y-lw,x+tw,y+tw),start=180,end=270,fill="black",width=line_width)
        else:
            draw.line((x,y+s,x+s,y),fill="black",width=int(line_width/1.5))
            draw_circle((x,y+s), line_width/2, "black")
            draw_circle((x+s,y), line_width/2, "black")
        if random.random() < 0.5:
            draw.arc((x-tw,y-tw,x+lw,y+lw),start=0,end=90,fill="black",width=line_width)
        else:
            draw.line((x-s,y,x,y-s),fill="black",width=int(line_width/1.5))
            draw_circle((x-s,y), line_width/2, "black")
            draw_circle((x,y-s), line_width/2, "black")
    else:
        if random.random() < 0.5:
            draw.arc((x-lw,y-tw,x+tw,y+lw),start=90,end=180,fill="black",width=line_width)
        else:
            draw.line((x,y-s,x+s,y),fill="black",width=int(line_width/1.5))
            draw_circle((x,y-s), line_width/2, "black")
            draw_circle((x+s,y), line_width/2, "black")
        if random.random() < 0.5:
            draw.arc((x-tw,y-lw,x+lw,y+tw),start=270,end=360,fill="black",width=line_width)
        else:
            draw.line((x-s,y,x,y+s),fill="black",width=int(line_width/1.5))
            draw_circle((x-s,y), line_width/2, "black")
            draw_circle((x,y+s), line_width/2, "black")

def random_color(min_light=None, max_light=None):
    lower = min_light or 0
    upper = max_light or 255
    return tuple([random.randint(lower,upper) for _ in range(3)])

for i in range(cells_wide):
    for j in range(cells_high):
        x = tile_size * i + tile_size/2
        y = tile_size * j + tile_size/2
        fill_square_tile(x, y)

for i in range(cells_wide):
    for j in range(cells_high):
        x = tile_size * i + tile_size/2
        y = tile_size * j + tile_size/2
        draw_square_tile(x, y)

image.save("/Users/pk/personal/art/truchet/Python/square.png")
