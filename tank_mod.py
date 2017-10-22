# importiert Sprite
from pygame.sprite import Sprite 
from math import sin, cos, pi
from pygame.math import Vector2
import pygame.image

# Klassendeklaration
class tank(Sprite):
    def __init__(self, life, armor, velocity, reload_time, damage, 
        turret_velocity, position, angle, turret_angle, image_path, image2_path):
        Sprite.__init__(self)
        self.life = life
        self.armor = armor
        self.velocity = velocity
        self.angle_velocity = self.velocity * 0.5
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

    def update(self, forward, backward, left, right, turret_left, turret_right, shoot):
        rad_angle = -(float(self.angle)/180.0) * pi
        if forward:
           self.position += Vector2(cos(rad_angle), sin(rad_angle)) * self.velocity
        if backward:
           self.position += Vector2(cos(rad_angle), sin(rad_angle)) * (-self.velocity)
        if left:
           self.angle -= self.angle_velocity
        if right:
           self.angle += self.angle_velocity
        if turret_left:
            self.turret_angle -= self.turret_velocity
        if turret_right:
            self.turret_angle += self.turret_velocity

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_turret_image = pygame.transform.rotate(self.turret_image, self.turret_angle)
        rotated_rect = rotated_image.get_rect()
        rotated_turret_rect = rotated_turret_image.get_rect()
        rotated_rect.center = self.position
        rotated_turret_rect.center = self.position
        surface.blit(rotated_image, rotated_rect)
        surface.blit(rotated_turret_image, rotated_turret_rect)
