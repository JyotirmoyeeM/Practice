#write a function to convert the given input to list and list to integer
def convertion_of_input_type(n):
    #for integer input converting to list
    if isinstance(n, int):
        if n == 0:
            return [0]
        lst =[]
        while n> 0:
            remainder = n % 10
            lst.append(remainder)
            n = n //10
        lst.reverse()
        return lst
    #for integer string converting to list
    elif isinstance(n, str):
        if not n.isdigit():
            raise ValueError("String input should have all digit")
        n = int(n)
        lst2 = []
        while n > 0:
            remainder = n % 10
            lst2.append(remainder)
            n = n //10
        lst2.reverse()
        return lst2
    
    #for list input converting to integer
    elif isinstance(n, list):
        string = 0
        for i in n:
            string = string*10 + i
        return string
    else:
        return ValueError("Input should either be string or integer or List.")
            
            
n = 123
n2 = "123"
n3 =[1, 2, 3]

print(f"{convertion_of_input_type(n)}\n{convertion_of_input_type(n2)}\n{convertion_of_input_type(n3)}")
