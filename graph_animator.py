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
scale = 0.5

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

  return tut


def turtle_clonery(tut, node):

  tut_clone = tut.clone()
  tut_clone.shapesize(node["size"]*scale)
  tut_clone.color(node["color"])
  tut_clone.setheading(node["theta"])

  return tut_clone


def draw_graph(graph):

  #
  # 0. Set up the founding turtles
  #
  screen = Screen()
  root_nodes = graph[0]
  root_turtles = [ turtle_factory(root_nodes[i]) for i in range(len(root_nodes)) ]    

  all_turtles = ["GOD-node"]
  all_turtles.append(root_turtles)

  #
  # 1. Spawn new layers of turtles on top of the original one
  #

  for layer in graph[1:]:
    cloned_turtles = []
    for node in layer:

      if node["base_layer"] == 0 and node["base_node"] == 0:  # Pointing to the god node
        cloned_turtles.append(turtle_factory(node))

      elif node["base_layer"] == 0 and node["base_node"] != 0:
          print("This should never happen... There is only one GOD-node!!!")
          exit(0)

      else:
        bl = node["base_layer"]
        bn = node["base_node"]
        cloned_turtles.append(turtle_clonery(all_turtles[bl][bn], node))

    all_turtles.append(cloned_turtles)

    #
    # 2. Step by step run cloned turtles forward untill they hit
    #     their max radius from the base.
    #
    clone_count = len(cloned_turtles)
    forward_count = [ 0 for i in range(clone_count) ]
    opened = False

    while not opened:
      opened = True

      for i in range(clone_count):

        if layer[i]["base_layer"] == 0 and layer[i]["base_node"] == 0:
          pass
        elif forward_count[i] <= layer[i]["radius"]:
          forward_count[i] += 1

          cloned_turtles[i].forward(1)
          opened = False

  screen.mainloop()

if __name__ == "__main__":
  graph = read_file_graph()
  display_graph_data(graph)
  draw_graph(graph)



