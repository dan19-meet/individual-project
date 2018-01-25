from Ball import *
import turtle 
import time
import random
import sys

##TODO
##SET THE SCREEN SIZE TO THE SIZE OF THE MONITOR 
turtle.setup(2000, 2000)
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() / 2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height() / 2)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUN_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

MINIMUM_ENEMY_DX = -3
MAXIMUM_ENEMY_DX = 3
MINIMUM_ENEMY_DY = -3
MAXIMUM_ENEMY_DY = 3
ACCELARATION_OF_BALL = 5

RADIUS_TO_WIN = 1000

##WRITE CLONE
writeToScreen = turtle.clone()
writeToScreen.color("grey")
writeToScreen.ht()

MIN_FOOD_RADIUS = 3
MAX_FOOD_RADIUS = 7
MAX_FOOD_NUM = 100

##The decay value of the ball
DECAY = 0.003

BALLS = []
FOOD = []

MY_BALL = Ball(0, 0, 2, 2, 30, (25, 25, 125))

RUNNING = True
SLEEP = 0.0077

turtle.tracer(0)
turtle.ht()

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

def createEnemies():
	isCrash = True
	
	for i in range(NUMBER_OF_BALLS):
		isCrash = True

		while isCrash == True:
			radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUN_BALL_RADIUS)
			x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)

			while ((x < MY_BALL.x + MY_BALL.radius + radius and x > MY_BALL.x - MY_BALL.radius - radius) and (y < MY_BALL.y + MY_BALL.radius + radius and y > MY_BALL.y - MY_BALL.radius - radius) and MY_BALL.radius < MAXIMUN_BALL_RADIUS):
				x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)	

			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			dx = 0
			dy = 0

			while (dx == 0):
				dx = random.randint(MINIMUM_ENEMY_DX, MAXIMUM_ENEMY_DX)

			while (dy == 0):
				dy = random.randint(MINIMUM_ENEMY_DY, MAXIMUM_ENEMY_DX)

			ball = Ball(x, y, dx, dy, radius, color)

			if collide(MY_BALL, ball) != True:
				BALLS.append(ball)
				isCrash = False
			else:
				ball.ht()
				del ball
				

createEnemies()

# Will create food if there is less than X food in the map
def createFood():
	isCreateFood = random.random()

	if isCreateFood < 0.1 and len(FOOD) < MAX_FOOD_NUM:
		x = random.randint(-SCREEN_WIDTH + MAX_FOOD_RADIUS, SCREEN_WIDTH - MAX_FOOD_RADIUS)
		y = random.randint(-SCREEN_HEIGHT + MAX_FOOD_RADIUS, SCREEN_HEIGHT - MAX_FOOD_RADIUS)
		radius = random.randint(MIN_FOOD_RADIUS, MAX_FOOD_RADIUS)
		color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

		food = Ball(x, y, 0, 0, radius, color)
		FOOD.append(food)

def moveAllBalls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def checkAllBallsCollision():
	for ballA in BALLS:
		for ballB in BALLS:
			isColliding = collide(ballA, ballB)

			if isColliding == True:
				ballARadius = ballA.radius
				ballBRadius = ballB.radius

				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUN_BALL_RADIUS)
				x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
				y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)

				while ((x < MY_BALL.x + MY_BALL.radius + radius and x > MY_BALL.x - MY_BALL.radius - radius) and (y < MY_BALL.y + MY_BALL.radius + radius and y > MY_BALL.y - MY_BALL.radius - radius) and MY_BALL.radius < MAXIMUN_BALL_RADIUS):
					x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
					y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)
					print("BLA BLA BLA" + str(random.random()))	
				
				dx = 0
				dy = 0

				while (dx == 0):
					dx = random.randint(MINIMUM_ENEMY_DX, MAXIMUM_ENEMY_DX)


				while (dy == 0):
					dy = random.randint(MINIMUM_ENEMY_DY, MAXIMUM_ENEMY_DX)

				color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

				if ballARadius > ballBRadius:
					ballB.setBall(x, y, dx, dy, radius, color)
				else:
					ballA.setBall(x, y, dx, dy, radius, color)

def checkMyBallCollision():
	for ball in BALLS:
		isColliding = collide(MY_BALL, ball)

		if isColliding == True:
			MY_BALL_RADIUS = MY_BALL.radius
			ballRadius = ball.radius

			x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)

			radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUN_BALL_RADIUS)
			while ((x < MY_BALL.x + MY_BALL.radius + radius and x > MY_BALL.x - MY_BALL.radius - radius) and (y < MY_BALL.y + MY_BALL.radius + radius and y > MY_BALL.y - MY_BALL.radius - radius) and MY_BALL.radius < MAXIMUN_BALL_RADIUS):
					x = random.randint(-SCREEN_WIDTH + MAXIMUN_BALL_RADIUS, SCREEN_WIDTH - MAXIMUN_BALL_RADIUS)
					y = random.randint(-SCREEN_HEIGHT + MAXIMUN_BALL_RADIUS, SCREEN_HEIGHT - MAXIMUN_BALL_RADIUS)
					print("BLA BLA BLA" + str(random.random()))

			dx = 0
			dy = 0

			while (dx == 0):
				dx = random.randint(MINIMUM_ENEMY_DX, MAXIMUM_ENEMY_DX)

			while (dy == 0):
				dy = random.randint(MINIMUM_ENEMY_DY, MAXIMUM_ENEMY_DX)

			color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

			if MY_BALL_RADIUS >= ballRadius:
				MY_BALL.radius += ball.radius / 4
				MY_BALL.setRadius(MY_BALL.radius)

				ball.setBall(x, y, dx, dy, radius, color)
				return True
			else:
				print("CRASH")
				return False

	return True


