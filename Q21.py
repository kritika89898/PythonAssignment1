# Write a python program that counts the occurrences of a specific element
# in a list.
L1 = []
n = int(input("Enter the number of elements in the list:"))
for i in range(1,n+1):
    print("Enter the ",i," element:")
    ele=(input())
    L1.append(ele)
print("List: ",L1)
element=input("Enter the element to count the occurence:")
count = 0
for item in L1:
    if item == element:
        count += 1
print(count)