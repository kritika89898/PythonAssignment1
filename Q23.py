# Write a program that converts temperature from Celsius to Fahrenheit
# and vice versa based on user input.
temp=int(input("Enter the temperature in Fahrenheit or Celsius:"))
ch=input("Enter F/C for above temperature:")
if(ch=="F"):
    C=((temp-32)*5)/9
    print("The temperature in celsius:",C,"°C")
elif(ch=="C"):
    F=((temp*9)/5)+32
    print("The temperature in Fahrenheit:",F,"°F")
else:
    print("Invalid temperature")