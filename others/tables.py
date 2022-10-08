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
doc_no int not null );'''
    cur1.execute(sql)
    mycon.commit()


def car():
    sql = '''create table Car_Desc(
name varchar(30) not null,
price float(5,2) not null,
year int not null,
odo int not null, 
fuel varchar(10) not null,
transmission varchar(10) not null,
Mileage float(5,2),
Engine_number int,
Horse_Power int,
Seats int not null,
Description varchar(300) not null,
Mess varchar(300) not null
);'''
    cur1.execute(sql)
    mycon.commit() 

car()

cur1.close()
mycon.close()
print("Done")
