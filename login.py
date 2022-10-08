from buy import buy
from seller import seller

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()


def login():
    username = input("Enter your username:\t")
    password = input("Enter your password:\t")
    print("\n--------------------------------------------\n")
    sql = "select * from login"
    cur1.execute(sql)
    result = cur1.fetchall()
    flag = 0
    for i in result:
        if(i[2] == username.lower() and i[3] == password):
            print('Login is succesful')
            print("\n--------------------------------------------\n")
            flag = 1
            afterlogin(username,password)

            
    if(flag != 1):
        print("Invalid username or password")
        print("\n--------------------------------------------\n")
        
        ch5 = input("Do you want to login again?(y/n) ")
        print("\n--------------------------------------------\n")
        if(ch5 == 'y'):
            login()  
    
def afterlogin(username,password):

    print("1. Buyer")
    print("2. Seller")
    print("3. Change Password")
    print("4. Logout")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    if(ch == '1'):
        buy()

    elif(ch == "2"):
        seller(username)

    elif(ch == "3"):
        changepass(username,password)
        
    elif(ch == "4"):
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    afterlogin(username,password)

def changepass(username,password):
    
    oldpass = input("Enter old password:\t")
    if(oldpass == password):
        newpass = input("Enter new password:\t")
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
            print("Changing password....")
            print("Your new password is ",newpass)
            print("\n--------------------------------------------\n")

        else:
            print("New Password is not valid")
            print("\n--------------------------------------------\n")
            
    else:
        print("\n--------------------------------------------\n")
        print("Your Old password did not match")
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
