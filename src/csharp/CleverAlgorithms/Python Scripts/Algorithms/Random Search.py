import unittest

try:
    j = 0
    l = int(raw_input("Adja meg a vektorok szamat: "))
    while j<l:
        vector_temp=[]
        i=0
        k=0
        n = int(raw_input("Adja meg a vektor hosszat: "))
        while i<n:
            k = int(raw_input("Adjon meg egy vektorbeli erteket: "))
            vector_temp.append(k)
            i=i+1
        j=j+1
    ossz = int(raw_input("Adja meg a vegeredmeny erteket: "))
        
    def Random_Search(vector):
        summa = 0
        for i in vector:
            summa = summa+i**2
        return summa.random()
            
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(min(Random_Search(vector_temp)), ossz)
    if __name__=='__main__':
        unittest.main()
    
except ValueError:
    print "Nem szamot adtal meg."