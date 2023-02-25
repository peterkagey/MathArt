from PIL import Image, ImageDraw
import random

rng_1 = random.Random()
rng_2 = random.Random()

s = 1             # `s` for scale
shrink_factor = 5 # Canvas width will be x_max * scale/shrink_factor
# For a x_max by y_max canvas, set s = shrink_factor.
# This makes it s*x_max in memory, and then resamples to s*x_max/shrink_factor.
x_max = 4000
y_max = 6000
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
    return (rng_1.randint(0,255),rng_1.randint(0,255),rng_1.randint(0,255))

def neighborhood_color(x, y):
    x0 = (x - s) % int(x_max * s)
    x1 = (x + s) % int(x_max * s)
    y0 = (y - s) % int(y_max * s)
    y1 = (y + s) % int(y_max * s)
    all_neighbors = []
    for a in [x0, x, x1]:
        for b in [y0, y, y1]:
            all_neighbors += [pixels[a, b]]
    non_white_colors = list(filter(lambda z: z != (255,255,255), all_neighbors))
    if non_white_colors == []:
        return random_color()
    else:
        return average(non_white_colors)

def draw_random_circle(r=250):
    # The second RNG is for backwards compatibility.
    if int(s//5) > 0:
        y_d = rng_2.randrange(int(s//5))
        x_d = rng_2.randrange(int(s//5))
    else:
        (x_d,y_d) = (0,0)
    # The *5 and /5 is for backwards compatibility.
    y = int(rng_1.randrange(0, y_max*5) * (s/5) + y_d)
    x = int(rng_1.randrange(0, x_max*5) * (s/5) + x_d)
    drawing_context.ellipse([x-r,y-r,x+r,y+r],fill=neighborhood_color(x, y))

def file_name(name):
    return "/Users/pk/personal/art/random_circles_wall_art/static_images/" + name + ".png"

def draw_frame(canvas_number):
    x = int(x_max*s//shrink_factor)
    y = int(y_max*s//shrink_factor)
    img.resize((x,y)).save(file_name(str(canvas_number).zfill(3)))

for seed_number in [1,2]:
    rng_1 = random.Random(seed_number)
    rng_2 = random.Random(seed_number)

    img = Image.new("RGB", (int(x_max*s), int(y_max*s)), (255,255,255))
    drawing_context = ImageDraw.Draw(img)
    pixels = img.load()

    phase_1 = 200000
    mod_1 = phase_1 // 100
    for i in range(phase_1):
        if i % mod_1 == 0:
            print("first phase (" + str(seed_number) + "): " + str(i//mod_1) + "%", end='\r')
        r = (i**2/40000000 - i/100 + 1005) * s/5
        draw_random_circle(r)
    print("")

    phase_2 = 200000
    mod_2 = phase_2 // 100
    for i in range(phase_2):
        if i % mod_2 == 0:
            print("second phase (" + str(seed_number) + "): " + str(i//mod_2) + "%\r", end='\r')
        r = 2 * s
        draw_random_circle(r)
    print("")

    phase_3 = 2000000
    mod_3 = phase_3 // 100
    for i in range(phase_3):
        if i % mod_3 == 0:
            print("third phase (" + str(seed_number) + "): " + str(i//mod_3) + "%", end='\r')
        r = s
        draw_random_circle(r)
    print("")

    draw_frame(seed_number)
