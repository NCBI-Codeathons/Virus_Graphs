#!/usr/bin/env python3

import argparse

import numpy as np
import pandas as pd

from collections import Counter
from Bio import SeqIO
import networkx as nx

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')

required.add_argument("-k", "--kmer-length", type=int,
                    help="""required, the length of k-mer that needs to be used'
                    """,
                    required=True)


required.add_argument("-f", "--fasta", nargs="+",
                    help="required, set of all fasta sequences",
                    required=True)

required.add_argument("-l", "--klist",help="""required, the list of k-mers that were used for SWIGG graph'
                    """,
                    required=True)

args = parser.parse_args()
print(args)

########################################################

seq_list = []
for seqq in args.fasta:
    seq_list = seq_list + [(seqq, str(list(SeqIO.parse(seqq, "fasta"))[0].seq))]
seq_df = pd.DataFrame(seq_list).head()
seq_df.columns=['name', 'Sequence']

k_length = int(args.kmer_length)

# Read in tables and format to dataframe.
print("Finding all possible kmers...", flush=True)
kmers = [(i_strain, seq[i_base:(i_base+k_length)], i_base) for i_strain,seq in enumerate(seq_df.Sequence.values) for i_base in range(len(seq)-k_length)]
kmers_df = pd.DataFrame(kmers, columns = ['alt_seq', 'kmer',  'pos_start'])
print(str(len(kmers)) + " total possible k-mers of length " + str(k_length), flush=True)
kmer_list = (args.klist )
kmer_list_df = pd.read_table(args.klist, header=False)
print(kmer_list_df)

# Need to compare kmers in list of kmers to kmers derived from fasta
å
