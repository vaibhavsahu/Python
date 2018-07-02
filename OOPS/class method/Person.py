'''Class methods:   class method are bound to class. first parameter of calss method is reference to class. we can call thm with calls or with instances.
static method will not work as expected in subclass because they don't know about subclasses members during inheritance b because they need to hardcode the class name.
classmethod solves our problem and work fine with inheritance because be have the reference to the current class as first argument of method
'''
class Person:
    name='Adam'
    @staticmethod
    def about():
	' class name is hardcoded and will return base class member only if we call it from subclass also'
        return Person.name 
	    
class 	GoodPerson(Person):
    name='Santa'   
class BadPerson(Person):
    name='Banta'	

pObj=Person()
print(pObj.about())	

gObj=GoodPerson()
print(gObj.about())
bObj=BadPerson()
print(bObj.about())