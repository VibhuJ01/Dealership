import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()
from tabulate import tabulate

def car_ver(username):
    
    sql = "select * from car_desc"
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    for i in result:
        if(i[1] == username.lower() and i[11] == "NO"):
            l.append(i)

    if(len(l) == 0):
        print("You have No Pending Unverified Car")
        print("\n--------------------------------------------\n")
        return
    
    print("All of your Unverified Cars are Listed Below:\n")
    keys = ['Serial No', 'Username', 'Name','Price','Model','Odometer','Fuel','Transmission','Mileage','Seats','Description','Verified']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")

    try:
        ch = input('Do you want to Verify any Car now?(y/n) ')
        if(ch == 'y'):
            print("\n--------------------------------------------\n")
            s = int(input("Enter Serial Number of the Car You want to Register: "))

            for i in result:
                if(int(s) == i[0]):
                    print("\n--------------------------------------------\n")
                    ver(s)
                    break

            else:
                print("\n--------------------------------------------\n")
                print("Serial number is not there")
                print("\n--------------------------------------------\n")
                
            
        elif(ch == 'n'):
            print("\n--------------------------------------------\n")

        else:
            print("\n--------------------------------------------\n")
            print("Wrong Input, Try again")
            print("\n--------------------------------------------\n")
        
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input, Try again")
        print("\n--------------------------------------------\n") 


def ver(s):
    print("To put your Car up for Sale,")
    print("You have to Verify your Car")
    print("\n--------------------------------------------\n")

    try:
        rc = int(input("Enter your RC Number: "))
        print("\n--------------------------------------------\n")
        
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input, Try again")
        print("\n--------------------------------------------\n")
        return

    else:
        print("\n--------------------------------------------\n")
        print("Car Verification Complete")
        print("\n--------------------------------------------\n")
