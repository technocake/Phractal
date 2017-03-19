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
      "node_id": int(line[1]),
      "number_of_nodes": int(line[2]),
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
        current_base = -1

        layer = serialize_layer(line)
        tree.append(dict({
          "layer": layer, 
          "bases": [], 
        }))

      elif line.find("base:") > -1:
        current_base += 1

        base = serialize_base(line)
        tree[current_layer]["bases"].append(dict({
          "base" : base, 
          "nodes" : [],
        }))

      elif line.find("node:") > -1:
        node = serialize_node(line)
        tree[current_layer]["bases"][current_base]["nodes"].append(node)
        #print(node)

  return tree


def display_tree_data(tree):

  for layer in tree:
    print("\n", layer["layer"])
    for base in layer["bases"]:
      print(base["base"])
      for node in base["nodes"]:
        print(node)


def turtle_factory(color):
  tut = Turtle()
  tut.shape("circle")
  tut.shapesize(1)
  tut.color(color)
  return tut

def turtle_clonery(tut, color):
   newtut = tut.clone()
   newtut.color(color)
   return newtut


def turtle_dance(tree):
  screen = Screen()

    # Root turtle
  tut1= turtle_factory(tree[0]["bases"][0]["nodes"][0]["color"])

  tut1.left(int(tree[0]["bases"][0]["nodes"][0]["theta"]))
  tut1.forward(int(tree[0]["bases"][0]["nodes"][0]["radius"]))


    # 1 layer
  layer1_tuts = [turtle_clonery(tut1, tree[1]["bases"][0]["nodes"][i]["color"]) for i in range(tree[1]["bases"][0]["base"]["number_of_nodes"])]
  
  for i in range(9):
    pass

  screen.mainloop()


if __name__ == "__main__":
  tree = read_file_tree()
  display_tree_data(tree)
  turtle_dance(tree)

  

