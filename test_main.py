import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_prime_function(self) :
        for n in range(2,100) :
           p = 1
           for j in range(2,n) :
               if n%j==0 : p=0
           if p==1 : self.assertTrue( isPrime(n)==1, "Your function for detecting prime numbers does not work" )
           else : self.assertTrue( isPrime(n)==0, "Your function for detecting prime numbers does not work" )
