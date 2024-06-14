# Write a python program that removes all punctuation from a given string
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
d=input("Enter the text: ")
result=""
for char in d:
    if char not in punctuation:
        result += char

print(result)

