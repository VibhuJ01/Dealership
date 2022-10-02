from tabulate import tabulate
import pandas as pd
from filters import filters
from filters import pick

def buy():
    df = pd.read_csv("dataset.csv")
    df = df.dropna()
    convert_dict = {'Mileage': float}
 
    df = df.astype(convert_dict)
    
    #Input->
    try:
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

    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        return

    else:
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
            print("\n--------------------------------------------\n")
            print("We dont have cars of that specification")
            print("\n--------------------------------------------\n")
            return
    
        printing(df)
        fil(df)

def fil(df):

    print("1. Pick a Car")
    print("2. Apply Filters")
    print("3. Back")
    ch = input("What do you wanna do? ")
    print("\n--------------------------------------------\n")
        
    if(ch == "1"):
        printing(df)
        car,a = pick(df)
        
        if(a == 0):
            fil(df)
        else:
            pass
        # yaha pe ab seller ko msg karna hai
        
    elif(ch == "2"):
        df = filters(df)
        if(len(df) == 0):
            return
        
        fil(df)

    elif(ch == "3"):
        print("\n--------------------------------------------\n")
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        fil(df)

        
def printing(df):
    print("\n--------------------------------------------\n")
    print(tabulate(df, headers = 'keys', tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")
