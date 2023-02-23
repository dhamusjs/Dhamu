class Courses:
    def myCourses(self):
        print("\n1.Python\t2.Java\t3.RDBMS\t4.Home")
        choice = int(input())
        if(choice==1):
            course.pythonCourse()  
        elif(choice==2):
            course.javaCourse()
        elif(choice==3):
            course.rdbmsCourse() 
        elif(choice==4):
            course.homePage()
        else:
            print("Invalid number")
            course.myCourses()

    def pythonCourse(self):
        try:
            file=open("python_course.txt",'r')
            print(file.read())
            #print(file.closed)
            course.myCourses()  
            file.close()      
        except KeyError:
            print(KeyError)
                   
    def javaCourse(self):
        try:
            file=open("java.txt",'r')
            print(file.read())
            course.myCourses()
            file.close()       
        except KeyError:
            print(KeyError)
          
    def rdbmsCourse(self):
        try:
             file=open("rdbms_course.txt",'r')
             print(file.read())
             course.myCourses()  
             file.close()          
        except KeyError:
            print(KeyError) 
             
    def homePage(self):
        from home_page import Home
        h=Home()
        h.homePage()

course = Courses()
#course.myCourses()