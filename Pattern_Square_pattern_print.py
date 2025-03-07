"""Today we shall be printing pattern SQUARE
*****
*****
*****
*****
*****

-----------------------
12345
12345
12345
12345
12345
-----------------------
11111
22222
33333
44444
55555
"""

N=5
_
def Pattern_Star_square():
  for i in range(1, N+1):
    for j in range(1. N+1):
      print("*",end="")
    print()

def Pattern_row_number():
    for i in range(1, N+1):
    for j in range(1. N+1):
      print(j,end="")
    print()

def Patter_coloumn_number():
    for i in range(1, N+1):
    for j in range(1. N+1):
      print(i,end="")
    print()

Pattern_Star_square()
Pattern_row_number()
Patter_column_number()

