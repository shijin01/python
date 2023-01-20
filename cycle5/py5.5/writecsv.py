import csv
field=["no","company","model"]
bikes=[{"no":1,"company":"Yamaha","model":"FZ"},{"no":2,"company":"Bajaj","model":"Pulsar"},{"no":3,"company":"HERO","model":"X-Pulse"}]
with open('dict.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field)
    writer.writeheader()
    writer.writerows(bikes)
with open('dict.csv','r') as fileobj:
    read_obj = csv.reader(fileobj)
    l=[]
    for x in read_obj:
    	l.append(x)
    for i in l:
    	for j in i:
    		print(j,end="\t")
    	print()
	
