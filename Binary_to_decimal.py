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
"""
Refined Explanation of the Logic
When converting a binary number to its integer equivalent, each digit in the binary number represents a power of 2, based on its position (or placeholder). Here's how it works:

Placeholder and Power of 2:

Each digit in the binary number corresponds to a placeholder, starting from the rightmost digit (which is the least significant bit).

The rightmost digit (ones place) has a placeholder value of 
2
0
=
1
2 
0
 =1.

The next digit to the left (tens place) has a placeholder value of 
2
1
=
2
2 
1
 =2.

The next digit (hundreds place) has a placeholder value of 
2
2
=
4
2 
2
 =4.

This pattern continues, with each subsequent placeholder being a power of 2 that increases by 1 as you move left.

Multiply and Sum:

For each digit in the binary number, multiply the digit (either 0 or 1) by its corresponding placeholder value (power of 2).

Add up all the results of these multiplications to get the final integer value.

Example
Let’s take the binary number 1011:

Break it down digit by digit, starting from the right:

Rightmost digit (1): 
1
×
2
0
=
1
×
1
=
1
1×2 
0
 =1×1=1

Next digit (1): 
1
×
2
1
=
1
×
2
=
2
1×2 
1
 =1×2=2

Next digit (0): 
0
×
2
2
=
0
×
4
=
0
0×2 
2
 =0×4=0

Leftmost digit (1): 
1
×
2
3
=
1
×
8
=
8
1×2 
3
 =1×8=8

Add up the results:

1
+
2
+
0
+
8
=
11
1+2+0+8=11

So, the binary number 1011 is equivalent to the integer 11.
"""
