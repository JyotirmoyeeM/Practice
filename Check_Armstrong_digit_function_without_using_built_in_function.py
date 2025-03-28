#Write a program to check Armstrong digit without using the built in function
"""Steps to write the program are
        --find the length of the input
        --input check armstrong digit logic
        --output
"""

#length of input
def find_length(string):
    count = 0
    for _ in string:
        count += 1
    return count
    
# check armstrong logic
def  checkArmstrong(n):
    d = find_length(str(n))
    sum_of_digit_to_power = 0
    temp = n
    while n > 0:
        x = n % 10
        sum_of_digit_to_power += x**d
        n //= 10
    
    return sum_of_digit_to_power == temp
    
#output
def main():
    user_input = int(input())
    print(checkArmstrong(user_input))
    
main()
