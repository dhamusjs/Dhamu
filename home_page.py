
class Home:
    def homePage(self):
        file=open('home.txt','r')
        print(file.read())
        print("\n\n")
        file.close()
        h.choose()
        
    def choose(self):
        print("\n1.Profile\t2.MyCourses")
        choice = int(input())
        if(choice==1):
            from bio import Detail
            d=Detail()
            d.myProfile()
        elif(choice==2):       
            from Mycourse import Courses    
            cour=Courses()
            cour.myCourses()
        else:
            print("Invalid input")
   
h = Home()
#h.homePage()
