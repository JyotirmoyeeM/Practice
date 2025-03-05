"""Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
Hint : Use type casting""""

S=int(input()) #start Farenheit
E=int(input()) #end Farenheit
W=int(input()) #step(difference)

#----input--------

#formula (F-32)*5/9=c 


for F in range(S, E+1, W):
  # Convert current Fahrenheit temperature to Celsius
  C=(F-32)*5/9

print(F, C) # Print Fahrenheit and Celsius temperatures
