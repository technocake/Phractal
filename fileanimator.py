#!/usr/bin/env python
# -*- coding: utf-8 -*-



def serialize_line(line):
  line = line.split(":")[1]      \
              .replace(" ", "")  \
               .replace("\n", "") \
                .split(",")
  return line


def serialize_layer(line):
  line = serialize_line(line)
  return dict({
      "layer_id": line[0],
      "number_of_bases": line[1],
  })


def serialize_base(line):
  line = serialize_line(line)
  return dict({
      "base_id": line[0],
      "number_of_nodes": line[1],
  })


def serialize_node(line):
  line = serialize_line(line)
  return dict({ 
      "color":  line[1],  
      "theta":  line[2],
      "radius": line[3],   
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


if __name__ == "__main__":
  tree = read_file_tree()
  display_tree_data(tree)

