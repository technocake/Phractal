#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# @author  Jonas Solsvik
# @email   jonasjso@stud.ntnu.no
# @created 18.03.17
# @file    file_parser.py
# @brief   Collection of functions regarding the parsing
#           of lines from a file
#          Supported formats:
#             *.tree
#             *.graph


def line_to_list(line):
  line = line.split(":")[1]      \
              .replace(" ", "")  \
               .replace("\n", "") \
                .split(",")
  return line