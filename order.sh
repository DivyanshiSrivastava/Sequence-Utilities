ls p* | sort -V > order.txt
while read -r line; do cat $line >> temp; done < order.txt
cat temp | cut -d " " -f 2 > test.out
