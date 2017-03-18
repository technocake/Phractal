#!/usr/bin/env python
# -*- coding: utf-8 -*-


import turtle
from turtle import *
import time
import math


def drawPhree(x, y, d, p=90, n=1):
	""" a simple start """
	branch = Turtle()
	branch.goto(x,y)
	
	if (n==1):
		branch.seth(90)
		branch.forward(d)
	else:
		branch.seth(p)	
		branch.forward(d)
	
	if (n < 10):
		x,y = branch.pos()
		drawPhree(x,y,d, 60, n+1)
		drawPhree(x,y,d, 120, n+1)



if __name__ == '__main__':
	drawPhree(x=0,y=0,d=100)

	turtle.listen()
	turtle.mainloop()