f1=open("file1.txt","r")
f2=open("file2.txt","w")
c=1
for i in f1:
	if(c%2!=0):
		f2.write(i)
	c+=1
f1.close()
f2.close()
f=open("file2.txt","r")
l=[]
for i in f:
	print(i)
f.close()
