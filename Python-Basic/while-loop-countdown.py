#Write a program to simulate a rocket launch countdown.

countdown = int(input())

elapsed = 0

while countdown >= 0:
    print(f"Time left: {countdown} seconds")
    print(f"Elapsed: {elapsed} seconds\n---")
    
    countdown -= 1
    elapsed +=1

# Print the "Liftoff!" message
print("Liftoff!")
