import random
from pattern_drawer import PatternDrawer

def x1(a,b,c):
  return a

def x8(a,b,c):
  x = a.real + 10**-8*random.random()
  y = b.real + 10**-8*(1+random.random())
  z = c.real + 10**-8*(1+random.random())
  return (y + z - x)

def x10(a,b,c):
  return b + c

def x11(a,b,c):
  x = a.real + 10**-8*random.random()
  y = b.real + 10**-8*(1+random.random())
  z = c.real + 10**-8*(1+random.random())
  return (y + z - x)*(y - z)**2

def x31(a,b,c):
  return a**3

def x37(a,b,c):
  return a*(b + c)

def x76(a,b,c):
  x = a.real + 10**-8*random.random()
  y = b.real + 10**-8*(1+random.random())
  z = c.real + 10**-8*(1+random.random())
  return x**-2

PatternDrawer(x10) \
  .draw_image(
    colors=[(255,255,255), (255,255,255), (255,255,255), (255,255,255)],
    number_of_points=1_000_000,
    radius=5,
    opacity=0.25,
    image_name=str(0).rjust(4, "0")
  )
