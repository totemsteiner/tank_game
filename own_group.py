from pygame.sprite import Group


class own_group(Group):
	def __init__(self):
            Group. __init__(self)

	def draw(self, args):
		for s in self.sprites():
			s.draw(*args)
