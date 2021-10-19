#!/bin/env python2.7

# Written by - Arif Mohammad Tanmoy
# This script was used to filter SNPs (in VCF file) by Phred-scaled quality score of Salmonella Paratyphi A genomes in DOI: (TO-DO).
# You can also activate few lines here to introduce filter by - Ratio of ALT alleles from high-quality reads.

from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='VCF Filtation.')
	commands.add_argument('--vcf', type=str, required=True,
						help='Mapped raw VCF file, with DP4 scores. (Required)')
	commands.add_argument('--phr', type=int, required=False, default=20,
						help='Minimum Phred-scaled quality score. Default 20.')
	#commands.add_argument('--ratio', type=float, required=False, default=0.1,
	#					help='Ratio of ALT alleles from high-quality reads. Default 0.1.')
	commands.add_argument('--output', type=str, required=False, default='Phred_Filtered.vcf',
						help='Output file.')
	return commands.parse_args()
args = parse_args()

phrdQ = float(args.phr)

with open(args.output, 'w') as output:
	for line in open(args.vcf, 'r'):
		if line.startswith("#") == True:
			output.write(line)
		else:
			element = line.split("\t")
			phrd = float(element[5])
			info = element[7]
			mapqual = float(info.split('MQ=')[1].split(';')[0])
			hqread = info.split('DP4=')[1].split(';')[0].split(',')
			read = float((int(hqread[2])+int(hqread[3]))/(int(hqread[0])+int(hqread[1])+int(hqread[2])+int(hqread[3])))
			readALTf = int(hqread[2])
			readALTr = int(hqread[3])
			FMT_read_dep = int(element[9].split(':')[2])
			# **Discard**: Following the values
			# 2nd: Ambiguous base (>1 base); Phred_quality =<20;
			if (len(element[4])==1) and (phrd > phrdQ):
				output.write(line)
			#if (len(element[4])==1) and (phrd > phrdQ) and (read > args.ratio):
			#	output.write(line)
			else:
				continue
output.close()

