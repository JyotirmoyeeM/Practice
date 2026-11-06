"""Convert a binary string to its decimal value without using int(..., 2)."""


def binary_to_decimal(binary):
    """Return the decimal value of a string containing only 0s and 1s."""
    if not binary or any(digit not in "01" for digit in binary):
        raise ValueError("binary must contain at least one 0 or 1")

    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + int(digit)
    return decimal


if __name__ == "__main__":
    print(binary_to_decimal(input("Enter a binary number: ").strip()))
