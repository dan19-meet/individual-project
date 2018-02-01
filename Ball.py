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

		self.dxv = dx
		self.dyv = dy

		self.radius = r
		self.playerColor = color

		self.shape("circle")
		self.shapesize(self.radius / 10)

		##??
		self.color(self.playerColor)


	def __del__(self):
		print("deleted")

	def move(self, screenWidth, screenHeight):
		currentX = self.x
		newX = currentX + self.dxv
		self.x = newX

		currentY = self.y
		newY = currentY + self.dyv
		self.y = newY

		rightSideBall = newX + self.radius
		leftSideBall = newX - self.radius
		upSideBall = newY + self.radius
		downSideBall = newY - self.radius

		if ((rightSideBall >= screenWidth)):
			self.dxv = -self.dxv

		if (leftSideBall <= -(screenWidth)):
			self.dxv = -self.dxv

		if (upSideBall >= screenHeight):
			self.dyv = -self.dyv

		if (downSideBall <= -(screenHeight)):
			self.dyv = -self.dyv

		self.goto(newX, newY)

	def setRadius(self, radius):
		self.shapesize(self.radius / 10)

	def setBall(self, x, y, dx, dy, radius, color):
		self.x = x
		self.y = y
		self.goto(x, y)

		self.dx = dx
		self.dy = dy
		self.dxv = dx
		self.dyv = dy
		self.radius = radius
		self.playerColor = color

		self.shape("circle")
		self.shapesize(self.radius / 10)
		self.color(self.playerColor)

	def hideBall(self):
		self.ht()