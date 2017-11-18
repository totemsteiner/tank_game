from pygame.math import Vector2 as v
from boundingbox import vectorline as vl

line1 = vl(v(0,0), v(10, 0))
line2 = vl(v(0, -1), v(10, -1))

p = line1.collide_with_line(line2)
print p
