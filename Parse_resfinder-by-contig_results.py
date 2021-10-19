#!/bin/env python2.7

# This script was used to parse raw resfinder results of Salmonella Paratyphi A genomes (one genome at a time) in DOI: (TO-DO).

from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='Parse raw resfinder results.')
	commands.add_argument('--res', type=str, required=True,
						help='Raw resfinder output file. (Required)')
	commands.add_argument('--output', type=str, required=False, default='Parsed.resfinder',
						help='Output file.')
	return commands.parse_args()
args = parse_args()

outfile = open(args.output, 'w')

cov, iden, pheno, gene = [], [], [], []
ID = str(args.res).split('/')[-1]

for line in open(args.res, 'r'):
	rec = line.rstrip()
	if "'coverage':" in rec:
		cov.append(rec.split(':')[1].replace(",",""))
	if "'identity':" in rec:
		iden.append(rec.split(':')[1].replace(",",""))
	if "'predicted_phenotype':" in rec:
		pheno.append(rec.split(':')[1].replace("'",""))
	if "'resistance_gene':" in rec:
		gene.append(rec.split(':')[1].replace('"','').replace(",",""))

for i in range(0, len(gene)):
	outfile.write(ID+'\t'+str(gene[i])+'\t'+str(pheno[i])+'\t'+str(cov[i])+'\t'+str(iden[i])+'\n')
    
