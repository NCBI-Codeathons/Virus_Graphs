#!/usr/bin/env python3
#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------


import io
import os
import sys

import networkx
import matplotlib.pyplot

import graph
import scc

class GenomeGraphWalker:

  def __init__(self):
    self.graph = graph.GenomeGraph()

  def show_graph(self):
    self.graph.show()

  def find_articulation_points(self):
    startnodes = self.graph.find_start_nodes()
    for i in startnodes:
      self.graph.find_articulation_nodes(self.graph.nodes[i])

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

  #print("\nArticulation points jpb (not checking root/leaf and a bug somewhere)")
  #gw.find_articulation_points(ap)

  graph = networkx.Graph()
  graph.add_edge('n0', 'n1')
  graph.add_edge('n1', 'n2')
  graph.add_edge('n2', 'n3')
  graph.add_edge('n2', 'n9')
  graph.add_edge('n3', 'n4')
  graph.add_edge('n3', 'n8')
  graph.add_edge('n4', 'n5')
  graph.add_edge('n5', 'n6')
  graph.add_edge('n6', 'n7')
  graph.add_edge('n8', 'n5')
  graph.add_edge('n9', 'n5')

  nxap = networkx.articulation_points(graph)
  print("\nArticulation points networkx")
  for i in nxap:
    print("\tnxap", i)

  gw = scc.TarjanSCC()
  gw.add_node('n0', 'n1')
  gw.add_node('n1', 'n2')
  gw.add_node('n2', 'n3')
  gw.add_node('n2', 'n9')
  gw.add_node('n3', 'n4')
  gw.add_node('n3', 'n8')
  gw.add_node('n4', 'n5')
  gw.add_node('n5', 'n6')
  gw.add_node('n6', 'n7')
  gw.add_node('n8', 'n5')
  gw.add_node('n9', 'n5')
  gw.run()
  print("\nscc jpb")
  for i in gw.sccs:
    for j in i:
      print("\tscc\t", j.name)

  digraph = networkx.DiGraph()
  digraph.add_edge('n0', 'n1')
  digraph.add_edge('n1', 'n2')
  digraph.add_edge('n2', 'n3')
  digraph.add_edge('n2', 'n9')
  digraph.add_edge('n3', 'n4')
  digraph.add_edge('n3', 'n8')
  digraph.add_edge('n4', 'n5')
  digraph.add_edge('n5', 'n6')
  digraph.add_edge('n6', 'n7')
  digraph.add_edge('n8', 'n5')
  digraph.add_edge('n9', 'n5')

  print("\nscc networkx")
  nxscc = networkx.strongly_connected_components(digraph)
  for i in nxscc:
    print("\tscc\t", i)


  # does not exist: nxbc = networkx.biconnected_component_subgraphs(graph)
  nxbc = networkx.biconnected_components(graph)
  print("\nbiconnected components networkx")
  for i in nxbc:
    print("\tcomponents\t", i)


  networkx.draw(graph)
  matplotlib.pyplot.savefig("path.png")

  return 0

if __name__ == '__main__':
  main()
