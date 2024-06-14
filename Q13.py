# Write a program that asks the user for their birth year and calculates their
# age.
import datetime
y=int(input("Enter the birth date year:"))
m=int(input("Enter the birth date month:"))
d=int(input("Enter the birth date day:"))
date=datetime.date(y,m,d)
print("Your D.O.B:",date)
today=datetime.date.today()
print("Today's date:",today)
age=today.year-date.year
print("Age:",age)
