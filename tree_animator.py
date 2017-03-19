#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# @author  Jonas Solsvik
# @email   jonasjso@stud.ntnu.no
# @created 18.03.17
# @file    tree_animator.py
# @brief   Takes filformat.tree kind of files as input, and draws an
#           a growing tree structure, layer by layer.
# 


from turtle import Turtle, Screen


def serialize_line(line):
  line = line.split(":")[1]      \
              .replace(" ", "")  \
               .replace("\n", "") \
                .split(",")
  return line


def serialize_layer(line):
  line = serialize_line(line)
  return dict({
      "layer_id": int(line[0]),
      "number_of_bases": int(line[1]),
  })


def serialize_base(line):
  line = serialize_line(line)
  return dict({
      "base_id": int(line[0]),
      "number_of_nodes": int(line[1]),
  })


def serialize_node(line):
  line = serialize_line(line)
  return dict({ 
      "color":  line[1],  
      "theta":  int(line[2]),
      "radius": int(line[3]),   
  })


def read_file_tree():
  tree=[]

  with open("file/fileformat.tree", "r") as treefile:

    current_layer = -1

    for line in treefile.readlines():
        
      if line.find("layer:") > -1:
        current_layer += 1

        layer = serialize_layer(line)
        tree.append(dict({
          "layer": layer, 
          "nodes": [], 
        }))

      elif line.find("base:") > -1:
        base = serialize_base(line)
        tree[current_layer]["nodes"].append(base)

      elif line.find("node:") > -1:
        node = serialize_node(line)
        tree[current_layer]["nodes"].append(node)

  return tree


def display_tree_data(tree):

  for layer in tree:
    print("\n", layer["layer"])
    for node in layer["nodes"]:
      print(node)


def turtle_factory(color):
  tut = Turtle()
  tut.shape("circle")
  tut.shapesize(.5)
  tut.color(color)
  tut.speed(0)
  return tut

def turtle_clonery(tut, color):
   newtut = tut.clone()
   newtut.color(color)
   newtut.seth(0)
   return newtut



def turtles_dance(tree):

  screen = Screen()

  #
  # 0. step - Create root turtle
  #
  tutroot = turtle_factory(tree[0]["nodes"][1]["color"])
  tutroot.left(tree[0]["nodes"][1]["theta"])
  tutroot.penup()
  tutroot.forward(tree[0]["nodes"][1]["radius"])
  tutroot.pendown()

  #
  # 0.5 step - Root turtle is now the base "layer" for layer 1 of turtles
  #
  base_turtle = [tutroot]

  for layer in tree[1:]:
    #
    # 1. step - clone new turtles
    #
    cloned_turtle = []
    base_num = -1
    nodes = layer["nodes"]

    for node in nodes:
      if "base_id" in node:
        base_num += 1
        print("Base_num:", base_num)
        pass
      else:
        cloned_turtle.append( turtle_clonery( base_turtle[base_num], node["color"]))


    #
    # 2. Step - Make all turtles face the right direction
    #
    i=0
    radius = []

    for node in nodes:
      if "base_id" in node:
        continue
      else:
        radius.append(int(node["radius"]))
        cloned_turtle[i].left(node["theta"])
        i+=1

    #
    # 3. Step by step run cloned turtles forward untill they hit
    #     their max radius from the base.
    #
    clone_count = len(radius)
    forward_count = [ 0 for i in range(clone_count) ]
    opened = False

    while not opened:
      opened = True

      for i in range(clone_count):
        if forward_count[i] <= radius[i]:
          forward_count[i] += 1

          cloned_turtle[i].forward(1)
          opened = False

    #
    # 4. Cloned turtles are now the base layer for the next
    #     layer of turtles
    #
    base_turtle = cloned_turtle 

  screen.mainloop()


if __name__ == "__main__":
  tree = read_file_tree()
  display_tree_data(tree)
  turtles_dance(tree)

