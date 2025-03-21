"""To print following patterns
D C B A 

A B C D 

A B C D 
A B C D 
A B C D 
A B C D 


D C B A 
D C B A 
D C B A 
D C B A 


A A A 
B B B 
C C C 
D D D 


D D D D 
C C C C 
B B B B 
A A A A 
"""

N = 4

def to_printAlphabets(N):
    for i in range(0,N,1):
        print(chr(65+i), end= " ")

def to_printAlphabets_reverse(N):
    for i in range(N-1, -1,-1):
        print(chr(65+i), end= " ")

def to_printsquare_alphabets(N):
    for i in range(0, N, 1):
        for j in range(0, N, 1):
            print(chr(65+ j), end= " ")
        print()

def to_print_reverse_square_alphabets(N):
    for i in range(0, N, 1):
        for j in range(N-1,-1, -1):
            print(chr(65+ j), end= " ")
        print()

def to_print_INCREASING_square_alphabets(N):
    for i in range(0, N, 1):
        for j in range(1, N, 1):
            print(chr(65+ i), end= " ")
        print()
        
def to_print_DECREASING_square_alphabets(N):
    for i in range(N-1,-1,-1):
        for j in range(1,N+1,1):
            print(chr(65+ i), end= " ")
        print()

to_printAlphabets_reverse(N)
print("\n")  
to_printAlphabets(N)    
print("\n")   
to_printsquare_alphabets(N)
print("\n")
to_print_reverse_square_alphabets(N)
print("\n")  
to_print_INCREASING_square_alphabets(N)
print("\n")  
to_print_DECREASING_square_alphabets(N)
