#Dictionary comprehension
dict={n:n*n for n in range (1,5)}
print(dict)

#Program1: Calculating product price for 5 units
old={'rice':60,'dal':120,'oil':150}
new={product:price*5 for (product,price) in  old.items()}
print(new)

#Program2: With Checks
real={'deepu':20,'tri':90,'rani':50}
now={name:age for (name,age) in real.items() if(age>3)}
print(now)

#other type
real={'deepu':20,'tri':90,'rani':50}
now={name:age for (name,age) in real.items() if(len(name)>3)}
print(now)

#Program3: Create a list with 8 customer names and display a dictionary which has customer names along with
#discounts for them from a particular shop
'''import random
l=list(map(str,input("enter customer names").split()))
dict={l[i]:random.randrange(1,100) for i in range(0,len(l))}
print(dict)'''

#Zip function 
l1=['a','b','c']
l2=[1,2,3]
dict={a:b for(a,b) in zip(l1,l2)}
print(dict)

#Program4:
'''l1=list(map(str,input("enter student names").split()))
l2=list(map(int,input("enter total marks").split()))
l3=[]
for i in range(0,len(l2)):
    per=(l2[i]/500)*100
    l3.append(per)
dict={names:percent for (names,percent) in zip(l1,l3)}
print(dict)'''

#another method
'''import random
l1=list(map(str,input("enter student names").split()))
l2=[]
for i in range(len(l1)):
    a=(random.randint(100,500)/500)*100
    l2.append(a)
dict={names:percent for (names,percent) in zip(l1,l2)}
print(dict)'''

#String Programs
#valid: oppositesymbols
'''"hi i'm deepu"
output:"hi i'm deepu"
'hi i am "deepu"'
output:'hi i am "deepu"'
'hi i\'am deepu'
output:"hi i'am deepu"
#invalid : same symbols
'hi i'm deepu'
SyntaxError: unterminated string literal (detected at line 1)
"hi i'm "deepu""
SyntaxError: invalid syntax'''


#string functions
'''s='hii my name is DEEPTHi'
print(s)
print(s.upper())
print(s.lower())
print(s.casefold())
print(s.capitalize())
print(s.replace('THI','U'))
print(s.strip())
print(s.split('&'))
print(s.split())
print(s.center(80,'*'))
print(s.count('E'))
print(s.count('i',5,len(s)))
print(s.endswith('i'))
print(s.endswith('i',0,len(s)))
print(s.find('a'))
print(s.find('l'))
print(s.find('i',6,len(s)))
print(s.index('m'))
print(s.index('D',4))
print(s.index('D',4,len(s)))
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.startswith("low"))
print(s.rfind('i'))
print(max(s))
print(min(s))'''

#output
'''hii my name is DEEPTHi
HII MY NAME IS DEEPTHI
hii my name is deepthi
hii my name is deepthi
Hii my name is deepthi
hii my name is DEEPTHi
hii my name is DEEPTHi
['hii my name is DEEPTHi']
['hii', 'my', 'name', 'is', 'DEEPTHi']
*****************************hii my name is DEEPTHi*****************************
2
2
True
True
8
-1
12
4
15
15
False
False
False
False
21'''

#Difference between Mutable and Immutable
#Mutable
'''x=2
x                       
output:20
id(x)
output:140724663215496          #address is changes
d
x=30
x
output:30
id(x)
output:140724663215816
#Immutable
l=[1,2,3]
l                     
output:[1, 2, 3]
id(l)
output:2439985812224          #address is not changed
l.append(4)
l
output:[1, 2, 3, 4]
id(l)
output:2439985812224'''

#One string  and one character are taken.Check whether character is present in string or not
'''s1=input("enter a string:")
s2=input("enter a character:")
for i in s2:
    if i in s1:
        print("present")
    else:
        print("not present")'''

#another method
'''s1=input("enter a string:")
s2=input("enter a character:")
if s2 in s1:
    print("yes")
else:
    print("no")'''

#check whether the string is pallindrome or not
'''s1=input("enter a string:")
s2=s1[::-1]
if(s1==s2):
    print("pallindrome")
else:
    print("not a pallindrome")'''

#take string as input and check whether it has white spaces or not.if yes count numberb of white spaces
'''s1=input("enter a string:")
count=0
if " " in s1:
    print("yes")
else:
    print("no")
for i in s1:
    if(i==" "):
        count=count+1
print(count)'''

#neon numbers
'''num=int(input("enter a number"))
sq=num*num
n=0
n1=sq%10
n2=sq//10
n=n1+n2
if(num==n):
    print("yes")
else:
    print("no")'''

#another method
'''num=int(input("enter a number"))
sq=num*num
sum1=0
while(sq>0):
    n=sq%10
    sum1=sum1+n
    sq=sq//10
if(sum1==num):
    print("neon")
else:
    print("no")'''

#count number of vowels in given string
s=input("enter")
l=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in s:
    if i in l:
        count=count+1
print(count)




    
    

    
    
    
    
    




        
    




















