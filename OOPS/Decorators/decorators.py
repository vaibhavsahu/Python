'''Decorators:  decorators are callable object used to modify the behaviour of function or class.
   decorator takes function or class as input argument , modify the behaviour and return the modified  function or class.
'''

def simpleDecorator(func):
    def functionWrapper(*args):
	    return func(*args) + ' simplefied using Decorator'
    return 	functionWrapper	    
def myfunc(*args):
    return 'My function'


'''there are two way to call decorator both '''
'pass your function as argument to decorator function, it will return modified function and then we call the function returned by decorator'
myfunc=simpleDecorator(myfunc)
print(myfunc())	


'second option is apply the decorator syntax @simpleDecorator on you function given below'

@simpleDecorator
def myfunc1(*args):
    return 'My function1'

print(myfunc1())

'Class based Decorator: classes with __call__ method implemented can be used as decorator and will work same as function decorator  '

class ClassDecorator:
    def __init__(self,func):
	    self.func=func
    def __call__(self,*args)	:
	    return 'Decorating '+self.func(*args) 
@ClassDecorator		
def myfunc2():# no argument function
    return 'myfunc2'		

print(myfunc2())

@ClassDecorator		
def myfunc3(x): #function with argument
    return 'myfunc2'+x		

print(myfunc3('000'))	

'memorize with Decorators: in   problems like fibbonacci series instead of doing same  calculating  again and again for same inputs we can save the results and use then for same inputs  '

def memorizeDecorator(func):
    memory={} 
    def wrapperFunction(x):
	    if x not in memory:
	        memory[x]= func(x)
	    return  memory[x]
    return  wrapperFunction		
@memorizeDecorator
def fib(x):
    'return the nth element of fib series starting from 1'
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(5))


class memorizeDecoratorCalss:
    def __init__(self,func):
	    self.func=func
	    self.memory={}
    def __call__(self,n):
        if n not in self.memory:
            self.memory[n]=self.func(n)
        return self.memory[n]
@memorizeDecoratorCalss
def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
