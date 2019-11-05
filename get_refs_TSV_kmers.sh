#!/bin/sh

# Surya Saha
# Solgenomics@BTI
# Purpose:
# Requirements: bowtie in installed

usage(){
	echo "usage:
	$0 <TSV file> <Reference fasta>"
	exit 1
}

if [ "$#" -ne 2 ]
then
	usage
fi

printf "SWIGG TSV : %s \\n" "$1"
printf "Reference fasta : %s \\n" "$2"


awk -v OFS='' -F"\\t" '{print ">",$1,"a\n",$2,"\n>",$1,"b\n",$3}' "$1" > "${1}.fasta"

bowtie-build -f "$2" "$2"

# report best hit for each ref seq the kmer is found in
bowtie "$2" --all --best -n 0 -f "${1}.fasta"| cut -f 1,3,5 > "${1}.fasta.reference_hits"
