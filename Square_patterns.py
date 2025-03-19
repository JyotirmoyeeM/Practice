“”” to print pattern 
(1)     * * * *
	* * * *
	* * * *
	* * * *

 (2)    1234
        1234
        1234
        1234

 (3)    4321
	4321
	4321
	4321

 (4)    1111
        2222
        3333
        4444

 (5)	4444
	3333
	2222
	1111

  
“””
N = 4

def star_square_pattern(N):
    for i in range(1, N + 1, 1):
        for j in range(1, N + 1,1):
            print("*", end="")
        print()

def accending_integer_square_pattern(N):
    for i in range(1,N + 1, 1):
        for j in range(1, N + 1, 1):
            print(j, end="")
        print()
def decending_integer_square_pattern(N):
    for i in range(1,N+1,1):
        for j in range(N, 0, -1):
            print(j, end ="")
        print()
def increasing_integer_square_pattern(N):
    for i in range(1,N + 1, 1):
        for j in range(1, N + 1, 1):
            print(i, end="")
        print()

def decreasing_integer_square_pattern(N):
    for i in range(N, 0, -1):   # i = 4 to 1
        for j in range(1, N + 1):
            print(i, end="")
        print()

        
star_square_pattern(N)
print()
accending_integer_square_pattern(N)
print()
decending_integer_square_pattern(N)
print()
increasing_integer_square_pattern(N)
print()
decreasing_integer_square_pattern(N)
