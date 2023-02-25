from PIL import Image, ImageDraw
from turn import Left, Right
import random
import math

class CircleSpiralDrawer:
  def __init__(self, step_size, layers, layer_function, step_pattern=None, resolution=None):
    self.step_size  = step_size
    self.seed       = step_pattern or self.random_step_pattern()
    self.resolution = resolution or 100
    self.theta      = 360/self.step_size
    self.layers     = layers
    self.layer_function = layer_function
    self.phi        = 0    # Initial angle
    self.position   = (0,0) # Initial position
    self.construct_walk()

  def random_step_pattern(self, step_count=None):
    steps = step_count or random.randint(8,32)
    def is_invalid(pattern):
      bits = [0,0]
      while pattern > 0:
        bits[pattern % 2] += 1
        pattern >>= 1
      return (bits[0] - bits[1]) % self.step_size == 0
    pattern = random.randint(2**(steps - 1), 2**steps - 1)
    while is_invalid(pattern):
      print(pattern, "was not valid!")
      pattern = random.randint(2**(steps - 1), 2**steps - 1)
    return pattern

  def construct_pattern(self):
    step_value = self.seed
    walk_pattern = []
    while step_value > 0:
      if step_value & 1 == 1:
        walk_pattern.insert(0, Left)
      else:
        walk_pattern.insert(0, Right)
      step_value >>= 1
    return walk_pattern

  def construct_walk(self):
    self.walk = []
    for s in self.construct_pattern() * self.step_size:
      t = s(self.resolution, self.theta, self.position, self.phi)
      self.walk.append(t)
      self.position = t.new_point()
      self.phi = t.new_angle()
    return self.walk

  def trace_walk(self, image_center, line_thickness=0.2, color="blue"):
    for s in self.construct_walk():
      s.draw(self.ctx, image_center, line_thickness, color)

  def canvas_size(self):
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for (x, y) in map(lambda s: s.position, self.walk):
      min_x = min(x, min_x)
      min_y = min(y, min_y)
      max_x = max(x, max_x)
      max_y = max(y, max_y)
    return (min_x, min_y, max_x, max_y)

  def trace_walks(self, lower_corner, image_size):
    line_size = 0.01*max(image_size)/self.resolution
    for i in list(range(self.layers))[::-1]:
      (line_width, layer_color) = self.layer_function(i)
      self.trace_walk(lower_corner, line_thickness=line_width*line_size, color=layer_color)

  def get_default_filename(self):
    return "robot_walk_" + str(self.step_size) + "_" + str(self.layers) + "_" + str(self.seed)

  def draw_image(self, filename = None):
    filename = filename or self.get_default_filename()
    (x_min, y_min, x_max, y_max) = self.canvas_size()
    walk_height = math.ceil(y_max - y_min)
    walk_width  = math.ceil(x_max - x_min)
    max_dimension = max(walk_height, walk_width)
    last_layer_thickness = self.layer_function(self.layers)[0]
    margin = int(last_layer_thickness*0.01*max_dimension)
    image_size = (max_dimension + 2*margin, max_dimension + 2*margin)
    img = Image.new("RGBA", image_size, (255,255,255,0))  # create new Image
    self.ctx = ImageDraw.Draw(img)  # create drawing context
    lower_corner = (x_min - margin, y_min - margin)
    self.trace_walks(lower_corner, image_size)
    del self.ctx
    if walk_height > 2048:
      img = img.resize((2048,2048), resample=Image.LANCZOS)
    file_name = "/Users/pk/personal/art/robot_walks_art/tmp/" + filename + ".png"
    img.save(file_name)
