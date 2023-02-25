from PIL import Image, ImageDraw
import math
import random

random.seed(0)
# Image size (pixels)
scale = 1
line_width = int(20*scale)
tile_size = int(200*scale)

cells_wide = 10
cells_high = 10

WIDTH, HEIGHT = int((cells_wide - 0.5) * tile_size), int(math.sqrt(3)/2 * cells_high * tile_size)

# Create a blank image with a white background
image = Image.new("RGB", (WIDTH, HEIGHT), "white")
draw = ImageDraw.Draw(image)

def random_color(min_light=None, max_light=None):
    lower = min_light or 0
    upper = max_light or 255
    return tuple([random.randint(lower,upper) for _ in range(3)])

def draw_circle(xy, r, color):
    (x,y) = xy
    draw.ellipse((x-r,y-r,x+r,y+r), fill=color)

for i in range(cells_wide):
    for j in range(cells_high):
        x = (i - (j % 2)/2 + 0.5) * tile_size
        y = (1/6 + j/2) * tile_size * math.sqrt(3)
        r = tile_size*math.sqrt(3)/3
        draw.regular_polygon((x,y,r), rotation=180, n_sides=3, fill=random_color(64,128))
        color = random_color(128,196)
        a = (x+tile_size/4,y+tile_size*math.sqrt(3)/12)
        b = (x-tile_size/4,y+tile_size*math.sqrt(3)/12)
        c = (x,y-tile_size*math.sqrt(3)/6)
        d = (x,y)
        step_patterns = [[a,d,b,d,c]]
        step_patterns += [[a,b],[a,c],[b,c]] * 4
        step_patterns += [[a,b,c],[a,c,b],[b,a,c]]
        step_patterns += [[a,d,b,c],[a,d,c,b],[b,d,a,c],[b,d,c,a],[c,d,a,b],[c,d,b,a]]

        draw.line(random.choice(step_patterns),fill=color,width=line_width,joint="curve")

for i in range(cells_wide):
    for j in range(cells_high):
        x = (i + (j % 2)/2) * tile_size
        y = (1/3 + j/2) * tile_size * math.sqrt(3)
        r = tile_size*math.sqrt(3)/3
        draw.regular_polygon((x,y,r), n_sides=3, fill=random_color(128,192))
        color = random_color(64,128)
        a = (x-tile_size/4,y-tile_size*math.sqrt(3)/12)
        b = (x+tile_size/4,y-tile_size*math.sqrt(3)/12)
        c = (x,y+tile_size*math.sqrt(3)/6)
        d = (x,y)
        step_patterns = [[a,d,b,d,c]]
        step_patterns += [[a,b],[a,c],[b,c]] * 4
        step_patterns += [[a,b,c],[a,c,b],[b,a,c]]
        step_patterns += [[a,d,b,c],[a,d,c,b],[b,d,a,c],[b,d,c,a],[c,d,a,b],[c,d,b,a]]
        draw.line(random.choice(step_patterns), fill=color,width=line_width,joint="curve")
        for p in [a,b,c]:
            draw_circle(p, line_width/2, color)

image.resize((int(WIDTH/scale), int(HEIGHT/scale)),Image.LANCZOS).save("/Users/pk/personal/art/truchet/Python/triangle.png")
