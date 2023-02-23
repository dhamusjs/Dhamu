import csv
class Login:
    def loginPage(self):
        global user_login_name,user_login_password
        print("\t\t-----------LOGIN-----------") 
        flag = True
        while flag:
            user_login_name = input("UserName: ")
            user_login_password = input("Password: ") 
            with open('data.csv','r')as file:
                file2 = csv.reader(file)
                # row = file.readlines()
                for lines in file:
                    data=lines.split(",")
                    #print(data)
                    #print(data[0],loginname)
                    #try:
                    if(data[0] == user_login_name and data[1] == user_login_password):
                        print("login successfully...")
            file.close()
            flag = False
        from home_page import Home
        h=Home()
        h.homePage()
                                

log = Login()
#log.login()



"welcome"
