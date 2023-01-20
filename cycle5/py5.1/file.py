f=open("file.txt","r")
l=[]
for i in f:
	l.append(i.rstrip("\n"))
f.close()
print(l)
