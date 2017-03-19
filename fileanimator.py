#!/usr/bin/env python
# -*- coding: utf-8 -*-

tree=[]

def serialize_line(line):
  line = line.split(":")[1]      \
              .replace(" ", "")  \
               .replace("\n", "") \
                .split(",")
  return line

def serialize_node(line):
  line = serialize_line(line)
  return dict({ 
      "color":  line[1],  
      "theta":  line[2],
      "radius": line[3],   
  })

def serialize_base(line):
  line = serialize_line(line)
  return dict({
      "base_id": line[0],
      "number_of_nodes": line[1],
  })

def read_file_tree():
  with open("file/filformat_alpha.tree", "r") as treefile:

    current_layer = -1

    for line in treefile.readlines():
        
      # Special case for finding the root node
      if line.find("layer:") > -1:
        tree.append([])
        current_layer += 1

      elif line.find("base:") > -1:
        base = serialize_base(line)
        tree[current_layer].append(base)

      elif line.find("node:") > -1:
        node = serialize_node(line)
        tree[current_layer].append(node)
        #print(node)

def display_tree_data():
  layer_count=1
  for layer in tree:
    counter = 0
    print("\nLayer:", layer_count)
    layer_count += 1

    while counter < len(layer):
      number_of_nodes = layer[counter]['number_of_nodes']

      print("\n", layer[counter])
      counter += 1

      for j in range(int(number_of_nodes)):

        print(layer[counter])
        counter += 1


if __name__ == "__main__":
  read_file_tree()
  display_tree_data()

