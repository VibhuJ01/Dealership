import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()
from regseller import reg_seller

def seller(username):

    sql = "select * from seller"
    cur1.execute(sql)
    result = cur1.fetchall()
    flag = 0
    for i in result:
        if(i[4] == username.lower()):
            flag = 1
            break
    
    if(flag == 0):
        register(username)

    else:
        reg_seller()


def register(username):

    print("To become a seller at our Delearship,")
    print("First you need to Register yourself")
    print("\n--------------------------------------------\n")
    
    try:  
        fname = input("Enter you first name: ")
        lname = input("Enter you last  name: ")
        print("\n--------------------------------------------\n")
        
        dob = input("Enter you DOB(xx/xx/xxxx): ")
        print("\n--------------------------------------------\n")
        
        padd = input("Enter you permenant address: ")
        print("\n--------------------------------------------\n")
        
        ph = int(input("Enter you Contact Number: "))
        al = int(input("Enter you Alternate Contact Number: "))
        print("\n--------------------------------------------\n")
        
        doc = int(input("Enter your Govt. Document Number: "))
        print("\n--------------------------------------------\n")
        
        ch = input("Are you sure that the above details are correct?(y/n) ")
        print("\n--------------------------------------------\n")
        
        if(ch.lower() == "y"):
            sql = 'insert into seller values(%s,%s,%s,%s,%s,%s,%s,%s)'
            data = (fname,lname,dob,padd,username.lower(),ph,al,doc)
            cur1.execute(sql,data)
            mycon.commit()

    except:
        
        print("Wrong Input, Try again")
        print("\n--------------------------------------------\n")
        return

    else:
        print("Registration Complete")
        print("\n--------------------------------------------\n")   
    
    
