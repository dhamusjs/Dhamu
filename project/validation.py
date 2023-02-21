import re
import csv
class validate():
   def __init__(self):
        pass
   def stud_details(self,Name,Regno,Tamil,English,Maths,Science,S_Science):
      N=1
      while N>0:
         pattern=r"^[A-Z]+[A-Za-z0-9_]{4,29}$"
         if  not re.findall(pattern,Name):
               print("........INVALID STUDENT NAME..................")
               Name=input("Student Name\t\t\t:")
         else:
               break
      N+=1
      
      R=1
      while R>0:
         pattern=r'^[0-9]{6,8}'
         if not re.findall(pattern,Regno):
           print("##### INVALID REGNO #####") 
           Regno=input("Re-Enter The Regno \t \t")

         else:
          break
      R+=1
      
      T=1
      while T>0:
         pattern=r'^[0-9]{1,3}'
         if not re.findall(pattern,Tamil):
            print("##### INVALID T_MARK #####") 
            Tamil=input("Re-Enter the Tamil mark \t \t")
         else:
            break

      T+=1
      
      E=1
      while E>0:
         pattern=r'^[0-9]{1,3}'
         if not re.findall(pattern,English):
            print("##### INVALID E_MARK #####") 
            English=input("Re-Enter the English mark \t \t")

         else:
            break
      E+=1

      M=1
      while M>0:
         pattern=r'^[0-9]{1,3}'
         if not re.findall(pattern,Maths):
            print("##### INVALID M_MARK #####") 
            Maths=input("Re-Enter the maths mark \t \t")
            
         else:
          break
      
      M+=1
      
      S=1
      while S>1:
         pattern=r'^[0-9]{1,3}'
         if not re.findall(pattern,Science):
            print("##### INVALID S_MARK #####") 
            Science=input("Re-Enter the Science mark \t \t")
           
         else:
            break
      S+=1
      
      SS=1
      while SS>0:
         pattern=r'^[0-9]{1,3}'
         if not re.findall(pattern,S_Science):
            print("##### INVALID SS_MARK #####") 
            S_Science=input("Re-Enter the S_Science mark \t \t")
          
         else:
            break
      SS+=1
      
      T=int(Tamil)
      E=int(English)
      M=int(Maths)
      S=int(Science)
      SS=int(S_Science)
      Total=T+E+M+S+SS
      with open("user_detail_2.csv","a+",newline="") as reg:
         detail=csv.writer(reg)
         detail.writerow([Name,Regno,Tamil,English,Maths,Science,S_Science,Total])      
    
v=validate() 


