from login import login
from login import password_validation

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()


def signup(a):
    global username,password
    
    fname = input("Enter your First Name :\t")
    lname = input("Enter your Last Name  :\t")
    username = input("Enter your Username:\t")
    print("Password must have 1 uppercase")
    password = input("Enter your Password:\t")
    print("\n--------------------------------------------\n")
    
    print("Validating Username....\n")
    res = email_validation()
    print("Validating Password....\n")
    res2 = password_validation(password)
    print("\n--------------------------------------------\n")


    if (res == 1 and res2 == 1):
        sql = 'insert into login values(%s,%s,%s,%s,%s)'
        if(a == 0):
            data = (fname,lname,username.lower(),password,'NO')

        else:
            data = (fname,lname,username.lower(),password,'YES')
            
        cur1.execute(sql,data)
        mycon.commit()
        print("Signup Complete")
        print("\n--------------------------------------------\n")
        ch3 = input("Do you want to login?(y/n) ")
        print("\n--------------------------------------------\n")
        if(ch3.lower() == 'y'):
            login()
            
    else:
        print("Email or Password is not valid")
        print("\n--------------------------------------------\n")
        try1 = input("Do you want to Sign Up again?(y/n) ")
        print("\n--------------------------------------------\n")
        if(try1.lower() == 'y'):
            signup(a)


def email_validation():
    a = 2
    for i in username:
        if(i == '@'):
            print("Username Validation Complete\n")
            a = 1
            break    
    return a
