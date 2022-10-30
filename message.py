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

    printing(l,df,a)
    
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
    
    


def printing(l,df,a):
    
    keys =  ['Serial_No','Username','Seller','Car_No','Car_Name']
    print("\n--------------------------------------------\n")
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")
    
    if(a == 1):
        message()
        
def message():
    
