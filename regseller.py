import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()

def reg_seller():
    print("1. Sell a Car")
    print("2. Talk to Buyers")
    print("3. Back")
    ch = input("What do you want to do?: ")
    print("\n--------------------------------------------\n")
    
    if(ch == '1'):
        sell()

    elif(ch == '2'):
        pass

    elif(ch == '3'):        
        return
    
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
    
    reg_seller()
    
def sell():

    print("Please fill the required details of your car")
    print("Note:- '#' means not mandotory to fill if you want")
    print("you can leave them empty by hitting enter to skip them")
    print("\n--------------------------------------------\n")

    try:
        print("Format: Company Car Model")
        print("Example: Hyundai Grand i10 Asta\n")
        name = input("Enter name of your car: ")
        print("\n--------------------------------------------\n")
        
        price = float(input("Enter price in lakhs: "))
        print("\n--------------------------------------------\n")
        
        year = int(input("Enter model year: "))
        print("\n--------------------------------------------\n")
        
        odo = int(input("Enter odometer reading: "))
        print("\n--------------------------------------------\n")
        
        print("Fuel type availabe:")
        print("1. Petrol")
        print("2. Diesel")
        print("3. CNG")
        fuel = int(input("Fuel type of your car: "))
        print("\n--------------------------------------------\n")

        if(fuel == 1):
            fuel = 'Petrol'
            
        elif(fuel == 2):
            fuel = 'Diesel'

        elif(fuel == 3):
            fuel = 'CNG'

        else:
            print("Wrong Input, Try again")
            print("\n--------------------------------------------\n")
            return
        
        print("Transmission type availabe:")
        print("1. Automatic")
        print("2. Manual")
        trans = int(input("Preferred fuel type? "))
        print("\n--------------------------------------------\n")

        if(trans == 1):
            trans = 'Automatic'
            
        elif(trans == 2):
            trans = 'Manual'

        else:
            print("Wrong Input, Try again")
            print("\n--------------------------------------------\n")
            return

    except:
        print("Wrong Input, Try again")
        print("\n--------------------------------------------\n")
        return

    else:
        pass



        
    
        
        
