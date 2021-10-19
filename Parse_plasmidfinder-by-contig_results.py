#!/bin/env python2.7

# This script was used to parse raw plasmidfinder results of Salmonella Paratyphi A genomes (one genome at a time) in DOI: (TO-DO).

from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='Parse raw plasmidfinder results.')
	commands.add_argument('--plas', type=str, required=True,
						help='Raw plasmidfinder output file. (Required)')
	commands.add_argument('--output', type=str, required=False, default='Parsed.plasmidfinder',
						help='Output file.')
	return commands.parse_args()
args = parse_args()

outfile = open(args.output, 'w')

cov, iden, contig, plasmid = [], [], [], []
ID = str(args.plas).split('/')[-1]

for line in open(args.plas, 'r'):
	rec = line.rstrip()
	if "'contig_name':" in rec:
		contig.append(rec.split(':')[1].replace(",",""))
	if "'coverage':" in rec:
		cov.append(rec.split(':')[1].replace(",",""))
	if "'identity':" in rec:
		iden.append(rec.split(':')[1].replace(",",""))
	if "'plasmid':" in rec:
		plasmid.append(rec.split(':')[1].replace('"','').replace(",",""))

for i in range(0, len(plasmid)):
	outfile.write(ID+'\t'+str(plasmid[i])+'\t'+str(contig[i])+'\t'+str(cov[i])+'\t'+str(iden[i])+'\n')
	#print results
