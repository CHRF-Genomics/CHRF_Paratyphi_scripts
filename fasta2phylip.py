#!/usr/bin/env python
#import os
#import sys
import argparse
from Bio import AlignIO

#name = os.path.basename(sys.argv[0]) #get scriptname from actual script filename that was called
parser=argparse.ArgumentParser(description="Converts Fasta alignments to phylip format (in strict and interleaved format; relaxed-interleaved if '-r' is set).\
 Allignment cannot contain any Dot (.). Please replace with dash (-) before runnig this script.")
parser.add_argument('-i','--input', action = "store", dest = "input", required = True, help = "Fasta allignment filename")
parser.add_argument('-o','--output', action = "store", dest = "output", help = "Output phylip filename")
parser.add_argument('-r','--relaxed', action = "store_true", dest = "relaxed", default = False, help = "Output phylip file in relaxed phylip format. \
Default output is strict phylip")

args=parser.parse_args()

if not args.output:
	args.output = args.input + ".phylip" # if no phylip file name is mentioned.

def main():
	fastafile = open(args.input, "r")
	phylipfile = open(args.output, "w")
	alignments = AlignIO.parse(fastafile, "fasta")
	if args.relaxed:
		AlignIO.write(alignments, phylipfile, "phylip-relaxed")
	else:
		AlignIO.write(alignments, phylipfile, "phylip")
	fastafile.close()
	phylipfile.close()
	sys.stderr.write("\nfinished\n")

main()
