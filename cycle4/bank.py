class bankaccount:
	def __init__(self,acc,name,acctype,bal):
		self.acc=acc
		self.name=name
		self.acctype=acctype
		self.bal=bal
	def deposit(self,amt):
		self.bal+=amt
	def withdraw(self,amt):
		if(bal==0 or bal-amt<0):
			print("insufficient accont balance")		
		else:
			self.bal-=amt
	def viewbalance(self):
		return balance

