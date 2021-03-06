#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# @author  Jonas Solsvik
# @email   jonasjso@stud.ntnu.no
# @created 19.03.17
# @file    file_parser.py
# @brief   Collection of functions regarding the parsing
#           of lines from a file
#          Supported formats:
#             *.tree
#             *.graph

filepath = "file/fileformat.graph" # File to load the graph from

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


#
# @function that serializes lines that looks like the one below
#           into dictionaries.
#      @example "node: 0, 0, 0, 0, 100, 1, orange"
#               <tag><id><base_layer><base_node><theta><radius><size><color>
#
def serialize_graph_node(line):
  list_of_values = serialize_line(line)
  return dict({
    "id"         : int(list_of_values[0]),
    "base_layer" : int(list_of_values[1]),
    "base_node"  : int(list_of_values[2]),
    "theta"      : int(list_of_values[3]),
    "radius"     : int(list_of_values[4]),
    "size"       : int(list_of_values[5]),
    "color"      :     list_of_values[6],
  })

#
# @function reads a file with the formate "fileformat.graph"
#            Puts the values in a datastructure which is a list of layers
#            containing a list of nodes. Each node is stored as a dictionary.
#           [[dict,dict,dict],
#            [dict,dict,dict],[dict,dict], ...]
#
def read_file_graph():
  graph=[]

  with open(filepath, "r") as graphfile:

    current_layer = -1

    for line in graphfile.readlines():
        
      if line.find("layer:") > -1:
        current_layer += 1
        graph.append([])

      elif line.find("node:") > -1:
        node = serialize_graph_node(line)
        graph[current_layer].append(node)

  return graph