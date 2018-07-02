'''__new__   The magic method __new__ will be called when instance is being created. Using this method you can customize the instance creation. This is only the method which will be called first then __init__ will be called to initialize instance when you are creating instance.
Method __new__ will take class reference as the first argument followed by arguments which are passed to constructor. Method __new__ is responsible to create instance, so you can use this method to customize object creation. Typically method __new__ will return the created instance object reference. Method __init__ will be called once __new__ method completed execution. '''
'We can create singleton class using __new__ method. singleton class is a class can has only one object or instance'	    
class Singleton(object):
    _instance=None
    def __init__(self):
        self.name=None
    
    def __new__(cls,*args,**kargs):
        if not cls._instance:
            cls._instance=object.__new__(cls,*args,**kargs)		
        return cls._instance
s=Singleton()
s.name='Santosh'
r=Singleton()
r.name='Vaibhav'