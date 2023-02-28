#PROTECTED---> variables that are declared are only accesible to that class
              #(single _ is used as protected variables)
class encap:
    _a=10
    b=20
    def encapfunc(self):
        _c=30
        print("Encap function-accessing protected")
        print(self._a+10)
        print(_c+10)
obj=encap()
print(obj._a)
obj.encapfunc()
print(obj.b)
print(obj._c)  #it will throw error bcoz function variables cannot accesed at outside

#----------------------------------------------------------------------------------------------
#PRIVATE ---> variables that are declared are accesible
             #with in the class only (double __ is used as private variables)

class encap:
    __a=10
    print(__a)
    def encapsulation(self):
        print('encap function')
        print(self.__a)
obj=encap()
obj.encapsulation()
print(obj.__a) # it will throw an error bcoz a is private only accesed within the class

#---------------------------------------------------------------------------------------------------
#PARENT AND CHILD CLASS EXAMPLE:--

class parent:
    def __init__(self):
        self.value="Inside parent"
    #parents show method
    def show(self):
        print(self.value)

#defining child class
class child(parent):
    def __init__(self):
        self.value="inside child"
    #childs show method
    def show(self):
        print(self.value)
obj1=parent()
obj2=child()
obj1.show()
obj2.show()
    


#Method Overloading
'''class moverload():
    def display(self,a=None,b=20):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()
print("with 2 arguments")
obj.display(1,2)
print("with arguments")
obj.display(1)'''

#Polymorphism example
'''class vijayawada():
    def placename(self):
        print("I live in vijayawada")
    def student(self):
        print("I am a student")
    def year(self):
        print("I am 3rd year")
class hyderabad():
    def placename(self):
        print("I live in hyd")
    def student(self):
        print("I am a student")
    def year(self):
        print("I am 3rd year")
obj1=vijayawada()
obj2=hyderabad()
for i in (obj1,obj2):
    i.placename()
    i.student()
    i.year()'''

#LINKED LISTS
#creating node declaration and creation
'''class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist():
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
obj.display()'''

#another example
'''class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist():
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("w")
obj.head=n
n1=Node("i")
n.next=n1
n2=Node("n")
n1.next=n2
n3=Node("n")
n2.next=n3
n4=Node("e")
n3.next=n4
n5=Node("r")
n4.next=n5
obj.display()'''

#INSERTING NODE AT THE BEGINNING
'''class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell():
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=singlell()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
print("before inserting")
obj.display()
print("")
obj.insert_beg(100)
print("after inserting")
obj.display()'''

#INSERTING AT THE END
'''class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell():
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
            
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=singlell()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
print("before inserting")
obj.display()
print("")
obj.insert_end(100)
print("after inserting")
obj.display()'''

#INSERTING AT THE POSITION
'''class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell():
    def __init__(self):
        self.head=None
    def insert_pos(self,data,pos):
        new=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
            new.next=temp.next
            temp.next=new
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=singlell()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
print("before inserting")
obj.display()
print("")
obj.insert_pos(100,2)
print("after inserting")
obj.display()'''

#DYNAMIC INPUT LINKED LIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
a_llist=Linkedlist()
n=int(input("how many elements do u want to enter"))
for i in range(n):
    data=int(input("enter data item"))
    a_llist.append(data)
print("the linked list ",end=" ")
a_llist.display()



    
        






            
