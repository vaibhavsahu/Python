	
'Test-Driven Development'
import unittest
class fibTest(unittest.TestCase):
    def setUp(self):
	    self.element=((0,0),(1,1),(2,1),(3,2),(4,3),(5,5))
	    print('setUp executed')
    def testCalculation(self):
        for i,val in self.element:
            self.assertEqual(fib(i),val)
    def tearDown(self):
        self.element=None
        print('tearDown executed ')		
if __name__ == '__main__':
    unittest.main()