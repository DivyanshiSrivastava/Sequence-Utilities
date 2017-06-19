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
Set=$3 
echo "Working with the ChIP-Seq: '$expt'"

if [ "$Set" == "B" ]; then
  # processing the positive set differently as I am reverse complementing.
  bash ~/group/lab/divyanshi/Sequence-Utilities/getfasta.sh $expt.200 $FILETYPE 
  python ~/group/lab/divyanshi/Sequence-Utilities/reverse_complement.py $expt.200
  # bed * 2 to account for rcs
  cat $expt.200.bed $expt.200.bed > loc.temp
  # coverage * 2 to account for rcs
  paste $expt.200.cov $expt.500.cov $expt.1000.cov > cov.temp
  cat cov.temp cov.temp > cov
  paste loc.temp $expt.200.seq cov | awk ' {OFS="\t"}{ print $0,1}'> $expt.mf
  rm loc.temp cov.temp cov
  mv $expt.mf .
  # dnase
elif [ "$Set" == "NB" ]; then
  # process negative set- as expt enter just prefix- eg. Ascl1.flanks
  bash ~/group/lab/divyanshi/Sequence-Utilities/getfasta.sh $expt.200 $FILETYPE
  paste $expt.200.bed $expt.200.seq $expt.200.bed.cov $expt.500.bed.cov $expt.1000.bed.cov | awk ' {OFS="\t"}{ print $0,0}' > $expt.mf
  mv $expt.mf .
fi

#python ~/group/lab/divyanshi/Sequence-Utilities/shuffle_dinucleotides.py $expt.pos.seq $expt.neg.seq
#cat $expt.neg.seq | awk ' { print $1,0}' > $expt.txt  
#cat $expt.pos.seq | awk ' { print $1,1}' >> $expt.txt
#cat $expt.txt | shuf - > $expt.shuf.txt

#rm $expt.seq
#rm $expt.pos.seq $expt.neg.seq $expt.txt
echo "Done"
