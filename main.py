from signup import signup
from login import login

def main():
    print("\n--------------------------------------------\n")
    print("Welcome to Dealership")
    print("We will help you select perfect car")
    print("As per your needs")
    print("\n--------------------------------------------\n")
    
    print("1. Manager")
    print("2. Customer")
    print("3. Exit")
    ch = input("Login as: ")
    print("\n--------------------------------------------\n")
    
    if(ch == "1"):
        pass

    elif(ch == "2"):
        print("1. Signup")
        print("2. Login")
        print("3. Back")
        ch2 = input("What do you want to do?: ")
        print("\n--------------------------------------------\n")

        if(ch2 == "1"):
            signup()
            
        elif(ch2 == "2"):
            login()

        elif(ch2 == '3'):
            pass

        else:
            print("Wrong Input")  

       

    elif(ch == "3"):
        print("Thank you for Visiting Dealership")
        print("Have a Nice Day")
        print("\n--------------------------------------------")
        return
        
    else:
        print("Wrong Input")
        
    main()
    
if __name__ == "__main__":
    main()
