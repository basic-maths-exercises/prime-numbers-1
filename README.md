# Detecting prime numbers

In the remainder of this exercise, we are going to consider how we use the language of logical propositions that we have introduced in mathematical definitions.  We are going to consider the definition of a prime number in particular.  To remind you prime numbers are defined as follows:

_A natural number p is said to be a prime number if it is greater than 1 and if its only divisors are 1 and p itself._ 

Consequently, for any number that is not prime, there exists a number a which is greater than 1 and less than p, which divides p.  Given this definition, you hopefully see how we might write a function to detect if a number is prime if we have some way to determine if a divides by.

The piece of the puzzle that is missing for you is the modulo operator.  If in Python we write the expression:

````
a = b%c
````

`a` is set equal to the remainder when `b` is divided by `c`.  In other words, if `b` is equal to 6 and `c` is equal to 4 then `b%c` is 2.  Alternatively, if `b=7` and `c=3` then `b%c = 1`.

With that in mind see if you can complete the function `isPrime` in `main.py`.  This function takes a single integer, `a`, in input.  The code should return 1 if `a` is prime and zero otherwise.  
