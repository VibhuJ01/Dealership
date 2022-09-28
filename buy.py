from tabulate import tabulate
import pandas as pd
from filters import filters
from filters import pick

df = pd.read_csv("dataset.csv")
df = df.dropna()

def buy():
    global df
    #Input->
    print("Enter Price in Lakhs")
    uprice = float(input("whats your upper budget? "))
    lprice = float(input("whats your lower budget? "))
    print("\n--------------------------------------------\n")
    
    seats = int(input("Preferred seat no? "))

    print("\n--------------------------------------------\n")
    print("Fuel type availabe:")
    print("1. Petrol")
    print("2. Diesel")
    print("3. CNG")
    print("4. Any")
    fuel = int(input("Preferred fuel type? "))
    print("\n--------------------------------------------\n")
    
    print("Transmission type availabe:")
    print("1. Automatic")
    print("2. Manual")
    print("3. Any")
    trans = int(input("Preferred fuel type? "))
    

    #Processing->
    df = df.loc[df['price'] <= uprice]
    df = df.loc[df['price'] >= lprice]
    df = df.loc[df['Seats'] == seats]

    if(fuel == 1):
        df = df.loc[df['fuel'] == 'Petrol']
        
    elif(fuel == 2):
        df = df.loc[df['fuel'] == 'Diesel']

    elif(fuel == 3):
        df = df.loc[df['fuel'] == 'CNG']

    if(trans == 1):
        df = df.loc[df['transmission'] == 'Automatic']
        
    elif(trans == 2):
        df = df.loc[df['transmission'] == 'Manual']

    if(len(df) == 0):
        print("We dont have cars of that specification")
        print("\n--------------------------------------------\n")
        return
    
    printing(df)
    fil()

def fil():
    global df

    print("1. Pick a Car")
    print("2. Apply Filters")
    print("3. Back")
    ch = input("What do you wanna do? ")
    print("\n--------------------------------------------\n")
        
    if(ch == "1"):
        a = pick(df)
        
        if(a == 0):
            fil()
        else:
            return
        
    elif(ch == "2"):
        filters(df)
        fil()

    elif(ch == "3"):
        print("\n--------------------------------------------\n")
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        fil()
    
def printing(df):
    print("\n--------------------------------------------\n")
    print(tabulate(df, headers = 'keys', tablefmt = 'pretty'))
    print("\n--------------------------------------------\n")

