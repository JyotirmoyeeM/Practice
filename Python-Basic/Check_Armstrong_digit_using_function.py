def checkArmstrong(n):
    d = len(str(n))
    sum_of_digit_with_power = 0
    temp = n
    while n>0:
        x = n%10
        sum_of_digit_with_power += x**d 
        n //= 10
    
    return sum_of_digit_with_power == temp

def main():
    user_input = int(input())
    print(checkArmstrong(user_input)
