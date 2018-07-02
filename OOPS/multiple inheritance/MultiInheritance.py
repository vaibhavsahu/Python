'multiple inheritance: Python allow to inherit a subclass from multiple parents or base calsses'
'in Python 3 and  pyuthon 2 with base class inherited from object class ,"Method Resolution Order" mro is used to search the method in class hierarchy'
'old style class in python 2 those base classses are not inherited from object class have depth first search- left to right order to search method or member in class hierarchy'
class A(object):
    def m():
        print('in A.m()')	
class B(A):
    pass   
  
class C(A):
    def m():
        print('in C.m()')	

class D(B,C):
    def m():
        print('in D.m()')		
d=D()
d.m()	


class A(object):
    def __init__(self):
        print('in A.__init__')	
class B(A):
    def __init__(self):
        print('in B.__init__')   
        super().__init__()
class C(A):
    def __init__(self):
        print('in C.__init__')
        super().__init__()

class D(B,C):
    def __init__(self):
        print('in D.__init__')
        super().__init__()
d=D()
d.mro()