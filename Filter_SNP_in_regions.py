#!/bin/env python2.7

# Written by - Arif Mohammad Tanmoy
# This script was used to filter SNPs by their genomic location (in phage, repeat_region and recombinant regions) and exclude them (from VCF file) of Salmonella Paratyphi A genomes in DOI: (TO-DO).
# A file needs to be provided with spcified regions. Do not keep any empty lines. 
# Start and end of all positions needs to be separated by TAB. Example - (ignore #)
#6083	6085
#16120	16465

from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='Filter VCF to exclude SNPs in specified regions.')
	commands.add_argument('--vcf', type=str, required=True,
						help='VCF file. (Required)')
	commands.add_argument('--position', type=str, required=True,
						help='Starts and Ends of specified regions. (Required)')
	commands.add_argument('--output', type=str, required=False, default='Region_filtered.vcf',
						help='Output file.')
	return commands.parse_args()
args = parse_args()
output = open(args.output, 'w')

def diff(a,b):
	uniq = [i for i in a if i not in b]
	return uniq

data, start, end, exclude = [], [], [], []
for line in open(args.position, 'r'):
	rec = line.split('\t')
	start.append(str(rec[0]))
	end.append(str(rec[1]))

for record in open(args.vcf, 'r'):
	line = record.rstrip()
	if line.startswith("#") == True:
		vcfhead = line
		output.write(vcfhead+'\n')
	else:
		data.append(line)
		position = line.split("\t")[1]
		for i in range(0, len(start)):
			if (int(start[i]) <= int(position) <= int(end[i])) != False:
				exclude.append(line)
exclude = list(dict.fromkeys(exclude))
include = diff(data,exclude)
output.write('\n'.join(include))
output.close()

