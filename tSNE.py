from __future__ import division
import sys, os
import itertools
import numpy as np
from collections import defaultdict
import sklearn
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD

print sklearn.__version__

print "Laoding features..."
features = np.genfromtxt("features.txt", dtype = int, delimiter = ",")
labels = np.genfromtxt("/Users/divyanshisrivastava/Desktop/Projects/data/label.txt", dtype = int)
print "Done loading"
print features.shape
print features
print labels
print labels.shape

# reduce dimensionality using svd ( for a sparse matrix )

svd = TruncatedSVD(n_components=50, n_iter=7)
svd_reduced = svd.fit_transform(features)
print svd_reduced
print svd_reduced.shape

# tSNE on a subset ( first pass as the whole thing takes a long time.)
mask = np.random.choice([False, True], len(features), p=[0.2, 0.8])
svd_reduced = svd_reduced[mask,:]
labels = labels[mask]
print svd_reduced
print svd_reduced.shape

model = TSNE(n_components=2)
print "Fitting the model..."
reduced = model.fit_transform(svd_reduced)
"Done fitting"
print reduced
print reduced.shape

from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

np.savetxt("reduced-labels.txt", labels, fmt = "%d")
np.savetxt("reduced.txt",reduced, fmt = "%f")

#plt.scatter(reduced[:,0],reduced[:,1], c = labels, cmap = Dark)