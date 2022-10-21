'''a=[1,2,3,4]
for i in a:
    print(i)'''
a=[]
n=int(input("Enter the size of list:"))
for i in range(n):
    print("Enter num-",i+1,":",end=" ")
    e=int(input())
    a.append(e)
print("List:",end=" ")
for i in a:
    print(i,end=" ")
