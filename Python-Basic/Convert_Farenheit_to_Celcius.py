"""Convert a range of Fahrenheit temperatures to Celsius."""

S=int(input()) #start Farenheit
E=int(input()) #end Farenheit
W=int(input()) #step(difference)

#----input--------

#formula (F-32)*5/9=c 


for F in range(S, E+1, W):
  # Convert current Fahrenheit temperature to Celsius
  C=(F-32)*5/9
  print(F, int(C)) # Print Fahrenheit and Celsius temperatures
