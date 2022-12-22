class bankaccount:
	def __init__(self,accno,name,acctype,bal):
		self.accno=accno
		self.name=name
		self.acctype=acctype
		self.bal=bal
	def deposit(self,amt):
		self.bal+=amt
	def withdraw(self,amt):
		if(bal-amt<0):
			print("insufficient accont balance")		
		else:
			self.bal-=amt
			print("Amount withdrawn successfully")
accno=int(input("Enter account number:"))
name=input("Enter name:")
acctp=input("Enter account type:")
bal=int(input("Enter balance:"))
acc=bankaccount(accno,name,acctp,bal)
while(1):
	print("MENU\n\t1.Deposit\n\t2.Withdraw\n\t3.View detail\n\t4.Exit")
	n=int(input("Enter choice:"))
	if(n==1):
		amt=int(input("Enter amount:"))
		acc.deposit(amt)
		print(f"Deposited successfully\n Account balance is:{acc.bal}")
	elif(n==2):
		amt=int(input("Enter amount:"))
		acc.withdraw(amt)
		print(f"Account balance is:{acc.bal}")
	elif(n==3):
		print(f"Account number:{acc.accno}\nAccount holder name:{acc.name}\nAccount type:{acc.acctype}\nBalance:{acc.bal}")
	elif(n==4):
		break
	else:
		print("Invalid operation")

	



