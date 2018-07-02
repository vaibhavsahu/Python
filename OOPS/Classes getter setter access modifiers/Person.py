'''private , protected and public member ,
getter, setter methods
''' 

class Person(object):
    def __init__(self,name,age):
	    self.__name=name # private menber , should not be accessed directly by calss name  object._Person__name
	    self.__age=age
	    self._food='NA' # protected member , should be used by subclass only 
	    
    def __del__(self):
        print('in del method')
    
    def __repr__(self):
        '''it is used for internal representation of object. get called when we try to print instance of calss  without print() function
        or   repr() function  applied on it or if __str__ function is not implemented.'''
        return "Person('"+ self.__name+ "'," + str(self.__age) + ")"
    
    def __str__(self):
        'get called when we print the instance of calss or with str()  function  applied on it , should be use to display the info to the  end user'
        return self.__name+'-' + str(self.__age)    

    @property
    def name(self):
        'getter method of __name member'
        return self.__name
    @name.setter	
    def name(self,name):
        'setter method of __name member'
        self.__name=name

    @name.deleter
    def name(self):
        self._name = N
        
obj= Person('Roberto',30) 
obj.name='Atul'
print(obj.name)