# collision detection 
from pygame.math import Vector2
from math import atan2

# referee class

class referee():
	def __init__(self, tank_list, offset = 0.43):
		self.tank_list = tank_list
                self.offset = offset

	def register_tank(self, tank):
		self.tank_list.append(tank)
        
        def update(self):
            for tank in self.tank_list:
                if tank.shot == True:
                    for t in self.tank_list:
                        if t is tank:
                            continue
                        diff = t.position - tank.position
                        diff_angle = atan2(diff.y, diff.x)
                        print "diff_angle: " + str(diff_angle)
                        print "turret_angle: " + str(tank.turret_angle)
                        if diff_angle > tank.turret_angle - self.offset and diff_angle < tank.turret_angle + self.offset:
                            t.life -= tank.damage
                        tank.shot = False


