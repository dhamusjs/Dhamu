from validation import validate
from logout import out
class admin():
    def __init__(self):
        pass
   
    def create_stud(self):

        for i in range(1):
          Name=input("\nStudent Name")
          Regno=input("Student Regno")
          Tamil=input("Student Tamil")
          English =input("Student English")
          Maths=input("Student Maths")
          Science=input("Student Science")
          S_Science=input("Student S_Science")
          v.stud_details(Name,Regno,Tamil,English,Maths,Science,S_Science)
                
    def time_table(self):
        f=open("TIME TABLE.txt","r")
        print(f.read())
        f.close()

    def grading_sys(self):
        f=open("Grading sys.txt","r")
        print(f.read())
        f.close()

    
    def start(self):
        global value
        i=1
        while i>0:
          print("###### ADMIN #####")
          print("\n1.ADD RESULTS \n2.EXAM TIME TABLE \n3.GRADING SYSTEM \n4.EXIT\n" )
          value=input("")
          if(value=="1"): 
            s.create_stud()
          elif(value=="2"):
            s.time_table()
          elif(value=="3"):
            s.grading_sys()
          elif(value=="4"):
            print("\n##### THANK YOU #####")
            o.end()
          else:
            print("\n##### WRONG VALUE #####")
            s.start()
        i+=1
       
s=admin()
v=validate()
o=out()




 
            
