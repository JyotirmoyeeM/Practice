"""
Write a program that uses a loop to take 3 key-value inputs from the user and create a dictionary using these keys and values.

Create an empty dictionary named my_dict.
Use for loop to iterate from 1 to 3, including 3.
Inside the loop, take inputs for key and value and store them in my_dict.
Print the updated my_dict.
"""

my_dict = {}

for i in range(3):
  key = input()
  value = input()
  my_dict[key] = value

print(my_dict)
