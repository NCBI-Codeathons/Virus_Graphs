#!/usr/bin/env python3
#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------


import io
import os
import sys

import graph

class GenomeGraphWalker:

  def __init__(self):
    self.graph = graph.GenomeGraph()

  def show_graph(self):
    self.graph.show()

def main():
  gw = GenomeGraphWalker()
  gw.graph.add_node('n0', 'n1')
  gw.graph.add_node('n1', 'n2')
  gw.graph.add_node('n2', 'n3')
  gw.graph.add_node('n2', 'n9')
  gw.graph.add_node('n3', 'n4')
  gw.graph.add_node('n3', 'n8')
  gw.graph.add_node('n4', 'n5')
  gw.graph.add_node('n5', 'n6')
  gw.graph.add_node('n6', 'n7')
  gw.graph.add_node('n8', 'n5')
  gw.graph.add_node('n9', 'n5')
  gw.show_graph()
  return 0

if __name__ == '__main__':
  main()
