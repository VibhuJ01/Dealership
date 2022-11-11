import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()
from tabulate import tabulate

def car_ver(username,result):

    ch = input('Do you want to Verify any Car now?(y/n) ')
    if(ch == 'y'):
        print("\n--------------------------------------------\n")

        try:
            s = int(input("Enter Serial Number of the Car You want to Register: "))
        except:
            print("\n--------------------------------------------\n")
            print("Wrong Input, Try again")
            print("\n--------------------------------------------\n")
            return

        
        for i in result:
            if(s == i[0]):
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

            
    

def ver(s):
    
    print("To put your Car up for Sale,")
    print("You have to Verify your Car")
    print("\n--------------------------------------------\n")

   
    try:
        rc = int(input("Enter your RC Number: "))
        print("\n--------------------------------------------\n")

        ins = int(input("Enter your Insurrance Number: "))
        print("\n--------------------------------------------\n")

        ins_exp = input("Enter your Insurrance Expiry Date: ")
        print("\n--------------------------------------------\n")

        pol_exp = input("Enter your Pollution Expiry Date: ")
        print("\n--------------------------------------------\n")

        sel = input("First seller, Second seller etc: ")
        print("\n--------------------------------------------\n")
        
        ch = input('Are you sure above Details are Correct?(y/n) ')
        if(ch == 'y'):
            sql = 'insert into car_ver values (%s,%s,%s,%s,%s,%s)'
            data = (s,rc,ins,ins_exp,pol_exp,sel)
            cur1.execute(sql,data)
            mycon.commit()       
            
        
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input, Try again")
        print("\n--------------------------------------------\n")
        return

    else:
        sql = '''update car_desc
                set Verified = %s
                where Serial_NO = %s'''
        data = ('YES',s)
        cur1.execute(sql,data)
        mycon.commit()
            
        print("\n--------------------------------------------\n")
        print("Car Verification Complete")
        print("\n--------------------------------------------\n")

def sold(username):

    try:
        ch = int(input("Serial Id of Car of your Choice: "))
        print("\n--------------------------------------------\n")
        ch1 = input("Are you sure?(y/n)")
        print("\n--------------------------------------------\n")
        if(ch1.lower() == 'y'):
            pass
            
        elif(ch1.lower() == 'n'):
            return
        
        else:
            wrong
            
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        return

    else:
        sql = '''update car_desc
                set Sold = %s
                where Serial_NO = %s'''
        data = ('YES',ch)
        cur1.execute(sql,data)
        mycon.commit()
        print("\n--------------------------------------------\n")
        print("Your Car has been marked Sold")
        print("\n--------------------------------------------\n")
            