def moveAround(event):
	mouseX = event.x - SCREEN_WIDTH
	mouseY = -(event.y - SCREEN_HEIGHT)

	ballX = MY_BALL.x
	ballY = MY_BALL.y

	distanceX = mouseX - ballX
	distanceY = mouseY - ballY

	MY_BALL.dxv = (distanceX / (MY_BALL.radius * ACCELARATION_OF_BALL)) * MY_BALL.dx
	MY_BALL.dyv = (distanceY / (MY_BALL.radius * ACCELARATION_OF_BALL)) * MY_BALL.dy

	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)

	#print("X: " + str(mouseX) + " Y: " + str(mouseY) + "\nPX : " + str(ballX) + " PY: " + str(ballY) + "\n\n")
	#print(str(SCREEN_WIDTH) + " : " + str(SCREEN_HEIGHT))

def moveMyBall():
	global RUNNING 

	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	if checkMyBallCollision() == False:
		RUNNING = False

	checkAllBallsCollision()


def eatFood():
	index = 0

	for food in FOOD:
		isColliding = collide(MY_BALL, food)

		if isColliding == True:
			MY_BALL.radius += food.radius / 2
			MY_BALL.setRadius(MY_BALL.radius)

			x = random.randint(-SCREEN_WIDTH + MAX_FOOD_RADIUS, SCREEN_WIDTH - MAX_FOOD_RADIUS)
			y = random.randint(-SCREEN_HEIGHT + MAX_FOOD_RADIUS, SCREEN_HEIGHT - MAX_FOOD_RADIUS)
			radius = random.randint(MIN_FOOD_RADIUS, MAX_FOOD_RADIUS)

			#Makes the food disappearing!
			food.hideBall()

			FOOD.pop(index)
			##DELETE FOOD

		index += 1

def decay():
	MY_BALL.radius -= DECAY
	MY_BALL.setRadius(MY_BALL.radius)

def score():
    writeToScreen.goto(-SCREEN_WIDTH + 10, -SCREEN_HEIGHT + 10)
    writeToScreen.clear()
    writeToScreen.write("Score: " + str(int(MY_BALL.radius * 2)), False, "left", ("Julee", 16, "normal"))

def youWin():
	writeToScreen.color(200, 200, 200)
	writeToScreen.goto(-SCREEN_WIDTH / 2, 0)
	writeToScreen.clear()
	writeToScreen.write("You WIN", False, "left", ("Julee", 100, "normal"))

def youLose():
	writeToScreen.color(200, 200, 200)
	writeToScreen.goto(-SCREEN_WIDTH / 2, 0)
	writeToScreen.clear()
	writeToScreen.write("You LOSE", False, "left", ("Julee", 100, "normal"))


while (RUNNING):
	global SCREEN_WIDTH, SCREEN_HEIGHT

	if (SCREEN_WIDTH != int(turtle.getcanvas().winfo_width() / 2) or SCREEN_HEIGHT != int(turtle.getcanvas().winfo_height() / 2)):
		SCREEN_WIDTH = int(turtle.getcanvas().winfo_width() / 2)
		SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height() / 2)

	moveAllBalls()
	moveMyBall()
	eatFood()
	createFood()
	turtle.getcanvas().bind('<Motion>', moveAround)
	
	##ACTIVATE DECAY HERE
	#if MY_BALL.radius > MINIMUM_BALL_RADIUS:
	#	decay()

	score()

	if MY_BALL.radius > RADIUS_TO_WIN:
		youWin()
		time.sleep(3)
		sys.exit()
		RUNNING = False

	##ACTIVATE TO BREAK GAME
	#if MY_BALL.radius > 300:
	#	break;

	getscreen().update()
	time.sleep(SLEEP)

youLose()
time.sleep(2)
print("END GAME!!!")

##TODO:
##- ADD FOOD - YES
##- DELETE FOOD FROM LIST - YES
##- CREATE A FUNCTION THAT GENERATES DIFFERENT VARIABLES FOR - X, Y, DX, DY ....... - NO
##- DECREASE SPEED AS THE MASS GOES UP - YES
##- How to delete objects - YES
##- Make skins by loading pictures on the circle's surface - NO
##- Make main menu ADD CREDITS HERE! - WILL BE IN PROGRESS
##- Make Score -YES
##- Make YOU WIN screen and Credits Screen (INCLUDE URIEL) - IN PROGRESS
##- make full screen - YES
##- make big enemies go slower - YES!
##- FIX SPAWN ISSUES - YES!!
##- CHANGE ALL MAXIMUN_BALL_RADIUS TO MAXIMUM_BALL_RADIUS - I ACCIDENTALY SWAP THE N AND THE M - NO
##- MAKE YOUR ENEMY MOVE WITH YOUR HEAD