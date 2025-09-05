#write a program that displays True if the number is even and False if it's odd.
while True:
    user_input = input("Enter a number (or type 'stop'/'end' to exit): ")
    
    # Check if user wants to exit
    if user_input.lower() in ["stop", "end"]:
        print("\nProgram terminated.")
        break
    
    try:
        number = int(user_input)
        
        if number == 0 or number == 1:
            print(f"This {number} is invalid input")
        else:
            if number % 2 == 0 :
                print(number, "Even", number % 2==0)
            else:
                print(number, "Odd", number % 2==0)
    except ValueError:
        print("Please enter a valid number or 'stop'/'end' to exit.")
