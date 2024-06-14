# Write a program that reads data from a CSV file and prints it to the
# console
import pandas as pd
data=pd.read_csv("monthly sale.csv")
print(data.to_string())