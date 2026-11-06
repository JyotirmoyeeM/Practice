"""Print composite numbers up to an inclusive limit."""


def is_prime(number):
    """Return whether ``number`` is prime."""
    if number < 2:
        return False
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False
    return True


def print_composite(limit):
    """Print all composite numbers from 2 through ``limit``."""
    for number in range(2, limit + 1):
        if not is_prime(number):
            print(number)


if __name__ == "__main__":
    print_composite(int(input()))
