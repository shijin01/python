class Publisher:
	def __init__(self,name):
		self.pname=name
	def viewdetail(self):
		print("Publisher:",self.pname)
class Book(Publisher):
	def __init__(self,title,author,pname):
		self.title=title
		self.author=author
		super().__init__(pname)
	def viewdetail(self):
		print("Title:",self.title)
		print("Author:",self.author)
		super().viewdetail()
class Python(Book):
	def __init__(self,title,author,publisher,price,pgno):
		self.price=price
		self.pgno=pgno
		super().__init__(title,author,publisher)
	def viewdetail(self):
		super().viewdetail()
		print("Price:",self.price)
		print("Page number",self.pgno)
p=Python("Python","Raj","DC books",1004,154)
p.viewdetail()
