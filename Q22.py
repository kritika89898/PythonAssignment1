# Write a python program that returns the minimum and maximum values
# in a list of numbers
L1 = []
n = int(input("Enter the number of elements in the list:"))
for i in range(1,n+1):
    print("Enter the ",i," element:")
    ele=int(input())
    L1.append(ele)
print("List: ",L1)
print("The maximum value is:",max(L1))
print("The minimum value is:",min(L1))



