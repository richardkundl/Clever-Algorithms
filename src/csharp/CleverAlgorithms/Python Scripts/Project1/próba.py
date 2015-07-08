import unittest

def objective_function(vector):
    summa=0
    for i in vector:
        summa=summa+i**2
    return summa

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(objective_function([2,3]), 13)
if __name__=='__main__':
    unittest.main()