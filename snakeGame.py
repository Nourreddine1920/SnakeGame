import pygame, sys, os
from pygame.locals import *
from random import randrange
os.environ["SDL_VIDEO_CENTERED"]='1'

def setFood():
	global snake
	(x, y) = (randrange(0, 290, 10),randrange(0, 290, 10))
	while (x, y) in snake:
		(x, y) = (randrange(0, 290, 10),randrange(0, 290, 10))
	return (x, y)


pygame.init()
wn = pygame.display.set_mode((300, 380))
score = 0
pygame.display.set_caption(f"Snake - Score : 0")
mainClock = pygame.time.Clock()
snake = [(150, 190), (150, 200), (150, 210)]
food = setFood()
side = 10
direction = "U"

while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key in [K_UP, K_w]:
				if direction != "D":
					direction = "U"
			elif event.key in [K_DOWN, K_s]:
				if direction != "U":
					direction = "D"
			elif event.key in [K_LEFT, K_a]:
				if direction != "R":
					direction = "L"
			elif event.key in [K_RIGHT, K_d]:
				if direction != "L":
					direction = "R"

	wn.fill((0,0,0))
	x, y = snake[0]
	if direction == "U":
		y-=10
	elif direction == "D":
		y+=10
	elif direction == "L":
		x-=10
	elif direction == "R":
		x+=10
	snake = [(x, y)] + snake[:-1]
	if x in [-10, 300] or y in [-10, 380] or (x, y) in snake[1:]:
		pygame.quit()
		sys.exit()
	if snake[0] == food:
		snake.append(snake[-1])
		food = setFood()
		score += 1
		pygame.display.set_caption(f"Snake - Score : {score}")

	for seg in snake:
		pygame.draw.rect(wn, (255,255,255), (*seg, side, side))
	pygame.draw.rect(wn, (255,0,0), (*food, side, side))
	pygame.display.update()
	mainClock.tick(15)