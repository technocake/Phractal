#!/usr/bin/env python
# -*- coding: utf-8 -*-

from turtle import Turtle, Screen

screen = Screen()

base_turtle = Turtle()

base_turtle.speed(0)


for i in range(1,9):
  new_tut = base_turtle.clone()
  new_tut.left(45*i)
  new_tut.forward(200)

  print("theta: ", round(new_tut.heading()) ,"rad: ", round(new_tut.distance(base_turtle)))



screen.mainloop()