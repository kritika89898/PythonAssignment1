# Write a program that acts as a simple calculator. It should take two
# numbers and an operator (+, -, *, /) as input and print the result.
n1=int(input("Enter first number:"))
n2=int(input("Enter second number: "))
op=input("Enter the operator:")
if(op=="+"):
    res=n1+n2
    print(res)
elif(op=="-"):
    res=n1-n2
    print(res)
elif(op=="*"):
    res=n1*n2
    print(res)
elif(op=="/"):
    res=n1/n2
    print(res)
else:
    print("Invalid operation")
print(n1," ",op," ",n2," = ",res)