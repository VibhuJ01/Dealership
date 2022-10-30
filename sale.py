from tabulate import tabulate
import mysql.connector as ms
import pandas as pd

mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()


def sale():
    sql = 'select * from car_desc'
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    for i in range(len(result)):
        if(result[i][11] == 'YES' and result[i][13] == 'NO' and result[i][12] == 'NO'):
            l.append(i)

    if(len(l) == 0):
        print('All Cars are Put on sale')
        print("\n--------------------------------------------\n")
        return

    res = []
    sql = 'select c.serial_no,c.name,c.price,c.year,c.odometer,c.fuel,c.transmission,c.Description,v.rc_no,v.Insurance_No,v.seller from car_desc c join car_ver v where c.serial_no = v.serial_no'
    cur1.execute(sql)
    result = cur1.fetchall()

    for i in range(len(result)):
        if(i in l):
            res.append(result[i])
    
    keys = ['Serial No','Name','Price','Model Year','Odometer','Fuel','Transmission','Description','RC NO',"Insurance No",'Seller']
    print(tabulate(res, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")

    while(True):
        ch = input('Do you want to put any Car on Sale?(y/n) ')
        print("\n--------------------------------------------\n")
        if(ch == 'y'):
            try:
                ch2 = int(input('Serial Number of a car you want to put on sale: '))
                print("\n--------------------------------------------\n")
                
            except:
                print("\n--------------------------------------------\n")
                print('Wrong Input')
                print("\n--------------------------------------------\n")
                
            else:
                if(ch2 not in l):
                    print("Serial Number is not there")
                    print("\n--------------------------------------------\n")
                    break
                
                putonsale(ch2)
                print("\n--------------------------------------------\n")
                break
                

        elif(ch == 'n'):
            print("\n--------------------------------------------\n")
            break

        else:
            print('Wrong Input')
            print("\n--------------------------------------------\n")

def putonsale(ser):
    
    sql = '''select serial_no,name,price,year,odometer,
            fuel,transmission,mileage,seats from car_desc'''
    cur1.execute(sql)
    result = cur1.fetchall()

    for i in range(len(result)):
        if(result[i][0] == ser):
            break

    i = result[i]
    ser = integrate(0)
    sql = 'insert into ins values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    data = (ser,i[1],i[2],i[3],i[4],i[5],i[6],i[7],0,i[8])
    cur1.execute(sql,data)
    mycon.commit()

    sql = '''update car_desc
             set on_sale = %s
             where serial_no = %s'''
    data = ('YES',i[0])
    cur1.execute(sql,data)
    mycon.commit()
    print('Car was Successfully Put on Sale')


def integrate(a):
    df = pd.read_csv("dataset.csv")
    

    sql = 'select serial_no,name,price,year,odo,fuel,trans,mil,hp,seats from ins'
    cur1.execute(sql)
    result = cur1.fetchall()

    if(a == 0):
        return len(df)+len(result)


    for i in result:
        df.loc[len(df.index)] = i
        
    df = df.dropna()
    convert_dict = {'Mileage': float}
    df = df.astype(convert_dict)
    return df
    
    
