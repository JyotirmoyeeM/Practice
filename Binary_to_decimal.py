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
print(ans)
