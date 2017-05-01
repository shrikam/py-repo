class Person:
	def __init__(self):
		print("class created")
	def __del__(self):
		print("class destroyed")
	def setName(self,firstName,lastName):
		self.firstName=firstName
		self.lastName=lastName
		
	def printName(self):
		print(self.firstName, self.lastName)
		
		
		
person_obj=Person()
person_obj.setName("shri","Kam")
person_obj.printName()
person_obj.__del__()

tp=Person()
tp.setName("heee","haaaa")
tp.printName()