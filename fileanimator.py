#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

  with open("file/filformat_alpha.tree", "r") as treefile:

    current_layer = -1

    for line in treefile.readlines():
        
      # Special case for finding the root node
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
        #print(node)

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
  tut.speed(9)
  return tut

def turtle_clonery(tut, color):
   newtut = tut.clone()
   newtut.color(color)
   newtut.seth(0)
   return newtut


def turtles_spread(turtles, nodes):
  opened = False
  radis = []

  # 2. Step - turn alll branches facing the right direction
  i=0
  for node in nodes:
    if "base_id" in node:
      continue
    else:
      radis.append([0, int(node["radius"])])
      turtles[i].left(node["theta"])
      i+=1

  # 3. step run nodes forward
  while not opened:
    opened = True

    i = 0
    for rad in radis:
      if rad[0] <= rad[1]:
        rad[0] += 1
        turtles[i].forward(1)
        opened = False

      i += 1



def turtle_dance(tree):
  screen = Screen()

    # Root turtle
  tutroot=turtle_factory(tree[0]["nodes"][1]["color"])

  tutroot.left(tree[0]["nodes"][1]["theta"])
  tutroot.penup()
  tutroot.forward(tree[0]["nodes"][1]["radius"])
  tutroot.pendown()

  bot_layer = [tutroot]
  top_layer = []

  for layer in tree[1:]:
    # 1. step - create new nodes
    base_num = -1
    nodes = layer["nodes"]
    for node in nodes:
      if "base_id" in node:
        base_num += 1
        print("Base_num:", base_num)
        pass
      else:
        top_layer.append(turtle_clonery(bot_layer[base_num], node["color"]))

    turtles_spread(top_layer, nodes)

    # Swap layers
    bot_layer = top_layer
    top_layer = []

  screen.mainloop()


if __name__ == "__main__":
  tree = read_file_tree()
  display_tree_data(tree)
  turtle_dance(tree)

  

