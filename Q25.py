# Write a program that copies the contents of one text file to another.
file1=open("D:/myfile.txt",'r')
c=file1.read()
file2=open("D:/mynewtxtdata.txt","w")
print(c,file=file2)