#Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

#function without argument and without return value:
'''def sample():       #called function
    print("hello")
    print("world")
sample()   '''         #calling function

#another method
'''def sample():          
    print("hello")            
    print("world")
sample()
print("hii")
sample()'''

#output:
'''hello
world
hii
hello
world'''

#another method taking user input
'''def sum():
    n1=int(input("enter a num:"))
    n2=int(input("enter a num:"))
    sum1=n1+n2
    print(sum1)
sum()'''

#output:
'''enter a num:2
enter a num:3
5'''

#function without argument and return value:
'''def prod():
    n1=int(input("enter a num:"))
    n2=int(input("enter a num:"))
    product=n1*n2
    return product
result=prod()
print(result)'''
#output
'''enter a num:2
enter a num:3
6'''

#function with argument and without return value:
#static
'''def sum(a,b,c):
    sum1=a+b+c
    print(sum1)
sum(1,2,3)'''

#dynamic
'''def sum(n1,n2,n3):
    sum1=n1+n2+n3
    print(sum1)
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
sum(a,b,c)'''

#function with argument and with return value:
#static
'''def sum(a,b,c):
    sum1=a+b+c
    return(sum1)
res=sum(1,2,3)
print(res)'''

#dynamic
'''def sum(n1,n2,n3):
    sum1=n1+n2+n3
    return sum1
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
res=sum(a,b,c)
print(res)'''

#program1 using functions of type1: lemons excess or need more
'''def lemons():
    n1=int(input("enter number of lemons u want:"))
    n2=int(input("enter number of lemons u have:"))
    if(n2>n1):
        x=n2-n1
        print("u have ",x," excess lemons")
    elif(n2<n1):
        y=n1-n2
        print("u need",y,"lemons")
    else:
        print("sufficient")
lemons()'''

#program2 using functions of type2: factors of given num
'''def factors():
    n=int(input("enter a number"))
    l=[]
    for i in range(1,n+1):
        if(n%i==0):
            l.append(i)
    return(l)
res=factors()
print("factors of given num are:")
print(res)'''

#another method
'''def factors():
    n=int(input("enter a number"))
    l=[]
    while(n>=0):
        for i in range(1,n+1):
            if(n%i==0):
                l.append(i)
        return(l)
res=factors()
print("factors of given num are:")
print(res)'''
                
#program3 using functions of type3: multiplication table of given num
'''def multi(n):
    product=1
    for i in range(1,11):
        print(n,"*",i,"=",(n*i))
n=int(input("enter a number:"))
multi(n)'''

#program4 using functions of type3:sum of digits of given num
#list of numbers
'''def add(l):
    sum1=0
    for i in l:
        sum1=sum1+i
    return(sum1)
l=list(map(int,input("enter numbers:").split()))
res=add(l)
print(res)'''

#a single number
'''def add(n):
    sum1=0
    while(n>0):
        temp=n%10
        sum1=sum1+temp
        n=n//10
    return(sum1)
n=int(input("enter a num:"))
res=add(n)
print(res)'''

#RECURSIVE FUNCTION
'''def display():
    n=int(input("enter a number:"))
    if(n==1):
        display()
    else:
        print("over")
display()'''

#factorial
def fact(n):
    fac=1
    for i in range(1,n+1):
          fac=fac*i
    return(fac)
n=int(input("enter a number:"))
res=fact(n)
print(res)

#recursive factorial
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter a num:"))
res=fact(n)
print(res)

#fibanocci series
#using while loop
n=int(input("enter number of numbers u want:"))
n1,n2=0,1
count=3
if n<0:
    print("not possible")
elif n==1 or n==0:
    print("fibonacci:",n1)
else:
    print("fibonacci:",n1,n2,end=" ")
    while count<=n:
        n3=n1+n2
        n1=n2
        n2=n3
        count=count+1
        print(n3,end=" ")

#USING FOR LOOP
n=int(input("enter how many numbers want:"))
n1,n2=0,1
if n<0:
    print("not possible")
elif n==1 or n==0:
    print("fibonacci:",n1)
else:
    print("fibonacci:",end=" ")
    for i in range(0,n):
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3

#USING RECURSION FUNCTION
def fib(n):
    if n<=0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter how many numbers want:"))
for i in range(0,n):
    print(fib(i),end=" ")

#FUNCTION RETURNS MORE VALUES
#addition and subtraction of 2 nums in one func
def add_sub(x,y):
    add=x+y
    sub=x-y
    return add,sub
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
res1,res2=add_sub(n1,n2)
print("add=",res1)
print("sub=",res2)




        
        
    




            
        
    




  




