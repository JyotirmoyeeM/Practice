“””to print pattern 
(1)    * * * *
		   * * * *
		   * * * *
		   * * * *

 (2)    1234
        1234
        1234
        1234

(3)     1111
        2222
        3333
        4444
  
“””
N = 4

def star_square_pattern(N):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print("*", end="")
        print()
def accending_integer_square_pattern(N):
    for i in range(1,N + 1, 1):
        for j in range(1, N + 1, 1):
            print(j, end="")
        print()

star_square_pattern(N)
print()
accending_integer_square_pattern(N)
