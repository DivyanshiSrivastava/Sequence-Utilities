from __future__ import division
import sys, os
import itertools
import numpy as np

def get_kmers(seq):
	return [seq[i:i+4] for i in range(0,len(seq))]

def all_kmers():
	# get a set of all possible strings from this alphabet.
	space = itertools.product(('A','T','G','C','N','N'), repeat = 6)
	return list(set(space))

def prune(seq):
	if seq.count('N') > 2:
		return False
	if any(i==j=='N' for i,j in zip(seq, seq[1:])):
		return True
	else:
		return False

allkmers = all_kmers()
subset = np.array([prune(allkmers[i]) for i in range(0,len(allkmers))])
filtered_kmers = np.asarray(allkmers)[subset]
