#error handling

'''a=int(input("enter a num:"))
b=int(input("enter a num:"))
try:      # u are telling this may have error,u try
    print(a/b)
except Exception as e:   #u are telling if there is an error i will handle it
    print("It's an error:",e)
finally:  #even if there is an error it will be executed
    print("done")'''

#another method
'''a=int(input("enter a num:"))
b=int(input("enter a num:"))
try:      # u are telling this may have error,u try
    print(a/b)
except ZeroDivisionError as e: #u are telling if there is an error i will handle it
    print("It's an error:",e)
finally:  #even if there is an error it will be executed
    print("done")'''

#Multiple except blocks:

'''try:
    a=int(input("enter a num:"))
    b=int(input("enter a num:"))
    print(a/b)
except ZeroDivisionError as e:
    print("division by zero is not possible:",e)
except ValueError as e:
    print("Invalid input:",e)
except Exception as e:
    print("other error:",e)
finally:
    print("done")'''

#raise exception
'''x=int(input("enter a num:"))
if(x%2)!=0:
      raise Exception ("It should be even num:")
else:
    print("correct")'''
#another method
'''l=list(map(int,input("enter a num:").split()))
for i in l:
    if((i%2)!=0):
        raise Exception("It should be even num:")
    else:
        print(i)'''


#classes and methods
#method is a function inside a class
'''class computer:
    def func(self):           #self keyword is mandotory in method
        print("hello")
obj=computer()        #creating an object for class computer
obj.func()  '''        #calling method

#without method
'''class computer:
    print("hello")
obj=computer()'''

#constructor usage
'''class Employee():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)
emp1=Employee("joh",13)
emp2=Employee("janaki",12)
emp1.display()
emp2.display()'''

#variables and variables access in class and methods
class computer():
    a=10               #global scope
    b=20
    print("class or instance variables:",a,b)
    def meth(self):
        c=100       #local scope
        print("local variable:",c)
        print("global variable:",self.a)
obj1=computer()
print(obj1.a)
print(obj1.a+obj1.b)
obj1.meth()
print(obj1.c)     # throws an error bcoz c is local scope variable.








        




    
