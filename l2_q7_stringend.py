str=input("Enter a string:")
print("String:",str)
if(str[-3:]=="ing"):
	str=str+"ly"
else:
	str=str+"ing"
print("String after update:",str)
