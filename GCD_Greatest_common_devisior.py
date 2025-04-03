"""
Lets Understand GCD.

GCD stands for "Greatest Common Divisor." It refers to the largest positive integer that divides two or more numbers without leaving a remainder. 
example 

One way to find the GCD is to use the prime factorization method:
Prime factorization of 96: 96 = 2*2*2*2*2*3
Prime factorization of 28: 28 = 2*2* 7
Common prime factors: 2*2
Therefore, the GCD of 96 and 28 is 4.


Algorithm for finding the greatest common divisor (GCD) of two integers `a` and `b`. The
algorithm is a well-known method for finding the GCD efficiently and is based on the fact that
the GCD of two numbers remains the same if you repeatedly take the remainder of the
larger number divided by the smaller number until the smaller number becomes zero. Here's
the algorithm step by step:
1. Start with two integers `a` and `b`, where `a` is greater than or equal to `b`.
2. While `b` is not equal to zero:
a. Calculate the remainder of `a` divided by `b`, i.e., `a % b`.
b. Update `a` with the value of `b`.
c. Update `b` with the remainder obtained in step (a).
3. Repeat step 2 until `b` becomes zero.
4. When `b` becomes zero, the GCD is the value of `a`.
The algorithm efficiently reduces the two numbers by taking the remainder, ensuring that the
GCD remains the same throughout the process. When `b` becomes zero, `a` will be the
GCD of the original `a` and `b`.

"""

def check_Gcdnumber(a, b):
  while b != 0 :
    remainder = b % a
    a = b
    b = remainder
  return a

a = int(input())
b = int(input())

check_Gcdnumber(a, b)

