from tabulate import tabulate
import pandas as pd

def filters(df):
    print("We provide the following Filters:")
    print("1. Minimum Mileage")
    print("2. Model Year")
    print("3. Odometer Reading")
    print("4. Stop Applying")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    if(ch == "1"):
        mil = input("What Mileage you are looking for? ")
        df = df.loc[df['Mileage'] >= mil]
        
    elif(ch == "2"):
        mod = float(input("What Model Year you are looking for? "))
        df = df.loc[df['year'] >= mod]

    elif(ch == "3"):
        odo = input("Maximum Odometer Reading? ")     
        df = df.loc[df['Odometer_Reading'] <= odo]

    elif(ch == "4"):
        return

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")  
        filters(df)
        
    print("\n--------------------------------------------\n")    
    printing(df)
    filters(df)

def pick(df):
    ch = int(input("Serial Id of car of your choice: "))
    print("\n--------------------------------------------\n")
    print(df.loc[ch])
    print("\n--------------------------------------------\n")
    ch = input("Do wanna buy this car?(y/n) ")
  

def printing(df):
    print("\n--------------------------------------------\n")
    print(tabulate(df, headers = 'keys', tablefmt = 'pretty'))
    print("\n--------------------------------------------\n")


