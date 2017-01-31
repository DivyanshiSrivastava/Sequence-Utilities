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
	print np.asarray(space)[subset].shape
	print np.asarray(space)[subset]
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
	#print wkmers
	#print wkmers.shape
	return wkmers

""" creating a dictionatry(that should implement a hash table, to allow O(n) time/(constant?) comparisons.) """
def createhash(kmeruniverse):
	kmerhash = dict()
	for kmer in kmeruniverse:
		kmerhash[tuple(kmer)] = 0
	return kmerhash

def map_to_hash(kmer_dict, seq):
	kmerset = get_kmers(seq)
	#print kmerset
	space = kmer_dict.copy()
	for kmer in kmerset:
		space[tuple(kmer)] += 1
		space[reverse_complement(tuple(kmer))] += 1
	return space


""" get the reverse complement for a DNA sequence """

def reverse_complement(seq):
    letters = []
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N' : 'N'} 
    seq_complement = tuple([complement[base] for base in seq])
    return seq_complement[::-1]

# reading data from fasta extracted sequences:
boundsites = np.genfromtxt("/Users/divyanshisrivastava/Desktop/Projects/data/seq.txt", dtype = str)
# create the global mappable space.  
kmer_dict = createhash(all_kmers())

# map features to this space. 
feature_martix = []
idx = 1
for sequence in boundsites:
	# getting the seq features.
	print "I am at idx %s" % idx
	idx += 1
	seq_features = map_to_hash(kmer_dict, sequence)
	feature_vector = []
	# extracting from dict to list. 
	for key, val in seq_features.iteritems():
		#print val
		feature_vector.append(val)
	feature_martix.append(feature_vector)

feature_martix = np.asarray(feature_martix)
feature_martix = feature_martix[:,np.sum(feature_martix, axis=0) > 1000]
print feature_martix.shape
print feature_martix
np.savetxt("features.txt", feature_martix, fmt='%d', delimiter=',')