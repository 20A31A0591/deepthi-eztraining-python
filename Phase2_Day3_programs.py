#ALL OPERATIONS IN A SINGLE PROGRAM
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        if not temp:
            print("list is empty")
            return
        else:
            print("start:",end=" ")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("end")
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        elif self.head.data >=new_node.data:
             new_node.next=self.head
             self.head=new_node
        else:
            temp=self.head
            while temp.next and new_node.data>temp.next.data:
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def delete(self,key):
        if self.head is None:
            print("list is empty")
            return
        if self.head.data==key:
            self.head=self.head.next
            return
        current=self.head
        while current:
            if current.data==key:
                break
            else:
                previous=current
                current=current.next
        if current is None:
            print("key not found")
        else:
            previous.next=current.next
if __name__=='__main__':
    LL=linkedlist()
    print('')
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(11)
    LL.insert(10)

    LL.printlist()
    LL.delete(12)
    LL.delete(8)
    LL.delete(10)
    LL.printlist()'''

#USER DEFINED FUNCTIONS CREATION
'''import function
function.printing()
print(__name__)'''

#ANOTHER EXAMPLE
'''print("before functions")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=='__main__':
    f1()
    f2()
    f3()
print("name:",__name__)'''

#DOUBLE LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublell:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
l=Doublell()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.display()'''

#INSERTION OPERATIONS IN DOUBLY LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublell:
    def __init__(self):
        self.head=None
    def insert_beg(self,data):
        new=Node(data)
        temp=self.head
        new.next=temp
        temp.prev=new
        self.head=new
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
l=Doublell()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.insert_beg(100)
l.display()'''

#INSERTION  OPERATIONS  aAT END IN DOUBLY LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublell:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new
        new.prev=temp
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
l=Doublell()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.insert_end(100)
l.display()'''

#INSERTION  OPERATIONS  AT POSITION IN DOUBLY LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublell:
    def __init__(self):
        self.head=None
    def insert_pos(self,data,pos):
        new=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        new.prev=temp
        new.next=temp.next
        temp.next.prev=new
        temp.next=new
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
l=Doublell()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.insert_pos(100,2)
l.display()'''

#DELETION AT BEGINNING IN DOUBLE LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublell:
    def __init__(self):
        self.head=None
    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
l=Doublell()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.delete_beg()
l.display()'''

#DELETION AT END IN DOUBLE LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublell:
    def __init__(self):
        self.head=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
l=Doublell()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.delete_end()
l.display()'''

#DELETION AT END IN DOUBLE LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Doublell:
    def __init__(self):
        self.head=None
    def delete_pos(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
l=Doublell()
n1=Node(10)
l.head=n1
n2=Node(20)
n2.prev=n1
n1.next=n2
n3=Node(30)
n2.next=n3
n3.prev=n2
l.delete_pos(1)
l.display()'''

#----------------------------------------------------------------------------------------------------------
#CIRCULAR LINKED LIST:------------

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Createlist:
    def __init__(self):
        self.head=Node(None)
        self.tail=Node(None)
        self.head.next=self.tail
        self.tail.next=self.head

    #Adding node at end of LL
    def add(self,data):
        newnode= Node(data)
        #is empty?
        if self.head.data is None:
            self.head=newnode
            self.tail=newnode
            newnode.next=self.head
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.tail.next=self.head
    def display(self):
        current = self.head   
        if self.head is None:
            print("List is empty")
            return    
        else:
            print("Nodes of the circular linked list: ") 
        #Prints each node by incrementing pointer.    
            print(current.data)   
            while(current.next != self.head):
                current = current.next    
                print(current.data)    
     
     
class CircularLinkedList:    
  cl = Createlist();    
  #Adds data to the list    
  cl.add(1);    
  cl.add(2);    
  cl.add(3);    
  cl.add(4);    
  #Displays all the nodes present in the list    
  cl.display();    
                
        
        



    
    
            
        
        




        
                
    
    
        
        
        
        
    
        



    
    
                
            
        
        
        
