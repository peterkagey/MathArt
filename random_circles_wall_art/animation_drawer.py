from PIL import Image, ImageDraw
import os
import random

x_max = 20000
y_max = 30000
img = Image.new("RGB", (x_max, y_max), (255,255,255))
drawing_context = ImageDraw.Draw(img)
pixels = img.load()
seed_number = 919
random.seed(919)

def average(triples):
    x0 = 0
    y0 = 0
    z0 = 0
    for (x,y,z) in triples:
        x0 += x
        y0 += y
        z0 += z
    return (x0//len(triples), y0//len(triples), z0//len(triples))

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def neighborhood_color(x, y):
    x0 = (x - 5) % x_max
    x1 = (x + 5) % x_max
    y0 = (y - 5) % y_max
    y1 = (y + 5) % y_max
    all_neighbors = []
    for a in [x0, x, x1]:
        for b in [y0, y, y1]:
            all_neighbors += [pixels[a, b]]
    non_white_colors = list(filter(lambda z: z != (255,255,255), all_neighbors))
    if non_white_colors == []:
        return random_color()
    else:
        return average(non_white_colors)

def draw_new_circle(x, y, r=250):
    drawing_context.ellipse([x-r,y-r,x+r,y+r],fill=neighborhood_color(x, y))

def directory_path():
    custom_path = "/Users/pk/personal/art/random_circles_wall_art/"
    seed = str(seed_number).zfill(3)
    return custom_path + "animations/frames_" + seed

def file_path(frame_count):
    return directory_path() + "/frame" + str(frame_count).zfill(3) + ".png"

def draw_frame(frame_count):
    img.resize((x_max//20,y_max//20)).save(file_path(frame_count))

if not os.path.isdir(directory_path()):
   os.makedirs(directory_path())

frame_count = 0
total_area = 0
for i in range(200000):
    r = i**2/40000000 - i/100 + 1000
    total_area += r

    if total_area > 666661:
        total_area -= 666661
        draw_frame(frame_count)
        frame_count += 1
    y = random.randrange(0, y_max)
    x = random.randrange(0, x_max)
    draw_new_circle(x, y, r)
