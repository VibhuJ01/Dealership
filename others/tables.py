import mysql.connector as ms
mycon=ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()

def login():
    sql = '''create table login
    (f_name varchar(20) not null,
    l_name varchar(20) not null,
    username varchar(50) not null primary key,
    password varchar(30) not null)'''
    cur1.execute(sql)
    mycon.commit()

login()
cur1.close()
mycon.close()
print("Done")
