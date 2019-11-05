  # Virus_Graphs

HIV inference based on NGS data.

## Ideas

* k-mer idea

## Outline, plan of action

hey

### Discussions today, 4th November 2019


## Identifying region of interest on genome graphs

Region of interest can be defined as loops, or "bubbles", within a genome path
since they indicate diverse regions among different sequences/genomes, ergo
potential points of interest. Facilitating the access to these loops of
interest would be a great plus.

Assuming the following graph (Graph 1), the loops between nodes 2 and 5 need to
be extracted and mapped to existing annotations.
```
               +-> (3) -> (4) --+
               |   |            |
               |   |            v
               |   + -> (8) -> (5) -> (6) -> (7)
(0) -> (1) -> (2)               ^
               |                |
               +----> (9)-------+

               Graph 1
```

Several tools exists to constructing virus graphs and most (all?) are based an
creating kmers. Unfortunately, corresponding metadata, e.g. kmer position, is
often missing (is this true?).

### Adding metadata to kmer data

[vg](https://github.com/vgteam/vg/)  offers adding metadata via
[RDF](https://github.com/vgteam/vg/tree/master/ontology) to its variant graphs.
However, a variant file (VCF) is currently [required](https://github.com/vgteam/vg/#variation-graph-construction).

A tool to annotate genome graphs with a variety of metadata is currently
missing. Overal appoach:

 0. Extract loops of interest
 1. find kmers within loops and map to annotation
 2. plot/extract/..

#### Extracting loops

Before  loops of interest can be anotated they need to be extracted. In graphs,
[articulation points](https://en.wikipedia.org/wiki/Biconnected_component), or
nodes, hint to regions where interesting things are happening.

Tried approaches:
  Running [$repo/tools/src/gg-walker/gg-walker.py](tools/src/gg-walker/gg-walker.py) will show tested approaches so far.

  Approaches were tested using Graph 1 (see above) to test if the loop between
  nodes 2 and 5 could be extracted.

  - [Tarjan's strongly connected components algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)

    - Methods
        - Own implementation [$repo/tools/gg-walker/src/scc.py](tools/gg-walker/src/scc.py) and [networkx.strongly_connected_components](https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.algorithms.components.strongly_connected.strongly_connected_components.html#networkx.algorithms.components.strongly_connected.strongly_connected_components)

    - Results
        - No cigar. There are no strong connected nodes which would

  - [networkx.biconnected_components](https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.algorithms.components.biconnected.biconnected_components.html#networkx.algorithms.components.biconnected.biconnected_components)

    - This reports the loop of interest. All components with more than two nodes
      can be considered a loop of interest.

  - [networkx.articulation_points](https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.algorithms.components.biconnected.articulation_points.html#networkx.algorithms.components.biconnected.articulation_points)

    - This reports nodes which break the graph when removed. These points can be
      checked for the number of incoming and outgoing edges to find nodes
      encompassing loops.

  - paths, aka CAS:

    - extracting all paths within a graph and identify nodes not present in all
      paths. `$repo/tools/src/gg-walker/gg-walker.py` implements a DFS for this
      task, but could get slow wityh bigger graphs.

#### Kmer indexing

WIP







