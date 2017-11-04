import pygame
import tank_mod
import own_group
import referee

SIZE = (512, 512)

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
running = True
tank1 = tank_mod.tank(3, 5, 1, 1, 0.034, pygame.math.Vector2(512/2, 512/2), 0, 0, "tank.png", "turret.png")
tank2 = tank_mod.tank(3, 5, 1, 1, 0.034, pygame.math.Vector2(512/2, 512/2), 0, 0, "tank.png", "turret.png")
referee = referee.referee([tank1, tank2])
all_sprite= own_group.own_group()
all_sprite.add(tank1, tank2)
while running:
	clock.tick(60)
	events = pygame.event.get()
	for e in events:
		if e.type == pygame.QUIT:
			running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                tank1.update(True, False, False, False, False, False, False)
        if keys[pygame.K_DOWN]:
                tank1.update(False, True, False, False, False, False, False)
        if keys[pygame.K_LEFT]:
                tank1.update(False, False, True, False, False, False, False)
        if keys[pygame.K_RIGHT]:
                tank1.update(False, False, False, True, False, False, False)
        if keys[pygame.K_a]:
                tank1.update(False, False, False, False, True, False, False)
        if keys[pygame.K_d]:
                tank1.update(False, False, False, False, False, True, False)
        if keys[pygame.K_SPACE]:
                tank1.update(False, False, False, False, False, False, True)
        referee.update()
        if tank2.life < 0:
            running = False
        screen.fill((0, 0, 0))
        all_sprite.draw([screen])
	pygame.display.flip()
