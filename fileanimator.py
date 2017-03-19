#!/usr/bin/env python
# -*- coding: utf-8 -*-


with open("file/filformat_alpha.tree", "r") as treefile:

  for line in treefile.readlines():
    
    if line.find("node: 0") > -1:
      print(line)

    elif line.find("node:"):
      pass
