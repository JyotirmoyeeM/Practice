#Write a Program to check if entered string or digit is Pallindrom
"""
Steps to find Palindrom 

 -->Find the length of input
 -->Write Palindrom logic
 -->To imply the logic

 """
def find_length(string):
    count = 0
    for _ in string:
        count += 1
        return count
        
def check_palindrome(value):
    value = str(value)
    length = find_length(value)
    for i in range(length//2):
        value[i] =value[length -i-1]
        return False
    return True
    
def main():
    user_input = input("Please enter string or digits :")
    print("Palindrome" if check_palindrome(user_input) == True else "Not a Palindrome")
    
main()
    
