from __future__ import division
import sys, os
import itertools
import numpy as np
from collections import defaultdict

""" getting a set of all possible wildcard kmers with at most 2 contigous N's """

def prune(seq):
	if seq.count('N') > 2:
		return False
	if any(i==j=='N' for i,j in zip(seq, seq[1:])):
		return True
	else:
		return False

def all_kmers():
	# get a set of all possible strings from this alphabet.
	space = list(set(itertools.product(('A','T','G','C','N','N'), repeat = 8)))
	subset = np.array([prune(space[i]) for i in range(0,len(space))])
	return np.asarray(space)[subset]

""" getting sequence specific kmers """

def add_wildcards(kmer):
	#  adding wildcards to kmers.	
	wildcard = []
	for i in range(0,len(kmer)-1):
		hold = kmer.copy()
		hold[i] = 'N'
		hold[i + 1] = 'N'	
		wildcard.append(list(hold))
	return np.array(wildcard)

def get_kmers(seq):
	# 6 & 5 hardcoded for 6 mers. Remove that if making it not rough.
	# the array and list is to get it in the same format as the unversal set. 
	kmers = np.asarray([list(seq[i:i+8]) for i in range(0,len(seq)-7)])
	wkmers = np.empty((0,8), str)
	for kmer in kmers:
		wkmers = np.vstack((wkmers,add_wildcards(kmer)))
	print wkmers
	print wkmers.shape
	return wkmers

""" creating a dictionatry(that should implement a hash table, to allow O(n) time/(constant?) comparisons.) """

def createhash(kmeruniverse):
	kmerhash = dict()
	for kmer in kmeruniverse:
		kmerhash[str(kmer)] = 0
	return kmerhash


def map_to_hash(bound):
	kmer_dict = createhash(all_kmers())
	# bound is a list of sequences
	for seq in bound:
		kmerset = get_kmers(seq)
		for kmer in kmerset:
			kmer_dict[str(kmer)] += 1
	return kmer_dict