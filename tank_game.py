import pygame
import tank_mod
import own_group

SIZE = (512, 512)

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
tank = tank_mod.tank(0, 0, 5, 0, 0, 2, pygame.math.Vector2(512/2, 512/2), 0, 0, "tank.png", "turret.png")
all_sprite= own_group.own_group()
all_sprite.add(tank)
while running:
	clock.tick(60)
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.QUIT:
			running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                tank.update(True, False, False, False, False, False, False)
        if keys[pygame.K_DOWN]:
                tank.update(False, True, False, False, False, False, False)
        if keys[pygame.K_LEFT]:
                tank.update(False, False, True, False, False, False, False)
        if keys[pygame.K_RIGHT]:
                tank.update(False, False, False, True, False, False, False)
        if keys[pygame.K_a]:
                tank.update(False, False, False, False, True, False, False)
        if keys[pygame.K_d]:
                tank.update(False, False, False, False, False, True, False)
        screen.fill((0, 0, 0))
        all_sprite.draw([screen])
	pygame.display.flip()
