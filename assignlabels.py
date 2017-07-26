import numpy as np
import sys, os

labels = np.loadtxt("Ascl1.intermediate.labels", dtype = "str")
refined_labels = labels.copy()

for ids in np.argwhere(labels=="SB"):
	if labels[int(ids)-1] != "SB":
		refined_labels[int(ids)-3:int(ids)] ="A"
	if labels[int(ids)+1] != "SB":
		refined_labels[int(ids)+1:int(ids)+4] ="A"
	else:
		pass

for ids in np.argwhere(refined_labels =="WB"):
	refined_labels[int(ids)-3: int(ids)+4] = "A"

np.savetxt("Ascl1.labels", refined_labels, fmt = "%s")
