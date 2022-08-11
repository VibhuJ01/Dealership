from tabulate import tabulate
import pandas as pd

def filters(df):
    print("We provide the following Filters:")
    print("1. Mileage")
    print("2. Model Year")
    print("3. Odometer Reading")

    




def pick(df):
    ch = int(input("Serial Id of car of your choice: "))
    print("\n--------------------------------------------\n")
    print(df.loc[ch])
    print("\n--------------------------------------------\n")
    ch = input("Do wanna buy this car?(y/n) ")
  

def printing():
    
    print(tabulate(df, headers = 'keys', tablefmt = 'pretty'))
    print("\n--------------------------------------------\n")

