# bitwise operators conversions
'''print(10&4)
print(12&7)
print(10|4)
print(~3)
print(~7)
print(~12345678)
print(5^6)
print(10<<2)
print(10>>2)'''

#taking user input for the above
'''n1,n2=map(int,input("enter").split())
print(n1&n2)
print(n1|n2)
print(~n1)
print(n1^n2)
print(n1<<n2)
print(n1>>n2)'''

#taking multiple inputs
'''n=int(input("size"))
l=list(map(int,input("enter:").strip().split()))
print(l)

l=list(map(int,input("enter:").strip().split()))
print(l)'''

#find product of 10 integer num
'''l=list(map(int,input("enter:").strip().split()))
p=1
for i in l:
    p=p*i
print(p)'''

#delimeters
'''print("its",'a','good','day',end='')#two lines executed on same line
print("all",'is','good',sep="***",end='\n')#each word is separated with ***
print("joy")

print("its",'a','good','day')#two lines executed on different  line
print("all",'is','good',sep="***",end='\n')#each word is separated with ***
print("joy")'''


#  heart
'''print("# # #           # # #")
print("#        ##        #")
print("#                  #")
print(" #                #")
print("   #             #")
print("     #          #")
print("       #      #")
print("           #    ")'''

# upside-down triangle
'''print("* * * * *")
print(" * * * *")
print("  * * *")
print("   * *")
print("    *")'''

#ifloop
'''temp=int(input("enter:"))
if(temp>45):
    print("hottest")
elif(temp>=40 and temp<=45):
    print("hot")
elif(temp>=25 and temp<=40):
    print("moderate")
elif(temp>=10 and temp<=25):
    print("cold")
else:
    print("chill")'''

#practice programs:
#program 1: num is equal to 500 or not
'''n=int(input("enter a number:"))
if(n==500):
    print("Yes! It is 500")
else:
    print("No! It is not 500")'''

#program2: num is even- pos or even -neg or odd- pos or odd- neg
'''n=int(input("enter a number:"))
if(n%2==0 and n>0):
    print("even positive")
elif(n%2==0 and n<0):
    print("even negative")
elif(n%2!=0 and n>0):
    print("odd positive")
else:
    print("odd negative")'''


#program3: find bigger num out of 2 num
'''n1,n2=map(int,input("enter two numbers:").split())
if(n1>n2):
    print("the bigger number is:",n1)
else:
    print("the bigger number is:",n2)'''


#program4 find given num is int or float
'''n=input("enter:")
if "." in n:
    print("it is a floating point number")
else:
    print("it is a integer number")'''

#another method
'''n=12.3
if(isinstance(n,int))==True:
    print("integer")
else:
    print("float")'''
#another method
'''n=10.3
res=n-int(n)
if(res>0 or res!=0):
    print("float")
else:
    print("integer")'''

#program5: find bigger num out of 3 num
'''n1,n2,n3=map(int,input("enter three numbers:").split())
if(n1>n2 and n1>n3):
    print("the bigger number is:",n1)
elif(n2>n1 and n2>n3):
    print("the bigger number is:",n2)
else:
    print("the bigger number is:",n3)'''

#program6: find whether given num is divisible by 11 or not
'''n=int(input("enter a number:"))
if(n%11==0):
    print("the number is divisible")
else:
    print("the number is not divisible")'''

#program7: find whether given number is divisible by 2 and 5 or not
'''n=int(input("enter a number:"))
if(n%2==0 and n%5==0):
    print("the number is divisible by 2 and 5")
else:
    print("the number is not divisible by 2 and 5")'''
    
    
#while loop
'''i=1
while(i<=10):
    print(i,end=" ")
    i=i+1'''

#program 1: print 2 to 20 even numbers using while loop
'''i=2
while(i<=20):
    if(i%2==0):
        print(i)
    i=i+1'''

#program 2: print 1 to 30 odd numbers using while loop
'''i=1
while(i<=30):
    if(i%2!=0):
        print(i)
    i=i+1'''
#program to print 1st 20 even numbers
'''n=20
count=1
while(count<=20):
    print(count*2)
    count=count+1'''
    

#for loop
'''for i in range(1,11):
    print(i)'''
'''for i in range(1,11,2):
    print(i)'''

#program 1: print 2 to 20 even numbers using for loop
'''n=20
i=2
for i in range(i,n+1,2):
    print(i)'''

#program 2: print 1 to 30 odd numbers using while loop
'''n=30
i=1
for i in range(i,n+1,2):
    print(i)'''

#program
'''import random
n=random.randrange(1,50)
guess=int(input("enter a number"))
while(guess!=n):
    if(guess<n):
        print("too low!")
        guess=int(input("enter another number:"))
    elif(guess>n):
        print("too high!")
        guess=int(input("enter another number:"))
    else:
        break
print("you guessed it right!")'''

#another method
'''import random
n=random.randrange(1,5)
guess=int(input("enter a number"))
while(guess!=n):
    if(guess<n):
        print("too low!")
        guess=int(input("enter another number:"))
    else:
        print("too high!")
        guess=int(input("enter another number:"))
    break
print("you guessed it right!")'''
    
    
