from PIL import Image, ImageDraw
import math
import random

class TruchetTile():

    def __init__(self, vertex_count, side_length=100, color=(255,222,255), scale=1):
        self.vertex_count = vertex_count
        self.s = scale
        self.radius = side_length/2/math.sin(3.14159/self.vertex_count)
        self.color = color
        width  = 2*math.ceil(self.radius)*scale
        height = 2*math.ceil(self.radius)*scale
        self.image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        self.draw = ImageDraw.Draw(self.image)
        self.vertices = self.make_polygon()
        self.draw_border()

    def image_center(self):
        x = math.ceil(self.radius)*self.s
        y = math.ceil(self.radius)*self.s
        return (x,y)

    def shift_to_center(self, points_list):
        (delta_x, delta_y) = self.image_center()
        new_points_list = []
        for (x, y) in points_list:
            new_points_list.append((x + delta_x, y + delta_y))
        return new_points_list

    def scale_points_list(self, points_list):
        new_points_list = []
        for (x, y) in points_list:
            new_points_list.append((self.s*x, self.s*y))
        return new_points_list

    def make_polygon(self):
        vertices = []
        for i in range(self.vertex_count):
            x = self.radius*math.cos(i*3.14159*2/self.vertex_count)
            y = self.radius*math.sin(i*3.14159*2/self.vertex_count)
            vertices.append((x, y))
        return self.scale_points_list(self.shift_to_center(vertices))

    def draw_border(self):
        self.draw.polygon(self.vertices, fill=self.color, width=self.s*1)

    def midpoint(self, p1, p2):
        (x1,y1) = p1
        (x2,y2) = p2
        return ((x1+x2)/2,(y1+y2)/2)

    def get_arc_info(self, e1, e2, v1, v2):
        (ex1, ey1) = e1
        (ex2, ey2) = e2
        (vx1, vy1) = v1
        (vx2, vy2) = v2
        if (abs(ex2-ex1) > self.s):
            t = (ex2-ex1)/(vx1-ex1+vx2-ex2)
        else:
            t = (ey2-ey1)/(vy1-ey1+vy2-ey2)
        x = ex1+t*(vx1-ex1)
        y = ey1+t*(vy1-ey1)

        side_length = self.radius*abs(math.sin(3.14159/self.vertex_count))
        r = self.s*side_length*abs(t) + 5*self.s

        theta1 = math.acos((ex1-x)/math.sqrt(((ex1-x)**2 + (ey1-y)**2)))*360/2/3.14159
        theta2 = math.acos((ex2-x)/math.sqrt(((ex2-x)**2 + (ey2-y)**2)))*360/2/3.14159

        if (ey1-y) < 0:
            theta1 = 360 - theta1
        if (ey2-y) < 0:
            theta2 = 360 - theta2
        return (theta1, theta2, x, y, r)

    def draw_arc(self, begin_index, end_index, color):
        if 2*((end_index - begin_index) % self.vertex_count) < self.vertex_count:
            return self.draw_arc(end_index, begin_index, color)
        (vx1, vy1) = self.vertices[begin_index % self.vertex_count]
        (vx2, vy2) = self.vertices[end_index % self.vertex_count]
        (ex1, ey1) = self.midpoint((vx1,vy1), self.vertices[(begin_index+1) % self.vertex_count])
        (ex2, ey2) = self.midpoint((vx2,vy2), self.vertices[(end_index+1) % self.vertex_count])
        if 2*((begin_index - end_index) % self.vertex_count) == self.vertex_count:
            self.draw.line([ex1, ey1, ex2, ey2], fill=color, width=10*self.s)
        else:
            (theta1, theta2, x, y, r) = self.get_arc_info((ex1, ey1), (ex2, ey2), (vx1, vy1), (vx2, vy2))
            self.draw.arc([x-r,y-r,x+r,y+r], start=theta1, end=theta2, fill=color, width=10*self.s)

    def draw_random_arcs(self, color="orange"):
        if self.vertex_count % 2 == 0:
            all_numbers = list(range(self.vertex_count))
            subset = random.sample(all_numbers, self.vertex_count//2)
            complementary_subset = list(set(all_numbers)-set(subset))
            random.shuffle(subset)
            random.shuffle(complementary_subset)
        elif self.vertex_count == 3:
            x1 = ([1,1],[2,3])
            x2 = ([2,2],[1,3])
            x3 = ([3,3],[1,2])
            (subset, complementary_subset) = random.choice([x1,x2,x3])
        else:
            raise ValueError("This only works on 2n-gons and triangles!")

        for i in range(math.ceil(self.vertex_count/2)):
            self.draw_arc(subset[i], complementary_subset[i], color)

    def draw_at(self, canvas, draw_at, theta):
        (image_center_x, image_center_y) = self.image_center()
        (x_delta, y_delta) = draw_at
        tile = self.image.rotate(theta)
        canvas.paste(tile, (x_delta-image_center_x, y_delta-image_center_y), tile)
