import datetime
import pandas as pd
from tabulate import tabulate

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()


def wishlist(username,df,a):

    sql = 'select * from wishlist'
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    
    for i in result:
        if(i[1] == username):
            l.append(i)

    if(len(l) == 0):
        print('Your Wishlist is Empty')
        print("\n--------------------------------------------\n")
        return

    printing(l,df,a,username)
    
def addW(car,username):
    x = datetime.datetime.now() 

    if(car[0] <= 19997):
        s = 'vibhu@gmail.com'

    else:
        sql = 'select seller from ins where serial_no = ' + str(car[0])
        cur1.execute(sql)
        result = cur1.fetchall()
        s = result[0][0]
        
     
    sql = 'insert into wishlist(username,seller,car_no,car_name) values(%s,%s,%s,%s)'
    data = (username,s,int(car[0]),car[1])
    cur1.execute(sql,data)
    mycon.commit()
    print('Car has been Successfully Added in your Wishlist')
    print("\n--------------------------------------------\n")
    
def printing(l,df,a,username):
    
    keys =  ['Serial_No','Username','Seller','Car_No','Car_Name']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")
    
    if(a == 1):
        message(l,df,username)
        
def message(l,df,username):

    try:
        ch = int(input('Enter Serial Number: '))
        print("\n--------------------------------------------\n")
        for i in l:
            if(i[0] == ch):
                break

        else:
            print("Serial Number is not Present")
            print("\n--------------------------------------------\n")
            return
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input, Try Again")
        print("\n--------------------------------------------\n")
        return

    else:
        ser = i[3]
        receiver = i[2]
        print('Details of the Car')
        print(df.loc[ser])
        print("\n--------------------------------------------\n")
        sql = 'select * from talk'
        cur1.execute(sql)
        result = cur1.fetchall()

        print("Just press 'Enter' to stop Messaging")
        print("\n--------------------------------------------\n")
        
        if(len(result) == 0):

            sql = 'insert into talkS(car_no,sender) values(%s,%s)'
            data = (ser,receiver)
            cur1.execute(sql,data)
            mycon.commit()
            
        else:
            for i in result:
                if(i[0] == ser and i[1] == username):
                    print(i[3],'\n')
                    
                elif(i[0] == ser and i[2] == username):
                    print("\t\t\t\t\t",i[3],'\n')
                    
        
        while(True):  
            mess = input(">>> ")
            
            if(mess == ''):
                print("\n--------------------------------------------\n")
                break

            else:
                sql = 'insert into talk values(%s,%s,%s,%s)'
                data = (ser,username,receiver,mess)
                cur1.execute(sql,data)
                mycon.commit()
                print('\n',mess,'\n')
            
    


def messageS(username):
    
    sql = 'select * from talkS where sender = %s'
    data = [username]
    cur1.execute(sql,data)
    result = cur1.fetchall()
    if(len(result) == 0):
        print('No buyers Yet')
        print("\n--------------------------------------------\n")
        return
    keys =  ['Serial_No','Car_No','Seller']
    print(tabulate(result, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")

    try:
        ch = int(input('Enter Serial Number: '))
        print("\n--------------------------------------------\n")
        for i in result:
            if(i[0] == ch):
                break

        else:
            print("Serial Number is not Present")
            print("\n--------------------------------------------\n")
            return
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input, Try Again")
        print("\n--------------------------------------------\n")
        return

    else:
        sql = 'select * from talk where car_no = %s and (sender = %s or receiver = %s)'
        data = (i[1],username,username)
        cur1.execute(sql,data)
        result = cur1.fetchall()
        receiver = i[2]
        ser = i[1]

        print("Just press 'Enter' to stop Messaging")
        print("\n--------------------------------------------\n")
        
        for i in result:
            if(i[1] == username):
                print(i[3],'\n')
                
            elif(i[2] == username):
                print("\t\t\t\t\t",i[3],'\n')
        
        while(True):  
            mess = input(">>> ")
            
            if(mess == ''):
                print("\n--------------------------------------------\n")
                break

            else:
                sql = 'insert into talk values(%s,%s,%s,%s)'
                data = (ser,username,receiver,mess)
                cur1.execute(sql,data)
                mycon.commit()
                print('\n',mess,'\n')
            

