#Write a program to check if the student passed or failed his/her examination by creating a function.
# define a function named check with argument marks
def check(marks):
    # inside the function, check Pass or Fail using if...else statement
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

marks = int(input())

#call the function
check(marks)
