from buy import buy
from seller import seller
from manager import manager
from query import query

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()


def login():
    username = input("Enter your Username:\t")
    password = input("Enter your Password:\t")
    print("\n--------------------------------------------\n")
    sql = "select * from login"
    cur1.execute(sql)
    result = cur1.fetchall()
    flag = 0
    for i in result:
        if(i[2] == username.lower() and i[3] == password):
            print('Login is Succesful')
            print("\n--------------------------------------------\n")
            flag = 1
            if(i[4] == 'YES'):
                manager(username,password)
            else:
                afterlogin(username,password)
            break
            
    if(flag != 1):
        print("Invalid Username or Password")
        print("\n--------------------------------------------\n")
        
        ch5 = input("Do you want to login again?(y/n) ")
        print("\n--------------------------------------------\n")
        if(ch5 == 'y'):
            login()  
    
def afterlogin(username,password):

    print("1. Buyer")
    print("2. Seller")
    print('3. Queries/Complaints')
    print("4. Change Password")
    print("5. Logout")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    if(ch == '1'):
        buy()

    elif(ch == "2"):
        seller(username)

    elif(ch == '3'):
        query(username)
        
    elif(ch == "4"):
        changepass(username,password)
        
    elif(ch == "5"):
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    afterlogin(username,password)

def changepass(username,password):
    
    oldpass = input("Enter Old Password:\t")
    if(oldpass == password):
        newpass = input("Enter New Password:\t")
        print("Password should have 1 uppercase")
        print("\n--------------------------------------------\n")
        print("Validating Password....\n")
        print("\n--------------------------------------------\n")
        a = password_validation(newpass)
        if(a == 1):
            sql = '''update login 
                    set password = %s
                    where username = %s'''
            data = (newpass,username)
            cur1.execute(sql,data)
            mycon.commit()
            print("\n--------------------------------------------\n")
            print("Changing Password....")
            print("Your New Password is ",newpass)
            print("\n--------------------------------------------\n")

        else:
            print("New Password is not Valid")
            print("\n--------------------------------------------\n")
            
    else:
        print("\n--------------------------------------------\n")
        print("Your Old password did not Match")
        print("\n--------------------------------------------\n")
        ch = input("Do you want to try again?(y/n) ")
        print("\n--------------------------------------------\n")

        if(ch.lower() == "y"):
            changepass(username,password)
            

        elif(ch.lower() != "n"):
            print("Wrong Input")
            print("\n--------------------------------------------\n")

def password_validation(password):
    a = 2
    for i in password:
        if(i.isupper() == True):
            print("Password Validation Complete")
            a = 1
            break
    return a
