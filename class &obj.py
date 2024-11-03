class Student:
    def __init__(self,name,age,gender):
        self.nm = name
        self.ag = age
        self.gn = gender
st=Student("navya",20,"F")
print(st.nm,st.ag,st.gn)
print(type(st))


class Std:
    def __init__(self):
        self.nm=None
        self.ag=None
        self.gn=None  
st2=Std()
st2.nm=input("enter name")        
st2.ag=input("enter age")
st2.gn=input("enter gender") 
print(st2.nm,st2.ag,st2.gn)

"""st3=Student(a,b,c)
print(st3.nm,st3.ag,st3.gn)"""


#inheritance
class A:
    def __init__(self,a,b):
        self.A=a 
        self._B=b
    def printB(self):
        print(self._B)
ob1=A(2,5)
print(type(ob1))
print(ob1,)        



"""create a student class that holds the details of students like
 name usn and marks in 5 subjects percentage & grade
 
 create 5 student object and get the data for name and marks after 
 that find the % and grade and store it in the class object""" 
