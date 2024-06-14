# Write a python program that calculates the sum of the digits of a given
# number.
n=int(input("Enter a number: "))
Sum=0
while(True):
    if((n/10)!=0):
        digit=n%10
        n=int(n/10)
        Sum=Sum+digit

    else:
        print("The sum of the digits of the number is:",Sum)
        break
