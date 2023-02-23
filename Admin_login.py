class Admin:
    def __init__(self,admin_name,admin_password):
        self.admin_name = admin_name
        self.admin_password = admin_password
    def adminLogin(self):
        self.login_name = input("Admin name: ")
        self.login_psswd = input("password: ")
        if(self.admin_name == self.login_name and self.admin_password == self.login_psswd):
            file=open("data.csv","r")
            print(file.read())
            print("1.Add user\t2.Logout")
            choice = int(input())
            if(choice==1):
                from Validate import Validate
                val=Validate()
                val.userRegister()
            elif(choice==2):
                print("Thank you")
                exit()
        else:
            print("Invalid admin name or password")
            ad.adminLogin()
    
ad = Admin("chan","chan@123")
ad.adminLogin()