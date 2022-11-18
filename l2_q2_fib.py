def fib(n):
	a=1
	b=0
	c=a+b
	while(b<n):
		print(b,end="\t")
		a=b
		b=c
		c=a+b
	
n=int(input("Enter a number:"))
print(f"Fibonacci series upto {n}:",end=" ")
fib(n)

