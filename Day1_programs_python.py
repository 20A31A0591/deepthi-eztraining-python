#program1
'''kc1=75
sc=kc1/2
kc2=sc/2
print("candy that kumar have:",sc+kc2)
print()'''

#program2
'''a=36.32*3
b=a+56.19
c=b-10
print(c)
print()'''

#program3
'''n1=10
n2=-3.5
n3=n1*n2
print(n3)
print()'''

#floor division
'''a=10//5
print(a)
b=10/5
print(b)
c=10%3
print(c)'''


#relational operators
'''print(10!=2)
print(10==2)
print(10<=2)
print(10>=2)
print(10<2)
print(10>2)
print()'''

#taking multiple input in one line
#method1
'''a,b=int(input("enter")),int(input("enter"))
print(a)
print(b)
s=a+b
print(s)'''

#method2
'''a,b=int(input("enter")),int(input("enter"))
print(a,b)'''

#method3
'''a,b=input("enter").split()
print(a)
print(type(a))
print(b)
print(a+b)'''

#method4
'''a,b=input("enter").split(",")
print(a)
print(type(a))
print(b)'''

#swapping two num with temp
'''n1,n2=int(input("enter")),int(input("enter"))
print("before swapping:",n1,n2)
temp=n1
n1=n2
n2=temp
print("after swapping:",n1,n2)'''

#area of rectangle
'''l,b=int(input("enter:")),int(input("enter"))
area=l*b
print(area)'''

#perimeter of rectangle
'''l,b=int(input("enter:")),int(input("enter"))
perimeter=2*(l+b)
print(perimeter)'''

#swapping two numbers without temp
'''n1,n2=map(int,input("enter:").split())
print("before swaping:",n1,n2)
n1=n1+n2
n2=n1-n2
n1=n1-n2
print("after swapping:",n1,n2)'''

#another method
'''n1,n2=map(int,input("enter:").split())
print("before swaping:",n1,n2)
n1=n1^n2
n2=n1^n2
n1=n1^n2
print("after swapping:",n1,n2)'''
