dict1={}
dict2={}
dict3={}
n=int(input("enter number of items in the dictionary 1:"))
for i in range(n):
	key=input("enter key:")
	value=input("enter value:")
	dict1[key]=value
n2=int(input("enter number of items in the dictionary 2:"))
for i in range(n2):
	key=input("enter key:")
	value=input("enter value:")
	dict2[key]=value
print("1st dictionary:",dict1)
print("2nd dictionary:",dict2)
dict3={**dict1,**dict2}
for k,v in dict3.items():
	if k in dict1 and k in dict2:
		dict3[k]=[v,dict1[k]]
print("dict1+dict2 after merging with duplicate val",dict3)
