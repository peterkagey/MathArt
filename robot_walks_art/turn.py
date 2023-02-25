import math

class Turn:
  def __init__(self, scale, theta, initial_position, initial_angle):
    self.scale    = scale
    self.theta    = theta
    self.position = initial_position
    self.phi      = initial_angle
    self.center   = self.compute_center()

  def sin_d(self, degrees):
    return math.sin(math.radians(degrees))

  def cos_d(self, degrees):
    return math.cos(math.radians(degrees))

# Arc A
class Right(Turn):

  def compute_center(self):
    (x,y) = self.position
    r = self.scale
    c_x = x + r*self.cos_d(self.phi - 90)
    c_y = y + r*self.sin_d(self.phi - 90)
    return (c_x, c_y)

  def draw(self, drawing_context, lower_corner, line_thickness, color):
    (x,y) = lower_corner
    r = (1 + line_thickness/2) * self.scale
    line_width = math.ceil(line_thickness * self.scale)
    (c_x, c_y) = self.center
    bounding_rectangle = [(c_x - x - r, c_y - y - r),(c_x - x + r, c_y - y + r)]
    drawing_context.arc(bounding_rectangle, self.phi + 89 - self.theta, self.phi + 91, width=line_width, fill=color)

  def new_point(self):
    r = self.scale
    (c_x, c_y) = self.center
    x = c_x + r*self.cos_d(self.phi + 90 - self.theta)
    y = c_y + r*self.sin_d(self.phi + 90 - self.theta)
    return (x, y)

  def new_angle(self):
    return self.phi - self.theta

# Arc B
class Left(Turn):

  def compute_center(self):
    (x,y) = self.position
    r = self.scale
    c_x = x + r*self.cos_d(self.phi + 90)
    c_y = y + r*self.sin_d(self.phi + 90)
    return (c_x, c_y)

  def draw(self, drawing_context, lower_corner, line_thickness, color):
    (x,y) = lower_corner
    r = (1 + line_thickness/2) * self.scale
    line_width = math.ceil(line_thickness * self.scale)
    (c_x, c_y) = self.center
    bounding_rectangle = [(c_x - x - r, c_y - y - r),(c_x - x + r, c_y - y + r)]
    drawing_context.arc(bounding_rectangle, self.phi - 91, self.phi - 89 + self.theta, width=line_width, fill=color)

  def new_point(self):
    r = self.scale
    (c_x, c_y) = self.center
    x = c_x + r*self.cos_d(self.phi - 90 + self.theta)
    y = c_y + r*self.sin_d(self.phi - 90 + self.theta)
    return (x, y)

  def new_angle(self):
    return self.phi + self.theta

