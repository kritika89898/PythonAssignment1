# Write a python program that checks if two strings are anagrams of each
# other
t1=input("Enter first string: ")
t2=input("Enter second string: ")
a=t1.lower()
b=t2.lower()
L1=set(a)
L2=set(b)
if(L1==L2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")