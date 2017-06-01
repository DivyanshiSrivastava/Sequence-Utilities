# Takes as input events/bed file for a ChIP-Seq, and converts it into a matrix with sequences + rcs as features.
# It then creates a negative set by shuffling the positive set in a way that the dinucleotide frequency is maintained.  
# Input: Expt Name
# Outpt: Expt.shuf.txt
#
# Sample Output: 
#
# ATGCGCG 1
# CCCACTT 0
# CCGTCCA 0
# AATCGGC 1

expt=$1
FILETYPE=$2
echo "Working with the ChIP-Seq: '$expt'"

bash ~/group/lab/divyanshi/bash_scripts/getfasta.sh $expt $FILETYPE
python ~/group/lab/divyanshi/bash_scripts/reverse_complement.py $expt	
python ~/group/lab/divyanshi/bash_scripts/shuffle_dinucleotides.py $expt.pos.seq $expt.neg.seq

cat $expt.neg.seq | awk ' { print $1,0}' > $expt.txt  
cat $expt.pos.seq | awk ' { print $1,1}' >> $expt.txt
cat $expt.txt | shuf - > $expt.shuf.txt

rm $expt.seq
rm $expt.pos.seq $expt.neg.seq $expt.txt
echo "Done"
