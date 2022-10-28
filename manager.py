from tabulate import tabulate
from manager2 import afterloginM
from sale import sale
import pandas as pd
import mysql.connector as ms

mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()


def manager(username,password):
    print('1. Manager')
    print('2. Customer')
    print('3. Logout')
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")
    
    if(ch == "1"):
        while(ch == '1'):
            print('1. Put Verified Cars on Sale')
            print('2. Add a New Manager')
            print('3. Remove a Manager')
            print('4. Diplay list of staff Members')
            print('5. Answer Queries')
            print('6. Back')
            ch2 = input("What do you want to do? ")
            print("\n--------------------------------------------\n")

            if(ch2 == "1"):
                sale()
                    
            elif(ch2 == "2"):
                display()
                add()

            elif(ch2 == "3"):
                display()
                remove()
            
            elif(ch2 == "4"):
                display()
            
            elif(ch2 == "5"):
                pass

            elif(ch2 == '6'):
                break

            else:
                print("Wrong Input")  
                print("\n--------------------------------------------\n")
            
    elif(ch == "2"):
        afterloginM(username,password)

    elif(ch == '3'):
        return 0

    else:
        print("Wrong Input")  
        print("\n--------------------------------------------\n")

    manager(username,password)

    
def add():
    u = input("Enter Username of the New Manager: ")
    print("\n--------------------------------------------\n")
    
    a = usercheck(u)
    if(a == 1):
        sql = 'update login set manager = %s where username = %s'
        data = ("YES",u)
        cur1.execute(sql,data)
        mycon.commit()

        print("Manager Successfully Added")
        print("\n--------------------------------------------\n")

    else:
        print("User doesn't Exist")
        print("\n--------------------------------------------\n")
    
        
def remove():
    u = input("Enter Username of the Manager for removal: ")
    print("\n--------------------------------------------\n")
    a = usercheck(u)
    if(a == 1):
        sql = 'update login set manager = %s where username = %s'
        data = ("NO",u)
        cur1.execute(sql,data)
        mycon.commit()

        print("Manager Successfully Removed")
        print("\n--------------------------------------------\n")

    else:
        print("User doesn't Exist")
        print("\n--------------------------------------------\n")
    

def usercheck(u):
    sql = 'select * from login'
    cur1.execute(sql)
    result = cur1.fetchall()

    for i in result:
        if(i[2] == u.lower()):
            a = 1
            return a      
    return 0
  
def display():
    print("All your staff memebers->\n")
    sql = 'select f_name,l_name,username,manager from login'
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    for i in result:
        if(i[3] == 'YES'):
            l.append(i)

    keys = ['First Name','Last Name','Username','Manager']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")

