#creating a list with 10 items
#Method 1:
l=[1,2,3,4,5,6,7,8,9,10]
print(l)

#Method 2:
l=[1,2,3,4]
for i in range(len(l)):
    print(l[i],end=" ")
    

#Method 3:
l=[1,2,3,4]
for i in l:
    print(i)

#Method 4:
'''l=list(input("enter numbers:"))
print(l)'''

#program2 take 5 float num and print sum and avg
#static
'''l=[1.2,2.3,3.4,4.5,5.6]
sum1=0
avg=0
for i in l:
    sum1=sum1+i
avg=(sum1/5)
print(sum1)
print(avg)'''

#Dynamic
'''n=int(input("enter size of the list:"))
l=list(map(float,input("enter numbers:").split()))
sum1=0
avg=0
for i in l:
    sum1=sum1+i
avg=(sum1/len(l))
print(sum1)
print(avg)'''

#create a list and display even numbers
'''l=list(map(int,input("enter numbers:").split()))
even_list=[]
odd_list=[]
for i in l:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)'''

#using while loop
'''n=int(input("enter size:"))
l=list(map(int,input("enter numbers:").split()))
even_list=[]
odd_list=[]
i=0
while(i<n):
    if(l[i]%2==0):
        even_list.append(l[i])
    else:
        odd_list.append(l[i])
    i=i+1    
print(even_list)
print(odd_list)'''

#find product and sum of given list.If the product < 750 then print sum orelse print product
'''l=list(map(int,input("enter numbers:").split()))
sum1=0
prod=1
for i in l:
    prod=prod*i
    sum1=sum1+i
if(prod<750):
    print(sum1)
else:
    print(prod)'''

#list comprehension
l=["hyd","vizag","vijaywada","ongole"]
city=[]
for i in l:
    if "v" in i:
        city.append(i)
print(city)

#another program
l=[2**a for a in range(2,5)]
print(l)

#another program
l1=[1,2,3,4,5,6]
l2=[a for a in l1 if(a<4)]
print(l2)
   

    


        




    


