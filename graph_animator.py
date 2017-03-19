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


if __name__ == "__main__":
  graph = read_file_graph()
  display_graph_data(graph)



