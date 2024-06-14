# Write a program that takes a string input from the user and writes it to a
# text file.
import keyword
text=input("Enter the text: ")
file1=open("D:/myfile.txt","w")
print(text,file=file1)