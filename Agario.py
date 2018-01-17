from Ball import *
import turtle 
import time
import random

SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() / 2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height() / 2)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUN_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

MY_BALL = Ball(0, 0, MAXIMUM_BALL_DX, MAXIMUM_BALL_DY, MINIMUM_BALL_RADIUS, (25, 25, 125))

RUNNING = True
SLEEP = 0.0077

turtle.tracer(0)
turtle.ht()

dxZero = True
dyZero = True
for i in range(NUMBER_OF_BALLS):
	x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
	y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)

	while (dxZero == True):
		dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
		if (dx != 0):
			dxZero = False

	while (dyZero == True):
		dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DX)
		if (dy != 0):
			dyZero = False

	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUN_BALL_RADIUS)
	color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	ball = Ball(x, y, dx, dy, radius, color)
	BALLS.append(ball)

def moveAllBalls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def collide(ball1, ball2):
		if (ball1 == ball2):
			return False

		distanceX = ball1.x - ball2.x
		distanceY = ball1.y - ball2.y

		distanceCircles = math.sqrt(math.pow(distanceX, 2) + math.pow(distanceY, 2))
		radiusSum = ball1.radius + ball2.radius

		if (distanceCircles + 10 <= radiusSum):
			return True
		else:
			return False


def checkAllBallsCollision():
	for ballA in BALLS:
		for ballB in BALLS:
			isColliding = collide(ballA, ballB)

			if isColliding == True:
				ballARadius = ballA.radius
				ballBRadius = ballB.radius

				x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)

				while (dxZero == True):
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
					if (dx != 0):
						dxZero = False

				while (dyZero == True):
					dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DX)
					if (dy != 0):
						dyZero = False

				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUN_BALL_RADIUS)
				color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

				if ballARadius > ballBRadius:
					###



while (True):
	moveAllBalls()
	getscreen().update()

mainloop()