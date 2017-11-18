import math
from pygame.math import Vector2

class vectorline():
    def __init__(self, a, b):
        self.a = a
        self.v = b - a

    def set_ab(self, a, b):
        self.a = a
        self.v = b - a

    def collide_with_line(self, line2):
        try:
            f2roof = line2.a.y - self.a.y - ((( line2.a.x - self.a.x)* self.v.y)/self.v.x)
            f2 = f2roof / ((self.v.y * line2.v.x / self.v.x) - line2.v.y)
            if f2 >= 0 and f2 <= 1:
                return line2.a + f2 * line2.v
        except (ZeroDivisionError):
            pass
        return None 

    def collide_with_lines(self, lines):
        for l in lines:
            collision_point = collide_with_line(l)
            if collision_point is not None:
                return collision_point
        return None


#Klassendeklaration boundingbox 

class boundingbox():
    def __init__(self, angle, rectangle):
        self.angle = angle
        self.rectangle = rectangle
        self.borders = []
        self.da = Vector2(rectangle.topleft).rotate(angle)
        self.db = Vector2(rectangle.bottomleft).rotate(angle)
        self.dc = Vector2(rectangle.bottomright).rotate(angle)
        self.dd = Vector2(rectangle.topright).rotate(angle)
        self.borders.append(vectorline(rectangle.center + da, rectangle.center + db))
        self.borders.append(vectorline(rectangle.center + db, rectangle.center + dc))
        self.borders.append(vectorline(rectangle.center + dc, rectangle.center + dd))
        self.borders.append(vectorline(rectangle.center + dd, rectangle.center + da))



