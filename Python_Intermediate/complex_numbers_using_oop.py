"""A small example of adding complex numbers with a class."""


class Complex:
    """Represent a complex number using real and imaginary parts."""

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        """Return the sum without changing either input."""
        return Complex(self.real + number.real, self.imag + number.imag)


if __name__ == "__main__":
    first = Complex(6, 5)
    second = Complex(2, -4)
    result = first.add(second)
    print(f"real part = {result.real}")
    print(f"imaginary part = {result.imag}")
