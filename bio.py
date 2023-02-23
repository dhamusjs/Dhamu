import csv
class Detail:
    def myProfile(self):
        print("------MYPROFILE-----------")
        import login 
        login_name = login.user_login_name
        login_psswd = login.user_login_password
        with open('data.csv','r')as file:
            file1 = csv.reader(file)
            for lines in file:
                data=lines.split(",")
                if(data[0]==login_name and data[1]==login_psswd):
                    print("Email Id: ",data[2])
                    print("Name: ",data[0])
                    print("City: ",data[3])
                    print("Password: ",data[1])
        file.close()
        print("1.Home\t2.MyCourses\t3.Logout")
        choice = int(input())
        if(choice==1):
            from home_page import Home
            h=Home()
            h.homePage()
        elif(choice==2):
            from Mycourse import Courses
            course=Courses()
            course.myCourses()
        elif(choice==3):
            from logout import Logout
            lo = Logout()
            lo.logOut()  
        else:
            print("Invalid number")
det = Detail()
#det.myprofile()