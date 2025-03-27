#Write a program to find the sum of N natural numbers by creating a function.
# define a function named find_sum()
def find_sum(N):
    total = 0
    for i in range(1, N+1):
        total += i
    return total

number = int(input())

# call the function and print the return value
sum_of_num = find_sum(number)
print(sum_of_num)
