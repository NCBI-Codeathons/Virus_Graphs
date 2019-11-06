#!/usr/bin/env python3
#-------------------------------------------------------------------------------
#\file swigg-metadata-merger.py
#\author Jan Piotr Buchmann <jpb@members.fsf.org>
#\copyright 2019
#\description
# Merge a SWIGG graph tsv file with metadata for individual kmer nodes to create
# an annotated graph.
# The  individual methods need properly implemented
#-------------------------------------------------------------------------------


import io
import os
import sys

import networkx

class MetadatMerger:
  """
  Parse SWIGG tsv file and create a new graph with metadata for the
  corresponding nodes. The method add_node accepts attributes as key value pairs:
  https://networkx.github.io/documentation/stable/reference/classes/generated/networkx.DiGraph.add_node.html?highlight=add_node
  """
  def __init__(self):
    pass

  def merge(self, fname, metadata):
    g = networkx.DiGraph()
    fh = open(fname, 'r')
    for i in fh:
      g.add_edge(v, w)
      v, w = i.split()[1:2]
      if v in metadata:
        g.add_node(v, add_meta)
      if w in metadata:
        g.add_node(w, add_meta)
    fh.close()
  networks.write_gexf(g, fname+'.merged.gexf')
  networks.drawing.nx_pydot.write_dot(g, fname+'.merged.dot')

class MetadataParser:
  """
  Parse metadata form file.

  :return dict: metadata
  """
  def __init__(self):
    pass

  def parse(self, fname):
    metadata = {}
    fh = open(fname, 'r')
    for i in fh:
      metadata[kmerseq] = {'metadatakey':'value'}
    fh.close()
    return metadata

def main():
  mp = MetadataParser()
  #metadata file
  metadata = mp.parse(sys.argv[1])
  mm = MetadatMerger()
  #tsv file
  mm.merge(sys.argv[2], metadata)
  return 0

if __name__ == '__main__':
  main()
