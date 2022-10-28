from signup import signup
from login import login

print("\n--------------------------------------------\n")
def main():
    print("Welcome to Dealership")
    print("We will help you select Perfect Car")
    print("As per your Needs")
    print("\n--------------------------------------------\n")
    
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    ch = input("Login as: ")
    print("\n--------------------------------------------\n")
    
    if(ch == "1"):
        signup(0)

    elif(ch == "2"):
        login()
       
    elif(ch == "3"):
        print("Thank you for Visiting Dealership")
        print("Have a Nice Day")
        print("\n--------------------------------------------")
        return
        
    else:
        print("Wrong Input")
        print("\n--------------------------------------------\n")
        
    main()
    
if __name__ == "__main__":
    main()
