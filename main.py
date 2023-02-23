class Main:
    def choose(self):
        print("\t\t------KNOWLEDGE BASE - LEARNING PORTAL-------\n")
        print("1.REGISTER \n2.USER LOGIN\n3.ADMIN LOGIN")
        choice = int(input())
        if(choice == 1):
            from Validate import Validate
            val=Validate()
            val.userRegister()
        elif(choice == 2):
            from login import Login
            log = Login()
            log.loginPage()
        elif(choice == 3):
            from Admin_login import Admin
           
            

m = Main()
m.choose()