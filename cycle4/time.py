class Time:
	def __init__(self,hour,minute,sec):
		self._hour=hour
		self._minute=minute
		self._sec=sec
	def __add__(self,other):
		hour=self._hour+other._hour
		if(hour>=24):
			hour=hour%24
		minute=self._minute+other._minute
		if(minute>=60):
			hour+=1
			minute=minute%60
		sec=self._sec+other._sec
		if(sec>=60):
			minute+=1
			sec=sec%60
		return Time(hour,minute,sec)
	def viewtime(self):
		print(f"{self._hour}:{self._minute}:{self._sec}")
t1=[int(i)  for i in input("Enter time1:").split(":")]
t2=[int(i) for i in input("Enter time2:").split(":")]
time1=Time(t1[0],t1[1],t1[2])
time2=Time(t2[0],t2[1],t2[2])
sumt=time1+time2
print("Time1:",end=" ")
time1.viewtime()
print("Time2:",end=" ")
time2.viewtime()
print("Sum:",end=" ")
sumt.viewtime()

