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
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.turret_image = pygame.image.load(image2_path)
        self.turret_rect = self.turret_image.get_rect()
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
        rotated_image = pygame.transform.rotate(self.image, -self.angle*180.0 / pi)
        rotated_turret_image = pygame.transform.rotate(self.turret_image, -self.turret_angle*180.0 / pi)
        rotated_rect = rotated_image.get_rect()
        rotated_turret_rect = rotated_turret_image.get_rect()
        rotated_rect.center = self.position
        rotated_turret_rect.center = self.position
        surface.blit(rotated_image, rotated_rect)
        surface.blit(rotated_turret_image, rotated_turret_rect)
