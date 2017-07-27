# Get Mus musculus specific sites

import sys,os

flag = 0 

with open(sys.argv[1], "r") as fp:
  for line in fp:
    if flag == 1 and "DE" in line: 
        flag =0      
    if sys.argv[2] not in line and flag == 1:
        print line.strip()
    if flag == 0 and sys.argv[2] in line:
      print line.strip()
      flag = 1
    else:
      pass
