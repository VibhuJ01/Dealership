from tabulate import tabulate
import pandas as pd
from filters import filters
from filters import pick
from sale import integrate


def buy():
    print("1. Buy a Car")
    print("2. Talk to Sellers")
    print("3. Back")
    ch = input("What do you want to do?: ")
    print("\n--------------------------------------------\n")
    
    if(ch == '1'):
        buying()

    elif(ch == '2'):
        pass
        #Talk to sellers wala ayega
    
    elif(ch == '3'):        
        return
    
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
    
    buy()

def buying():
    df = integrate(1)
    
    #Input->
    try:
        print('1. Enter Budget')
        print('2. Any')
        ch = input("What do you want to do?: ")
        print("\n--------------------------------------------\n")
        
        if(ch == '1'):
            print("Enter Price in Lakhs")
            uprice = float(input("What's your Upper Budget? "))
            lprice = float(input("What's your Lower Budget? "))
            print("\n--------------------------------------------\n")
            df = df.loc[df['price'] <= uprice]
            df = df.loc[df['price'] >= lprice]

        elif(ch == '2'):
            pass
        else:
            print("Wrong Input")
            print("\n--------------------------------------------\n")
            return

        print('1. Enter Seat Number')
        print('2. Any')
        ch = input("What do you want to do?: ")
        
        if(ch == '1'):
            print("\n--------------------------------------------\n")
            seats = int(input("Preferred Seat Number: "))        
            df = df.loc[df['Seats'] == seats]

        elif(ch == '2'):
            pass
        else:
            print("\n--------------------------------------------\n")
            print("Wrong Input")
            print("\n--------------------------------------------\n")
            return
        
        print("\n--------------------------------------------\n")
        print("Fuel Type Availabe:")
        print("1. Petrol")
        print("2. Diesel")
        print("3. CNG")
        print("4. Any")
        fuel = int(input("Preferred Fuel Type: "))
        print("\n--------------------------------------------\n")
        
        print("Transmission Type Availabe:")
        print("1. Automatic")
        print("2. Manual")
        print("3. Any")
        trans = int(input("Preferred Transmission Type: "))

    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        return

    else:
        #Processing->
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
            print("We dont have Cars of that Specification")
            print("\n--------------------------------------------\n")
            return
    
        printing(df)
        fil(df)

def fil(df):

    print("1. Pick a Car")
    print("2. Apply Filters")
    print("3. Back")
    ch = input("What do you wanna do? ")
        
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
