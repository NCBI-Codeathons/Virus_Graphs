#!/usr/bin/perl -w
# Solgenomics@BTI
# Surya Saha Nov 2019
# Purpose: Find kmers in Fastq using jellyfish and then find the nodes with those kmers. Printing kmer in fastq, count in fastq, sample, genbank_accession, taxonomy_id

use strict;
use warnings;


unless (@ARGV == 3){
	print "USAGE: $0 <kmer size> <Fastq file> <SWIGG annotated TSV>\n";
	exit;
}

my $input_kmerlength = $ARGV[0];
my $input_fq         = $ARGV[1];
my $input_tsv        = $ARGV[2];

my $cmd = "/usr/bin/jellyfish.linux count --mer-len=$input_kmerlength --size=100M -t 4 -o ${input_fq}.jf input_fq";
system( $cmd );
$cmd = "/usr/bin/jellyfish.linux dump ${input_fq}.jf > ${input_fq}.jf.count.fasta";
system( $cmd );

open my $FQCOUNTFA, '<', "${input_fq}.jf.count.fasta" or die "Cannot open ${input_fq}.jf.count.fasta\n";
open my $TSV, '<', "$input_tsv" or die "Cannot open $input_tsv\n";
open my $OUT, '>', "${input_fq}.SWIGG.hits" or die "Cannot open ${input_fq}.SWIGG.hits\n";

my %fq_kmer_hash;

while ( my $line = <$FQCOUNTFA> ){									# get kmers and count from jellyfish dump
	if ( $line =~ /^>/ ){
		my $kmer = <$FQCOUNTFA>;
		$line    =~ s/^>//;
		$fq_kmer_hash{$kmer} = $line;
	}
}

my $header = <$TSV>;											# get header with annotations from TSV, scalable for additional attributes
my @header_arr = split ("\t", $header);

print $OUT "kmer in fastq, count in fastq";
for my $val (2..$#header_arr){
	print $OUT ",$val";
}
print $OUT "\n";

while ( my $line = <$TSV> ){									# parse SWIGG CSV data lines
	my @tsv_data_arr = split (/,/, $line);

	if ( exists $fq_kmer_hash{$tsv_data_arr[0]} ){				# printing kmer in fastq, count in fastq, sample, genbank_accession, taxonomy_id
		print $OUT "$tsv_data_arr[0],$fq_kmer_hash{$tsv_data_arr[0]},$tsv_data_arr[2],$tsv_data_arr[3],$tsv_data_arr[4],$tsv_data_arr[5]\n";
	}
	elsif ( exists $fq_kmer_hash{$tsv_data_arr[1]} ){
		print $OUT "$tsv_data_arr[0],$fq_kmer_hash{$tsv_data_arr[0]},$tsv_data_arr[2],$tsv_data_arr[3],$tsv_data_arr[4],$tsv_data_arr[5]\n";
	}
}