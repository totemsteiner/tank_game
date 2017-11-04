# importiert Sprite
from pygame.sprite import Sprite 
from math import sin, cos, pi
from pygame.math import Vector2
import pygame.image
import time


# Klassendeklaration
class tank(Sprite):
    def __init__(self, life, velocity, reload_time, damage, 
        turret_velocity, position, angle, turret_angle, image_path, image2_path):
        Sprite.__init__(self)
        self.life = life
        self.velocity = velocity
        self.angle_velocity = 0.034
        self.reload_time = reload_time
        self.damage = damage
        self.turret_angle = turret_angle
        self.turret_velocity = turret_velocity
        self.position = position
        self.angle = angle
        self.image1 = pygame.image.load(image_path)
        self.rect1 = self.image1.get_rect()
        self.rect1.center = position
        self.image2 = pygame.image.load(image2_path)
        self.rect2 = self.image2.get_rect()
        self.shot = False
        self.timestamp_last_shot = 0

    def update(self, forward, backward, left, right, turret_left, turret_right, shoot):
        if forward:
           self.position += Vector2(cos(self.angle), sin(self.angle)) * self.velocity
        if backward:
           self.position += Vector2(cos(self.angle), sin(self.angle)) * (-self.velocity)
        if left:
           self.angle = (self.angle - self.angle_velocity) % (2 * pi)
        if right:
           self.angle = (self.angle + self.angle_velocity) % (2 * pi)
        if turret_left:
            self.turret_angle = (self.turret_angle- self.turret_velocity) % (2 * pi)
        if turret_right:
            self.turret_angle = (self.turret_angle + self.turret_velocity) % (2 * pi)
        if shoot:
            current_timestamp = time.time()
            if (current_timestamp - self.timestamp_last_shot) > self.reload_time:
                self.shot = True 
                self.timestamp_last_shot = current_timestamp


    def draw(self, surface):
        rotated_image1 = pygame.transform.rotate(self.image1, -self.angle*180.0 / pi)
        rotated_image2 = pygame.transform.rotate(self.image2, -self.turret_angle*180.0 / pi)
        self.rect1 = rotated_image1.get_rect()
        self.rect2 = rotated_image2.get_rect()
        self.rect1.center = self.position
        self.rect2.center = self.position
        surface.blit(rotated_image1, self.rect1)
        surface.blit(rotated_image2, self.rect2)
