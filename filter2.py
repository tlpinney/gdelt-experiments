from glob import glob

# load cameo codes 
cameo = {}
f = open("cameo.tsv", "r")
for line in f:
    row = line.rstrip("\n").split("\t")
    cameo[row[0]] = row[1]


for i in glob("data/*.CSV"):
    for line in open(i,"r"):
        rows = line.strip().split("\t")
        
        #if rows[53] == 'BR' and rows[26] in ('1821', '1384', '1385', '1383', '137', '182', '175', '193', '194', '1951', '1952', '196', '202', '203', '2041', '2042'):
        if rows[55] == '-671824' and rows[26] in ('1821', '1384', '1385', '1383', '137', '182', '175', '193', '194', '1951', '1952', '196', '202', '203', '2041', '2042'):
            print "\t".join((rows[0], rows[1], rows[26], cameo[rows[26]], rows[51], rows[53], rows[54], rows[57]
