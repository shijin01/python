'''a=[]
astr=input("Enter elements:")
astr=astr.split(" ")
print(astr)
a=list(map(int,astr))
c=[x for x in a if x>0 ]
print("List:",a)
print("1.Positive integer list:",c)
c=[x*x for x in a]
print("2.Square list:",c)'''
b=input("Enter elements:")
c=[i for i in b if(i in ['a','e','i','o','u','A','E','I','O','U'])]
print(f"vowels in string \"{b}\":{c}")
c=[ord(i) for i in b]
print("Ordinal:",c)
