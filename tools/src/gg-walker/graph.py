#!/usr/bin/env python3
#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------


import io
import os
import sys

class GenomeGraph:

  class Node:

    def __init__(self, name):
      self.name = name
      self.seq = None
      self.origin = None
      self.incoming = {}
      self.outgoing = {}

  def __init__(self):
    self.nodes = {}
    self.paths = []
    self.visited = {}

  def add_node(self, name, target=None):
    if name not in self.nodes:
      self.nodes[name] = self.Node(name)
    if target is not None:
      if target not in self.nodes:
        self.nodes[target] = self.Node(target)
      self.nodes[target].incoming[name] = 0
      self.nodes[name].outgoing[target] = 0

  def find_start_nodes(self):
    start_nodes = []
    for i in self.nodes:
      if not self.nodes[i].incoming:
        start_nodes.append(i)
    return start_nodes

  def show(self):
    print("Nodes\nNode\tLinks")
    for i in self.nodes:
      print("{}\t{}".format(i, ','.join(x for x in self.nodes[i].outgoing)))
    nodes = self.find_start_nodes()
    if nodes:
      for i in nodes:
        self.paths += self.resolve_paths(i)
      print("All graph paths:")
      for i in self.paths:
        print(' -> '.join(x for x in i))

  def resolve_paths(self, start, path=None):
    if not path:
      path = []
    path = path + [start]
    if not self.nodes[start].outgoing:
      return [path]
    paths = []
    visited = {}
    for i in self.nodes[start].outgoing:
      if i not in visited:
        visited[i] = 0
        for j in self.resolve_paths(i, path):
          paths.append(j)
    return paths
