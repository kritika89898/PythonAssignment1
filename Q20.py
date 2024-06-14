# Write a python program that takes a list of numbers and returns their sum.
L1 = []
n = int(input("Enter the number of elements in the list:"))
for i in range(1,n+1):
    print("Enter the ",i," element:")
    ele=int(input())
    L1.append(ele)
print("List: ",L1)
Sum = 0
for i in L1:
    Sum = Sum + i
print("The Sum of elements of list:",Sum)

# or print(sum(L1))