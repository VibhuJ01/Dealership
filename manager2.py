from buy import buy
from seller import seller

def afterloginM(username,password):

    print("1. Buyer")
    print("2. Seller")
    print("3. Change Password")
    print("4. Back")
    ch = input("What do you want to do? ")
    print("\n--------------------------------------------\n")

    if(ch == '1'):
        buy(username)

    elif(ch == "2"):
        seller(username)

    elif(ch == "3"):
        changepass(username,password)
        
    elif(ch == "4"):
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")

    afterloginM(username,password)

def changepass(username,password):
    
    oldpass = input("Enter Old Password:\t")
    if(oldpass == password):
        newpass = input("Enter New Password:\t")
        print("Password should have 1 uppercase")
        print("\n--------------------------------------------\n")
        print("Validating Password....\n")
        print("\n--------------------------------------------\n")
        a = password_validation(newpass)
        if(a == 1):
            sql = '''update login 
                    set password = %s
                    where username = %s'''
            data = (newpass,username.lower())
            cur1.execute(sql,data)
            mycon.commit()
            print("\n--------------------------------------------\n")
            print("Changing Password....")
            print("Your New Password is ",newpass)
            print("\n--------------------------------------------\n")

        else:
            print("New Password is not Valid")
            print("\n--------------------------------------------\n")
            
    else:
        print("\n--------------------------------------------\n")
        print("Your Old password did not Match")
        print("\n--------------------------------------------\n")
        ch = input("Do you want to try again?(y/n) ")
        print("\n--------------------------------------------\n")

        if(ch.lower() == "y"):
            changepass(username,password)
            

        elif(ch.lower() != "n"):
            print("Wrong Input")
            print("\n--------------------------------------------\n")

def password_validation(password):
    a = 2
    for i in password:
        if(i.isupper() == True):
            print("Password Validation Complete")
            a = 1
            break
    return a
