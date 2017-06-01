import numpy as np
import sys

def rc(seq):
    letters = []
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N' : 'N'} 
    seq_complement = tuple([complement[base] for base in seq])
    seq_complement = ''.join(seq_complement)
    return seq_complement[::-1]

fw = np.genfromtxt(sys.argv[1] + ".seq", dtype= None)
rcs = list()
for seq in fw:
	rcs.append(rc(seq.strip()))
np.savetxt(sys.argv[1] + ".pos.seq", np.hstack((fw, np.array(rcs))),fmt = "%s", delimiter = '')
