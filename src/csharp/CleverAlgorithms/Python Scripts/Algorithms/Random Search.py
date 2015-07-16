import unittest

try:
    vector_temp=[]
    i=0
    k=0
    n = int(raw_input("Adja meg a vektor hosszat: "))
    while i<=n:
        k = int(raw_input("Adjon meg egy vektorbeli erteket: "))
        vector_temp.append(k)
        i=i+1
    ossz_ertek = int(raw_input("Adja meg a vegeredmenyt: "))
    def Random_Search(vector):
        summa = 0
        for i in vector:
                summa = summa+i**2
        return summa
        print summa
        
    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(Random_Search(vector_temp), ossz_ertek)
    if __name__=='__main__':
        unittest.main()
    
except ValueError:
    print "Nem szamot adtal meg."