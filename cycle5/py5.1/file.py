f=open("file.txt","r")
l=[]
for i in f:
	l.append(i)
f.close()
print(l)
