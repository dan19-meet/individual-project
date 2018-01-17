from turtle import *
import math

colormode(255)
class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)

		pu()
		ht()

		self.pu()

		self.goto(x, y)

		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.radius = r
		self.playerColor = color

		self.shape("circle")
		self.shapesize(self.radius / 10)

		##??
		self.color(self.playerColor)

	def move(self, screenWidth, screenHeight):
		currentX = self.x
		newX = currentX + self.dx

		currentY = self.y
		newY = currentY + self.dy

		rightSideBall = newX + self.radius
		leftSideBall = newX - self.radius
		upSideBall = newY + self.radius
		downSideBall = newY - self.radius

		if (rightSideBall >= screenWidth):
			self.dx = -self.dx

		if (leftSideBall <= -(screenWidth)):
			self.dx = -self.dx

		if (upSideBall >= screenHeight):
			self.dy = -self.dy

		if (rightSideBall <= -(screenHeight)):
			self.dy = -self.dy

		self.goto(newX, newY)
