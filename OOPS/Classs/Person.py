'class without implementation with pass statment'
class Person:
    pass
	

class Person(object):
    def __init__(self,name,age): 
	    '__init__ method work as constructor, automatically get called after object creation for initialization of data members.'
	    self.name=name
	    self.age=age
	    
    def __del__(self):
        'work like destructor  but should called manually  from code to release the resource of objects'
        print('in del method')
    
    def __repr__(self):
        '''it is used for internal representation of object. get called when we try to print instance of calss  without print() function
        or   repr() function  applied on it or S __str__ function is not implemented.'''
        return "Person('"+ self.name+ "'," + str(self.age) + ")"
    
    def __str__(self):
        'get called when we print the instance of calss or with str()  function  applied on it , should be use to display the info to the  end user'
        return self.name+'-' + str(self.age)
    
	    
obj= Person('Javier',35)
obj
print(obj)
#del obj
#eval can only be applied on the strings created by repr
obj = eval(repr(obj)) #evaluate internal repesentation of object to object
print(obj.name)