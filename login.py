from buy import buy

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
        if(i[2] == username and i[3] == password):
            print('Login is succesful')
            print("\n--------------------------------------------\n")
            flag = 1
            afterlogin()

            
    if(flag != 1):
        print("Invalid username or password")
        print("\n--------------------------------------------\n")
        
        ch5 = input("Do you want to login again?(y/n) ")
        
        if(ch5 == 'y'):
            login()  

def afterlogin():

    print("1. Buy a car")
    print("2. Sell a car")
    print("3. Logout")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    if(ch == '1'):
        buy()

    elif(ch == "2"):
        pass

    elif(ch == "3"):
        return
        
    else:
        print("Wrong Input")

    afterlogin()
