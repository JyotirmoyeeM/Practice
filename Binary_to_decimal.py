#WAP a program to convert Binary to integers
N= int(input())
ans =0
last_digit= 0
pow_of_two = 1
while N>0:
  last_digit = N % 10
  ans+= last_digit*pow_of_two
  pow_of_two*=2
  n//=2
print(and)
"""
Here the logic used is that if a binary is given then for every digit in the binary we will assign it placeholder with the power of 2, where the zeros place one will have the power of two as 1, tenths place will have 2, hundreds will have 4 and so on and we will first multiply the placeholder digits with the 
power of 2 assigned to the same placeholder and lastly, we will add all of their output to find the result as over binary conversion to integer.
"""
