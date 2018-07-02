'operator overloding'
'if we need to perform  addition of two objects of a class we can overload the __add__() method in class and on + operation  __add__() method will be called. we can also overload other arithmatic operator like __sub__,__mul_, __div__'	
	  
class Cake:
    def __init__(self,flavour,qty):
	    self.flavour=flavour
	    self.qty=qty
    def __add__(self,other):
	    self.qty+=other.qty
	    return self.qty
c1=Cake('Apple',10)	
c2=Cake('Pinapple',10)
print(c1+c2)	

print(c1.qty)