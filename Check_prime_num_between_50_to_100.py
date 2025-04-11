# function to check prime numbers between 50 and 100
def check_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

n1 = 50
n2 = 100

# iterate loop from 50 to 100
for number in range(n1, n2+1):
    is_prime = check_prime(number)

    # print if the number is prime
    if is_prime:
        print(f"This a prime number: {number}")
