class Person:
	def __init__(self):
		print("class created")
	def __del__(self):
		print("class destroyed")
	def setName(self,firstName,lastName):
		self.firstName=firstName
		self.lastName=lastName
	def setAge(self,nAge):
		self.nAge=nAge
	def printName(self):
		print(self.firstName, self.lastName,self.nAge)
	def addName(self):
		print(self.firstName + self.lastName)
     		

person_obj=Person()
person_obj.setName("shri","Kam")
person_obj.setAge("30")
person_obj.printName()
person_obj.__del__()

tp=Person()
tp.setName("heee","haaaa")
tp.setAge("45")
tp.printName()
tp.addName()
tp.__del__()


try_me=Person()
try_me.setName("kam","shri")
try_me.setAge("40")
try_me.addName()
try_me.printName()
try_me.__del__()
