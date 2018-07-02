'''Class methods:   class method are bound to class. first parameter of calss method is reference to class. we can call thm with calls or with instances.
static method will not work as expected in subclass because they don't know about subclasses members during inheritance b because they need to hardcode the class name.
classmethod solves our problem and work fine with inheritance because be have the reference to the current class as first argument of method
'''
class Person:
    name='Adam'
    @classmethod
    def about(cls):
        'we have the reference to the current class so it will return the menber of current class'
        return cls.__name__ +' '+ cls.name
	    
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