FILETYPE=$2
idx=$1

if [ "$FILETYPE" == "events" ]; then    	
    # getting the bed file
    cat $idx.events | cut -f 1 | grep -v "#" | awk ' BEGIN {FS=":"}{OFS="\t"}{ print $1,$2 - 100, $2 + 100}' | awk ' { if($2>0) print}' > $idx.bed 
elif [ "$FILETYPE" == "narrowPeak" ]; then    
    # getting th bed file
    cat $idx.narrowPeak | awk ' BEGIN {OFS="\t"}{OFMT="%d"}{ print $1,($2+$3)/2 - 100, ($2+$3)/2 + 100}' | awk ' { if($2 > 0) print}'> $idx.bed
elif [ "$FILETYPE" == "bed" ]; then
    # no action needed
    echo "already a bed file"
fi

~/group/software/bedtools2/bin/bedtools getfasta -fi ~/group/lab/divyanshi/genomes/mm10/mm10.fa -bed $idx.bed -fo $idx.fa
cat $idx.fa | grep -v ">" | awk ' { print toupper($0)}' > $idx.seq
