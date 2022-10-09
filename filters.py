from tabulate import tabulate
import pandas as pd
    
def filters(df):
    print("\n--------------------------------------------\n")
    print("We provide the following Filters:")
    print("1. Minimum Mileage")
    print("2. Model Year")
    print("3. Odometer Reading")
    print("4. Stop Applying")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    if(ch == "1"):
        mil = float(input("What Mileage you are looking for?(Km/L) "))
        df = df.loc[df['Mileage'] >= mil]
        
    elif(ch == "2"):
        mod = float(input("What Model Year you are looking for? "))
        df = df.loc[df['year'] >= mod]

    elif(ch == "3"):
        odo = input("Maximum Odometer Reading? ")     
        df = df.loc[df['Odometer_Reading'] <= odo]

    elif(ch == "4"):
        return df

    else:
        print("Wrong Input")
        df = filters(df)
        

    if(len(df) == 0):
            print("\n--------------------------------------------\n")
            print("We dont have cars of that specification")
            return df
        
    printing(df)
    df = filters(df)
    return df

def pick(df):

    try:
        ch = int(input("Serial Id of car of your choice: "))

    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        return "No",0

    else:
        
        if(ch in df["Serial_Id"]):
            print("\n--------------------------------------------\n")
            print(df.loc[ch])
            print("\n--------------------------------------------\n")
            ch1 = input("Do wanna buy this car?(y/n) ")
            print("\n--------------------------------------------\n")
            if(ch1.lower() == "y"):
                a = df.loc[ch]
                return a,1

            else:
                return "No",0
        else:
            print("\n--------------------------------------------\n")
            print("Wrong Input, Try Again")
            print("\n--------------------------------------------\n")
            return "No",0
        
    

def printing(df):
    print("\n--------------------------------------------\n")
    print(tabulate(df, headers = 'keys', tablefmt = 'pretty', showindex = False))

