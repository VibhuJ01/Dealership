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
            print('6. See all the Queries')
            print('7. Back')
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
                ser,i = displayA(0)
                if(ser != -1):
                    answer(ser,i)

            elif(ch2 == '6'):
                displayA(1)
                
            elif(ch2 == '7'):
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


def displayA(a):
    sql = 'select * from queries'
    cur1.execute(sql)
    result = cur1.fetchall()

    if(a == 1):
        print("All the Available Queries/Complaints->\n")
        keys = ['Serial_No','Username','Type','Subject','Query','Answer','Feedback']
        print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))
        print("\n--------------------------------------------\n")
        
    elif(a == 0):
        l = []
        for i in result:
            if(i[5] == 'We will reply soon.'):
                l.append(i)

        if(len(l) == 0):
            print('No Queries Available')
            print("\n--------------------------------------------\n")
            return -1,0
        
        print("All the Available Queries/Complaints->\n")
        keys = ['Serial_No','Username','Type','Subject','Query','Answer','Feedback']
        print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
        print("\n--------------------------------------------\n")

        try:
            ser = int(input("Enter the Serail Number of Query: "))
            print("\n--------------------------------------------\n")
            
            for i in l:
                if(i[0] == ser):
                    return ser,i
            else:
                print('Serial Number is not Available')
                print("\n--------------------------------------------\n")
                return -1,0
                
        except:
            print("\n--------------------------------------------\n")
            print("Wrong Input")
            print("\n--------------------------------------------\n")

    
def answer(ser,i):
    l = []
    l.append(i)
    keys = ['Serial_No','Username','Type','Subject','Query','Answer','Feedback']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")
    
    ans = input("Enter your Reply: ")
    
    sql = '''update queries
             set answer = %s
             where serial_no = %s'''

    data = (ans,i[0])
    cur1.execute(sql,data)
    mycon.commit()

    print("\n--------------------------------------------\n")
    print("The Question is Answered Successfully")
    print("\n--------------------------------------------\n")
    
