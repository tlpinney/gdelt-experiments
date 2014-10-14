import requests

#http://data.gdeltproject.org/events/20141002.export.CSV.zip

r = requests.get("http://data.gdeltproject.org/events/20141002.export.CSV.zip")
open("20141002.export.CSV.zip","w").write(r.content)
r = requests.get("http://data.gdeltproject.org/events/20141001.export.CSV.zip")
open("20141001.export.CSV.zip","w").write(r.content)

for i in range(1,31):
  r = requests.get("http://data.gdeltproject.org/events/201409%02d.export.CSV.zip" % i)
  open("201409%02d.export.CSV.zip" % i,"w").write(r.content)

for i in range(1,32):
  r = requests.get("http://data.gdeltproject.org/events/201408%02d.export.CSV.zip" % i)
  open("201408%02d.export.CSV.zip" % i,"w").write(r.content)
