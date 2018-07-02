'Callable : A callable object is an object which can be used and behaves like a function but might not be a function.'
#if a calass implements the __call__ function then 	its object becaome callable and we apply function call on object obj(), it will invoke __call__ method.	'


class Cake:
    def __init__(self,flavour,qty):
	    self.flavour=flavour
	    self.qty=qty 

    def __call__(self):
	    return self.flavour + ' cake is delicious'
		
cObj=Cake('Mango',1)
print(cObj())	