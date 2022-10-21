a=[]
b=[]
s1=0
s2=0
astr=input("Enter the elements of list1:")
n=0
astr=astr.split(" ")
bstr=input("Enter the elements of list2:")
bstr=bstr.split(" ")
for i in astr:
    e=int(i)
    a.append(e)
    s1+=e
    n+=1
b=list(map(int,bstr))
m=len(b)
s2=sum(b)
c=[]
for i in a:
    if i in b:
        c.append(i)
if(m==n):
    print("Same length")
else:
    print("Different length")
print("S1=",s1,"S2=",s2)
if(s1==s2):
    print("Sum of elements in both list are same")
else:
    print("Sum of elements in both list are different")
if(len(c)==0):
    print("No common elements")
else:
    print("Common elements:",c)
