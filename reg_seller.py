import mysql.connector as ms
from tabulate import tabulate
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()
from car_ver import car_ver,sold

def reg_seller(username):
    sql = "select * from car_desc"
    cur1.execute(sql)
    result = cur1.fetchall()
    s = len(result)
    print("1. Sell a Car")
    print("2. Verify Car")
    print("3. See Details of your Cars")
    print('4. Mark your Car as Sold')
    print("5. Talk to Buyers")
    print("6. Back")
    ch = input("What do you want to do?: ")
    print("\n--------------------------------------------\n")
    
    if(ch == '1'):
        sell(username,s)

    elif(ch == '2'):        
        car_ver(username)

    elif(ch == "3"):
        display(username)

    elif(ch == '4'):
        a = display_unsold(username)
        if(a == 1):
            sold(username)
        
    elif(ch == '5'):
        pass
  
    elif(ch == '6'):
        return
    
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
    
    reg_seller(username)
    
def sell(username,s):

    print("Please fill the required details of your car")
    print("\n--------------------------------------------\n")

    try:
        print("Format: Company Car Model")
        print("Example: Hyundai Grand i10 Asta\n")
        name = input("Enter name of your car: ")
        print("\n--------------------------------------------\n")
        
        price = float(input("Enter price (in lakhs): "))
        print("\n--------------------------------------------\n")
        
        year = int(input("Enter Model Year: "))
        print("\n--------------------------------------------\n")
        
        odo = int(input("Enter Odometer Reading: "))
        print("\n--------------------------------------------\n")

        
        print("Fuel type availabe:")
        print("1. Petrol")
        print("2. Diesel")
        print("3. CNG")
        fuel = int(input("Fuel type of your car: "))
        if(fuel == 1):
            fuel = 'Petrol'
            
        elif(fuel == 2):
            fuel = 'Diesel'

        elif(fuel == 3):
            fuel = 'CNG'

        else:
            print("\n--------------------------------------------\n")
            print("Wrong Input, Try again")
            print("\n--------------------------------------------\n")
            return
        print("\n--------------------------------------------\n")

        print("Transmission type availabe:")
        print("1. Automatic")
        print("2. Manual")
        trans = int(input("Transmission type of your car: "))

        if(trans == 1):
            trans = 'Automatic'
            
        elif(trans == 2):
            trans = 'Manual'

        else:
            print("\n--------------------------------------------\n")
            print("Wrong Input, Try again")
            print("\n--------------------------------------------\n")
            return
        print("\n--------------------------------------------\n")

        mil = float(input("Average Mileage of your car: "))
        print("\n--------------------------------------------\n")

        seats = int(input("Number of seats in your car: "))
        print("\n--------------------------------------------\n")

        descr = input("Description of the Car: ")
        print("\n--------------------------------------------\n")
        
        ch = input("Are you sure that the above details are correct?(y/n) ")
        if(ch.lower() == "y"):
            sql = 'insert into car_desc values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            data = (s,username.lower(),name,price,year,odo,fuel,trans,mil,seats,descr,"NO",'NO','NO')
            cur1.execute(sql,data)
            mycon.commit()

    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input, Try again")
        print("\n--------------------------------------------\n")
        return

    else:
        print("\n--------------------------------------------\n")
        print("Car Registration Complete")
        print("\n--------------------------------------------\n") 
        car_ver(username) 

def display(username):
    sql = "select * from car_desc"
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    for i in result:
        if(i[1] == username.lower()):
            l.append(i)

    if(len(l) == 0):
        print("You haven't Registered any Car")
        print("\n--------------------------------------------\n")
        return
    
    print("All of your Cars are Listed Below:\n")
    keys = ['Serial No', 'Username', 'Name','Price','Model','Odometer','Fuel','Transmission','Mileage','Seats','Description','Verified','On_sale','Sold']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")


def display_unsold(username):
    sql = "select * from car_desc"
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    for i in result:
        if(i[1] == username.lower() and i[13] == 'NO'):
            l.append(i)

    if(len(l) == 0):
        print("All your Cars are Either Sold or You haven't Registered any Car")
        print("\n--------------------------------------------\n")
        return 0
    
    print("All of your Unsold Cars are Listed Below:\n")
    keys = ['Serial No', 'Username', 'Name','Price','Model','Odometer','Fuel','Transmission','Mileage','Seats','Description','Verified','On_sale','Sold']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")
    return 1
