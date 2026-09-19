class Dog:
 def __init__(self,pet_name):
  
 @property
 def pet_name(self):
  return self._pet_name
 @pet_name.setter
 def pet_name(self,pet_name):
  self._pet_name=pet_name