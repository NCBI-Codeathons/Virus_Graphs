### Setup
library(tidyverse)
library(ggraph)
library(igraph)
library(rgexf)
#library(plotly)
#library(RColorBrewer)

### Saria's summary of SWIGG output
kmer_hits <- read.delim("../HIV_full_Refs_k23_1.tsv.fasta.reference_hits", header = FALSE, stringsAsFactors = FALSE)
colnames(kmer_hits) <- c("unknown", "acc_id", "kmer_seq")
kmer_anno <- kmer_hits %>%
  group_by(kmer_seq) %>%
  summarise(
    n_acc_ids = length(unique(acc_id)),
    the_acc_ids = paste(unique(acc_id), collapse = ";")
  )

### Load SWIGG output
swigg <- read.delim("../HIV_full_Refs_k23_1.tsv", header = FALSE, stringsAsFactors = FALSE)

### Edge annotation
edges <- swigg
edges$acc_ids <- paste(
  ifelse(
    kmer_anno$the_acc_ids[kmer_anno$kmer_seq == edges$V2]
    ),
  kmer_anno$the_acc_ids[kmer_anno$kmer_seq == edges$V3],
  collapse = ";"
)
edges_anno1a <- merge(
  edges, kmer_anno, by.x = "V2", by.y = "kmer_seq", all.x = TRUE
)$the_acc_ids
edges_anno1b <- merge(
  edges, kmer_anno, by.x = "V3", by.y = "kmer_seq", all.x = TRUE
)$the_acc_ids
edges$the_acc_ids <- paste(edges_anno1a, edges_anno1b, sep = ";")

edges_anno2a <- merge(edges, kmer_anno, by.x = "V2", by.y = "kmer_seq", all.x = TRUE)$n_acc_ids
edges_anno2b <- merge(edges, kmer_anno, by.x = "V3", by.y = "kmer_seq", all.x = TRUE)$n_acc_ids
edges$n_acc_ids <- edges_anno2a + edges_anno2b

### Node annotation
# use kmer_anno


### Load gfex
gfex <- "data/HIV_full_Refs_k23_1_Color_Annotated.gexf"
gr <- rgexf::gexf.to.igraph(rgexf::read.gexf(gfex))

### Add annotation

# Edges
E(gr)$n_acc_ids <- edges$n_acc_ids
E(gr)$the_acc_ids <- edges$the_acc_ids

# Nodes
kmer_anno <- kmer_anno[order(kmer_anno$kmer_seq, names(V(gr))), ]
V(gr)$n_acc_ids <- kmer_anno$n_acc_ids
V(gr)$the_acc_ids <- kmer_anno$the_acc_ids

### Parameters
layout <- "igraph"
algorithm <- "kk"
edge_color <- "the_acc_ids"
node_color <- "n_acc_ids"
node_shape <- 21
node_fill <- "the_acc_ids"
node_size <- "n_acc_ids"

### Plot
gr %>%
  ggraph(layout = layout, algorithm = algorithm) +
  geom_edge_density(aes(fill = n_acc_ids)) +
  geom_edge_link0(alpha = 0.5) +
  geom_node_point(aes(fill = n_acc_ids, alpha = n_acc_ids), shape = node_shape)
