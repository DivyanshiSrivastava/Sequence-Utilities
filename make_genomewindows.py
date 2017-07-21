import numpy as np
import sys

# read chr size file
genomefile = np.genfromtxt("/home/dvs5680/group/lab/divyanshi/genomes/mm10/mm10-main.chrom.sizes", dtype = None)
print genomefile

for chrom,chrom_size in genomefile:
    # keeping a 500 window on either side for coverage! :)
    with open("mm10.500.windows.bed", "a") as fp:
        start = 550
        step =  50
        window = 500
        while start + 200 < chrom_size -550:
            fp.write("%s\t%d\t%d\n" % (chrom,start,start + window))
            start = start + step
# done
