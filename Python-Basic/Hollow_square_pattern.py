def hollow_square_pattern(N):
    for i in range(1, N + 1, 1):
        for j in range(1, N + 1, 1):
            if i == 1 or i == N or j == 1 or j == N:
                print("*", end=" ")
            else:
                print(" ", end= " ")
        print()
        
def hollow_accending_integer_square_pattern(N):
    for i in range(1, N + 1, 1):
        for j in range(1, N + 1, 1):
            if i == 1 or i==N or j == 1 or j == N:
                print(j, end=" ")
            else:
                print(" ", end = " ")
        print()

def hollow_decreaing_integer_square_pattern(N):
    for i in range(1, N + 1 , 1):
        for j in range(N, 0, -1):
            if i == 1 or i==N or j == 1 or j == N:
                print(j, end=" ")
            else:
                print(" ", end = " ")
        print()

def increasing_hollow_square_pattern(N):
    for i in range(1, N + 1, 1):
        for j in range(1, N + 1, 1):
            if i == 1 or i == N or j == 1 or j == N:
                print(i, end=" ")
            else:
                print(" ", end= " ")
        print()

def decreasing_hollow_square_pattern(N):
    for i in range(N, 0, -1):
        for j in range(1, N + 1, 1):
            if i == 1 or i == N or j == 1 or j == N:
                print(i, end=" ")
            else:
                print(" ", end= " ")
        print()

hollow_square_pattern(N)
print()
hollow_accending_integer_square_pattern(N)
print()
hollow_decreaing_integer_square_pattern(N)
print()
increasing_hollow_square_pattern(N)
print()
decreasing_hollow_square_pattern(N)
print()
