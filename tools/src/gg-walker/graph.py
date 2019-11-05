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
      self.visited = False
      self.num = 0
      self.parent = None
      self.low = 0
      self.incoming = {}
      self.outgoing = {}

    def num_out_edges(self):
      return len(self.outgoing)

    def num_in_edges(self):
      return len(self.incoming)

  def __init__(self):
    self.nodes = {}
    self.paths = []
    self.visited = {}
    self.node_counter = 0

  def add_node(self, name, target=None):
    if name not in self.nodes:
      self.nodes[name] = self.Node(name)
    if target is not None:
      if target not in self.nodes:
        self.nodes[target] = self.Node(target)
      self.nodes[target].incoming[name] = 0
      self.nodes[name].outgoing[target] = 0

  def nodelist(self):
    return [self.nodes[x] for x in self.nodes]

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
      print("All graph paths:")
      for i in nodes:
        for j in self.resolve_path(i):
          print(' -> '.join(x for x in j))

  def resolve_path(self, start, path=None): # DFS search
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
        for j in self.resolve_path(i, path):
          paths.append(j)
    return paths

  def find_paths(self):
    startnodes = self.find_start_nodes()
    if startnodes:
      for i in startnodes:
        self.paths += self.resolve_path(i)

  def find_articulation_nodes(self, node):
    node.visited = True
    node.low = self.node_counter
    node.num = self.node_counter
    self.node_counter += 1
    for i in node.outgoing:
      if not self.nodes[i].visited: # fwd edge from start
        self.nodes[i].parent = node.name
        self.find_articulation_nodes(self.nodes[i])
        if self.nodes[i].low >= node.num:
          print("articulation point", node.name)
        node.low = min(self.nodes[i].low, node.low)
      else:
        if node.parent != self.nodes[i].name:
          node.low = min(node.low, self.nodes[i].num)
