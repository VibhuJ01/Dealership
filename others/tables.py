import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()

def login():
    sql = '''create table login
(f_name varchar(20) not null,
l_name varchar(20) not null,
username varchar(50) not null primary key,
password varchar(30) not null
);'''
    cur1.execute(sql)
    mycon.commit()


def seller():
    sql = '''create table seller
(f_name varchar(30) not null,
l_name varchar(30) not null,
DOB varchar(10) not null,
p_address varchar(100) not null,
username varchar(30)primary key not null,
ph_no int not null,
al_no int not null,
doc varchar(20) not null,
doc_no int not null );'''
    cur1.execute(sql)
    mycon.commit()


def car_desc():
    sql = '''create table Car_Desc(
Serial_NO int primary key,
Name varchar(30) not null,
Price float(5,2) not null,
Year int not null,
Odometer int not null, 
Fuel varchar(10) not null,
Transmission varchar(10) not null,
Mileage float(5,2),
Seats int not null,
Description varchar(300) not null,
Verified varchar(3) not null
);'''
    cur1.execute(sql)
    mycon.commit() 


def car_ver():
    sql = '''create table Car_ver(
RC_No int primary key,
Insurance_No int not null,
Insurance_Exp varchar(10) not null,
Pollution_Exp varchar(10) not null,
Seller varchar(20) not null
);'''    
    cur1.execute(sql)
    mycon.commit() 

cur1.close()
mycon.close()
print("Done")
