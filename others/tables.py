import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()

def login():
    sql = '''create table login
            (f_name varchar(20) not null,
            l_name varchar(20) not null,
            username varchar(50) not null primary key,
            password varchar(30) not null,
            manager varchar(3)
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
            Username varchar(30) not null,
            Name varchar(30) not null,
            Price float(5,2) not null,
            Year int not null,
            Odometer int not null, 
            Fuel varchar(10) not null,
            Transmission varchar(10) not null,
            Mileage float(5,2),
            Seats int not null,
            Description varchar(300) not null,
            Verified varchar(3) not null,
            On_Sale varchar(3) not null,
            Sold varchar(3) not null
            );'''
    cur1.execute(sql)
    mycon.commit() 


def car_ver():
    sql = '''create table Car_ver(
            Serial_No int primary key,
            RC_No int Not Null,
            Insurance_No int not null,
            Insurance_Exp varchar(10) not null,
            Pollution_Exp varchar(10) not null,
            Seller varchar(20) not null,
            foreign key (serial_no) references car_desc(serial_no) ON DELETE CASCADE
            );'''    
    cur1.execute(sql)
    mycon.commit() 


def queries():
    sql = '''create table queries(
            serial_no int primary key,
            username varchar(30) not null,
            query varchar(250),
            answer varchar(250),
            feedback int
            )'''    
    cur1.execute(sql)
    mycon.commit() 


def ins():
    
    sql = '''create table ins(
            serial_no int primary key,
            Name varchar(50) not null,
            price int not null,
            year int not null,
            odo int not null,
            fuel varchar(20) not null,
            trans varchar(20) not null,
            mil int not null,
            hp int,
            seats int not null
            )'''    
    cur1.execute(sql)
    mycon.commit()

ins() 
queries()
cur1.close()
mycon.close()
print("Done")

