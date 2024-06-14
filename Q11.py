# Write a python program that generates the first n numbers in the
# Fibonacci sequence.
n=int(input("Enter thr number: "))
n1=0
n2=1
n3=n2
print(n1)
print(n2)
for i in range(n):
    print(n3)
    n1,n2=n2,n3
    n3=n1+n2


