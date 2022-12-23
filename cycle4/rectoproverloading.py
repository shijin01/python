class rectangle:
	def __init__(self,a,b):
		self.__length=a
		self.__breadth=b
		
	def area(self):
		self.area1=self.__length*self.__breadth
		return self.area1
	def __lt__(self,other):
		if(self.area1<other.area1):
			return 1
		else:
			return 0
l1=int(input("Enter length of rectangle1:"))
b1=int(input("Enter breadth of rectangle1:"))
l2=int(input("Enter length of rectangle2:"))
b2=int(input("Enter breadth of rectangle2:"))
r1=rectangle(l1,b1)
r2=rectangle(l2,b2)
print(f"Area of rectangle 1:{r1.area()}")
print(f"Area of rectangle 2:{r2.area()}")
if(r1<r2):
	print("rectangle2 is large")
else:
	print("rectangle1 is large")
