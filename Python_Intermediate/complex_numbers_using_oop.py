#create a program TO ADD COMPLEX NUMBERS
class Complex:
    def __init__(self, imag, real):
        self.imag = imag
        self.real = real
        
        def add(self, number):
            result_imag = self.imag + number.imag
            result_real = self.real + number.real
            
            result = Complex(result_imag, result_real)
            return result
        
        
    
    
    

n1 = Complex(5,6)
n2 = Complex(-4,2)

n3 = n1.add(n2)

# printing n3 attributes
print('real part =', n3.real)
print('imaginary part =', n3.imaginary)
