a=input("Enter firstname list:")
a=a.split(" ")
n=0
for i in a:
	if 'a' in i:
		n+=1
print(f"Occurance of \'a\' in {a}:{n}")
