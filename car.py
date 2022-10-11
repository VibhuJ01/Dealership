import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()

def car_ver():
    pass



def ver():
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
