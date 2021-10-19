#!/bin/env python2.7

# This script was used to parse concatenated parsed-resfinder or parsed-plasmidfinder results of Salmonella Paratyphi A genomes (one genome at a time) in DOI: (TO-DO).
# Use: python Rearrange_parsed-finder_results.py all_samples_merged_parsed.resfinder > all_samples_merged_parsed.resfinder.parsed
# Use: python Rearrange_parsed-finder_results.py all_samples_merged_parsed.plasmidfinder > all_samples_merged_parsed.plasmidfinder.parsed

import sys

name, gene, group = [], [], []

for line in open(sys.argv[1],'r'):
	rec = line.split('\t')
	name.append(rec[0])
	gene.append(rec[1])
	group.append(rec[2])
	
nameuniq = sorted(list(set(name)))
#print len(nameuniq)

for i in range(0, len(nameuniq)):
	n = [j for j, x in enumerate(name) if x == str(nameuniq[i])]
	if len(n)==1:
		l = name.index(str(nameuniq[i]))
		print str(nameuniq[i])+'\t'+str(gene[l])+'\t'+str(group[l])
	if len(n) >1:
		egene = []
		egroup = []
		for x in range(0, len(n)):
			egene.append(gene[n[x]].replace("'",""))
			egroup.append(group[n[x]])
		gene_all = ','.join(egene)
		group_all = ','.join(egroup)
		print str(nameuniq[i])+'\t'+gene_all+'\t'+group_all
			
