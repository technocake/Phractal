#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# @author  Jonas Solsvik
# @email   jonasjso@stud.ntnu.no
# @created 19.03.17
# @file    graph_animator.py
# @brief   Takes "fileformat.graph"-kind of files and draws
#           a graph based on it, layer by layer.


import file_parser as parser
from turtle import Turtle, Screen
  
filepath = "file/fileformat.graph" # File to load the graph from


def read_file_graph():
  graph=[]

  with open(filepath, "r") as graphfile:

    current_layer = -1

    for line in graphfile.readlines():
        
      if line.find("layer:") > -1:
        current_layer += 1
        graph.append([])

      elif line.find("node:") > -1:
        node = parser.serialize_graph_node(line)
        graph[current_layer].append(node)

  return graph

def display_graph_data(graph):

  for layer in graph:
    for node in layer:
      print(node)


def turtle_factory(node):

  scale = .5

  tut = Turtle()

  tut.hideturtle()
  tut.penup()
  tut.shapesize(node["size"]*scale)
  tut.color(node["color"])
  tut.setheading(node["theta"])
  tut.forward(node["radius"])
  tut.shape("circle")
  tut.speed(0)
  tut.pendown()
  tut.showturtle()

  node["turtle"] = tut

  return tut


def turtle_clonery(tut, color):
   newtut = tut.clone()
   newtut.color(color)
   newtut.seth(0)
   return newtut


def draw_graph(graph):

  #
  # 0. Set up the founding turtles
  #
  screen = Screen()
  root_nodes = graph[0]
  root_turtles = [ turtle_factory(root_nodes[i]) for i in range(len(root_nodes)) ]    

  for layer in graph[1:]:
    for node in layer:
      continue
      #node["turtle"] = turtle_clonery(base_turtles[node["base_layer"]])

  screen.mainloop()

if __name__ == "__main__":
  graph = read_file_graph()
  display_graph_data(graph)
  draw_graph(graph)



