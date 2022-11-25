def factor(n):
	for i in range(n):
		if(n%i==0):
			print(i,end="\t")
n=int(input("Enter a number:"))
print(f"factor of {n}:",end="\t")
factor(n)
