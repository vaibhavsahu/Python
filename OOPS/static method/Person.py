'''staticmethod:
    static method does not need the self as first argument.  static methods are bound to instances not class
to make a method static we have to apply @staticmethod decorator
'''
class Person(object):
    __count=0
    def __init__(self):
        type(self).__count += 1
    @staticmethod	
    def personInstances():
	    return Person.__count
p=Person()
print(p.personInstances())    
q=Person()
print(q.personInstances())   
print(p.personInstances())
print(Person.personInstances())