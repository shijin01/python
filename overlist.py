n=int(input("Enter the number of elements in list:"))
print(f"Enter {n} elements:")
a=[]
for i in range(n):
	e=int(input())
	if e>100:
		a.append("over")
	else:
		a.append(e)
print(f" List:{a}")
