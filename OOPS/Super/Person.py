'super method'
'''for initialization of base class member from subclass, we have to call base class constructor __int__  from subclass __init__ method.
in Python 2 we can call __init__ with base class name or with super( subclass,self).__init__() sysntax.
in python 3  we can call __init__ with super( subclass,self).__init__()   or    super().__init__() syntax
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.__class__.__name__ +" "+ self.name +' '+str(self.age)
		
class GoodPerson(Person):
    def __init__(self, name,age,gender):
        super(GoodPerson,self).__init__(name,age)  #will work with python2 and python 3
        self.gender=gender
    def __str__(self):
        return 	 self.__class__.__name__ +" "+ self.name +' '+str(self.age)+' '+ self.gender
		
class BadPerson(Person):
    def __init__(self, name,age,gender):
        super().__init__(name,age)  #will work only with python 3
        self.gender=gender
    def __str__(self): #method overriding
        return 	 self.__class__.__name__ +" "+ self.name +' '+str(self.age)+' '+ self.gender   		
		
p=Person('Adam',30)
print(p)
g=GoodPerson('Santa',32,'M')
print(g)  
b=BadPerson('Banta',33,'M')
print(b)