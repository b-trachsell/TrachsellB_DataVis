# importing packages from third parties is the same as local files
# Just import what you need and run the methods

from matplotlib import pyplot
#charting and visualisations
from turtle import *
from random import randint


#these are functions from the turtle library
#just use them
speed(0)
bgcolor('black')

x = 1
r = 0
g = 255
b = 255

while x < 400:
	r = (r + 2)
	g = (g - 2)
	b = (b - 2)

	colormode(255)

	pencolor( r , g , b )

	fd (200 + x)
	rt (90.911)

	x = x + 1



