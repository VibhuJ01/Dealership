from tabulate import tabulate

import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="autos",passwd="vibhu")
cur1 = mycon.cursor()


def query(username):
    print('1. Create a Query / Ask Question')
    print('2. Check your Queries')
    print('3. Give Feedbacx')
    print('4. Back')
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")
    
    if(ch == "1"):
        createQ(username)

    elif(ch == "2"):
        ansQ(username)

    elif(ch == "3"):
        feedback(username)
        
    elif(ch == "4"):
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
    
    query(username)


def createQ(username):   
    print('1. Query')
    print('2. Complaint')
    type = input("What is your Type of problem? ")
    print("\n--------------------------------------------\n")
    
    if(type == '1'):
        type = 'Query'

    elif(type == '2'):
        type = 'Complaint'

    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        return

    sub = input('Enter the Subject of your Problem: ')
    query = input("Enter your "+type+": ")

    sql = 'insert into queries(username,type,subject,query,answer) values(%s,%s,%s,%s,%s)'
    data = (username,type,sub,query,'We will reply soon.')
    cur1.execute(sql,data)
    mycon.commit()
    
    print("\n--------------------------------------------\n")
    print(type+' Logged Successfully')
    print("\n--------------------------------------------\n")
    
def ansQ(username):
    sql = 'select * from queries'
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    
    for i in result:
        if(i[5] != 'We will reply soon.' and i[1] == username):
            l.append(i)
    
    print("All Your Queries/Complaints->\n")
    keys = ['Serial_No','Username','Type','Subject','Query','Answer','Feedback']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")
    
def feedback(username):
    sql = 'select * from queries'
    cur1.execute(sql)
    result = cur1.fetchall()
    l = []
    
    for i in result:
        if(i[5] != 'We will reply soon.' and i[1] == username and i[6] == None):
            l.append(i)

    if(len(l) == 0):
        print('No Queries Available')
        print("\n--------------------------------------------\n")
        return
    
    print("All Your Queries/Complaints->\n")
    keys = ['Serial_No','Username','Type','Subject','Query','Answer','Feedback']
    print(tabulate(l, headers = keys, tablefmt = 'pretty',showindex = False))
    print("\n--------------------------------------------\n")

    try:
        ser = int(input("Enter the Serail Number of Query: "))
        print("\n--------------------------------------------\n")
        
        for i in l:
            if(i[0] == ser):
                break
            
        else:
            print('Serial Number is not Available')
            print("\n--------------------------------------------\n")
            return
            
    except:
        print("\n--------------------------------------------\n")
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        return

    else:
        try:
            feed = int(input("Enter Feedback(1-10): "))

        except:
            print("\n--------------------------------------------\n")
            print("Wrong Input")
            print("\n--------------------------------------------\n")
            return

        else:

            sql = '''update queries
                     set feedback = %s
                     where serial_no = %s'''

            data = (feed,ser)
            cur1.execute(sql,data)
            mycon.commit()
            
            print("\n--------------------------------------------\n")
            print('Feedback Successfully Given')
            print("\n--------------------------------------------\n")
