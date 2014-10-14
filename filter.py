from glob import glob

for i in glob("*.CSV"):
  for line in open(i,"r"):
    rows = line.strip().split("\t")
    # print rows[58]
    #if rows[51] == '':
    #  print "blank"

    if rows[51] == 'TK':
        print rows[51]

    #if rows[26] == '1821' and rows[51] = 'TK':
    #  print rows[26], rows[51]
    
    

