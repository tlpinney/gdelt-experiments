import re

re_cameo = re.compile("^([0-9]+): (.+)$")

for line in open("cameo_clean.txt","r"):
    m = re_cameo.match(line)
    if m:
        if len(m.group(1)) > 2:
            print m.group(1) + "\t" + m.group(2)
