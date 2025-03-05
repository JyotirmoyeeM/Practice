"""Write a program to print the first x terms of the mathematical series 3N + 2 which are not multiples of 4.

The series is defined as:
=;'./
T(N) = 3N + 2, where N is a positive integer starting from 1. Your task is to print the first x terms of this series, but you should exclude any term that is a multiple of 4."""


X=int(input())

count=0
n=1
while count <x: #count has to be less than the terms the user inputted
    term=3*n+2 # Calculate the current term
    if term%4!=0: #the condition that it should not be divisible by 4
        print(term, end=" ")

        count+=1
    n+=1
