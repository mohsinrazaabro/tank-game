import pygame
import time
import random
#import pygame_sdl2
#pygame_sdl2.import_as_pygame()
import sys
from pygame.locals import *


pygame.init()
surface = pygame.display.set_mode((500, 500))
fps_clock = pygame.time.Clock()
fps = 40










class Bullet:

	def __init__(self):


		
		
		self.LBullets = []
		self.RBullets = []
		self.UBullets = []
		self.DBullets = []




	def start(self, surface):

		num = 0
		self.velocity()


		for bulletLoop in (self.UBullets, self.RBullets, self.DBullets, self.LBullets):


			if bulletLoop is not None:
				
				
				#self.velocity(bulletLoop, num)
				innerNum = 0
				for i, j in bulletLoop:

					self.bullet = pygame.image.load('textures/bullet'+str(num)+'.png')
					surface.blit(self.bullet, (i, j))
					if num == 0:
						if j < 50:
							del(self.UBullets[innerNum])
					if num == 1:
						if i > 450:
							del(self.RBullets[innerNum])
						
					if num == 2:
						if j > 450:
							del(self.DBullets[innerNum])
					if num == 3:
						if i < 50:
							del(self.LBullets[innerNum])

						

			num +=1
		



		
		




		

	def shoot(self):
		if tank.state == 'up':
			self.shootUp()
		elif tank.state == 'down':
			self.shootDown()
		elif tank.state == 'left':
			self.shootLeft()
		elif tank.state == 'right':
			self.shootRight()

		




	def shootUp(self):
		self.UBullets += [[tank.tankRect.left+24, tank.tankRect.top]]
		

	def shootDown(self):
		self.DBullets += [[tank.tankRect.left+24, tank.tankRect.top+50]]
		
		

	def shootLeft(self):
		self.LBullets += [[tank.tankRect.left, tank.tankRect.top+23]]
		
		
	def shootRight(self):
		self.RBullets += [[tank.tankRect.left+50, tank.tankRect.top+24]]




	def velocity(self):
		speed = 5

		if self.UBullets is not None:


			for i in range(len(self.UBullets)):
				self.UBullets[i][1]-=speed

		if self.RBullets is not None:
			for i in range(len(self.RBullets)):
				self.RBullets[i][0]+=speed
		if self.DBullets is not None:

			for i in range(len(self.DBullets)):
				self.DBullets[i][1]+=speed
		if self.LBullets is not None:

			for i in range(len(self.LBullets)):
				self.LBullets[i][0]-=speed
		

		


		



class Zombie:
	def __init__(self):
		self.UZombies = []
		self.RZombies = []
		self.DZombies = []
		self.LZombies = []

	def makeZombie(self):

		self.DZombies += [[random.randint(5,460), random.randint(5,460)]]

	def drawZombie(self):
		if self.DZombies is not None:
			for i, j in self.DZombies:
				pygame.draw.rect((255,0,255),i,j )





zombie = Zombie()

class Tank:
	def __init__(self):
		self.white = (255,255,255)
		self.tank = pygame.image.load('textures/tank.png')
		self.tank = pygame.transform.scale(self.tank, (50,50))
		self.tankRect = self.tank.get_rect()
		self.tankRect = self.tankRect.move(0,0)
		self.state = 'up'

		
	def move(self, surface):
		surface.blit(self.tank, self.tankRect)
		
	#	self.tankRect = self.tankRect.move(self.tankRect.left, self.tankRect.top)
		
		
		
	def moveUp(self):
		if self.state != 'up':
			self.state = 'up'
			self.tank = pygame.image.load('textures/tank.png')
			self.tank = pygame.transform.scale(self.tank, (50,50))


		else:
			
		
			self.tankRect = self.tankRect.move(0, -50)

		
		
		
	def moveDown(self):
		if self.state != 'down':
			self.state = 'down'
			self.tank = pygame.image.load('textures/tankDown.png')
			self.tank = pygame.transform.scale(self.tank, (50,50))
			
		else:
			self.tankRect = self.tankRect.move(0, 50)
	
	def moveLeft(self):
		if self.state != 'left':
			self.state = 'left'
			
			self.tank = pygame.image.load('textures/tankLeft.png')
			self.tank = pygame.transform.scale(self.tank, (50,50))
			
		else:
			
			self.tankRect = self.tankRect.move(-50, 0)
			
	
	def moveRight(self):
		if self.state != 'right':
			self.state = 'right'
			self.tank = pygame.image.load('textures/tankRight.png')
			self.tank = pygame.transform.scale(self.tank, (50,50))


		else:
			
			self.tankRect = self.tankRect.move(50, 0)
		
	
		
		
tank = Tank()
class Game:
	def __init__(self):
		self.nothing = 50
		
	def update(self, surface):
		
		
		tank.move(surface)

		
		
bullet = Bullet()
game = Game()	

		
						
while True: # main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == K_LEFT:
					tank.moveLeft()
				elif event.key == K_DOWN:
					tank.moveDown()
				
				elif event.key == K_RIGHT:
					tank.moveRight()
				elif event.key == K_UP:
					tank.moveUp()
				elif event.key == K_z:
					bullet.shoot()
				
		surface.fill((0, 0, 0))
		game.update(surface)
		bullet.start(surface)
		
		
		pygame.display.update()
		fps_clock.tick(fps)