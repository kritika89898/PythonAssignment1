# Write a program in python that checks if a string starts with a given prefix
# or ends with a given suffix.
text=input("Enter the text:")
prefix=input("Enter the prefix to be checked:")
suffix=input("Enter the suffix to be checked:")
pre=text.startswith(prefix)
suf=text.endswith(suffix)
if pre==True:
    print("The text has prefix",prefix)
else:
    print("The given prefix is not present")
if suf==True:
    print("The text has suffix",suffix)
else:
    print("The given suffix is not present")