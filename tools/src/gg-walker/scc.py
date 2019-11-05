#!/usr/bin/env python3
#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
# http://www.logarithmic.net/pfh/blog/01208083168
# https://github.com/alviano/python/blob/master/fasp/scc.py
# https://gist.github.com/JonasGroeger/5459190
#  -------------------------------------------------------------------------------


import io
import os
import sys


class TarjanSCC:

  class Node:

    def __init__(self, name):
      self.name = name
      self.idx = None
      self.num = 0
      self.parent = None
      self.visited = False
      self.lowlink = 0
      self.incoming = {}
      self.outgoing = {}

  def __init__(self):
    self.visited = {}
    self.stack = []
    self.idx = 0
    self.lowlink = {}
    self.sccs = []
    self.nodes = {}

  def add_node(self, name, target=None):
    if name not in self.nodes:
      self.nodes[name] = self.Node(name)
    if target is not None:
      if target not in self.nodes:
        self.nodes[target] = self.Node(target)
      self.nodes[target].incoming[name] = 0
      self.nodes[name].outgoing[target] = 0

  def run(self):
    for i in self.nodes:
      if not self.nodes[i].idx:
        self.strongconnect(self.nodes[i])

  def strongconnect(self, node):
    node.idx = self.idx
    node.lowlink = self.idx
    node.visited = True
    self.idx += 1
    self.stack.append(node)

    for i in node.outgoing:
      if not self.nodes[i].idx:
        self.strongconnect(self.nodes[i])
        node.lowlink = min(node.lowlink, self.nodes[i].lowlink)
      else:
        if self.nodes[i].visited:
          node.lowlink = min(node.lowlink, self.nodes[i].idx)

    if node.lowlink == node.idx:
      scc = []
      while True:
        suc = self.stack.pop()
        suc.visited = False
        scc.append(suc)
        if suc.name == node.name:
          break
      self.sccs.append(scc)
