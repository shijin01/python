def pyramid(n):
	for i in range(1,n+1):
		for j in range(1,i+1):
			print(j*i,end="\t")
		print()
n=int(input("Enter a number:"))
pyramid(n)
