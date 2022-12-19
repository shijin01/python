class rectangle:
	
	def __init__(self,a,b):
		self.length=a
		self.breadth=b
		
	def area(self):
		self.area1=self.length*self.breadth
		return self.area1
	def perimeter(self):
		self.perimeter1=2*(self.length+self.breadth)
		return self.perimeter1
l1=int(input("Enter length of rectangle1:"))
b1=int(input("Enter breadth of rectangle1:"))
l2=int(input("Enter length of rectangle2:"))
b2=int(input("Enter breadth of rectangle2:"))
r1=rectangle(l1,b1)
r2=rectangle(l2,b2)
a1=r1.area()
a2=r2.area()
p1=r1.perimeter()
p2=r2.perimeter()

print(f"Area of rectangle 1:{a1}\nPerimeter of rectangle1:{p1}")
print(f"Area of rectangle 2:{a2}\nPerimeter of rectangle2:{p2}")
if(a1>a2):
	print("a is large")
else:
	print("b is large")

