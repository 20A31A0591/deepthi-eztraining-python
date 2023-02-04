#Project1
q1="""who is the President of India?
a.Ramnadh Kovindh
b.Draupadi Murmu
c.Nirmala Sitharamam
d.Venkai naidu"""

q2="""what is the 1st movie name of Mahesh babu?
a.Takkari dhonga
b.Pokiri
c.Rajakumarudu
d.Murari"""

q3="""Who is the prime minister of Britain?
a.Rishi Sunak
b.John Major
c.Harold Wilson
d.James Callaghan"""

q4="""Who's Bollywood actor name is written on Burj Khalifa?
a.Salman khan
b.Sharukh Khan
c.Ranveer Kapoor
d.Varun Dhawan"""

q5="""Who is the founder of Python?
a.Dennis ritche
b.Guido van Rossum
c.John Backus
d.Mark Jukerberg"""

questions={q1:"b",q2:"c",q3:"a",q4:"b",q5:"b"}
name=input("Enter your name:")
print("Hello!",name,"Welcome to Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag=input("Do you wnat to skip this question:(yes/no):")
    if(flag=="yes"):
        continue
    else:
        ans=input("Enter your answer:")
    if(ans==questions[i]):
        print("Wow! You got 1 point")
        score=score+1
        print("Your current score is:",score)
    else:
        print("It is a wrong answer")
        
        score=score-1
        print("Your current score is:",score)
    flag2=input("Do you want to quit this game:(yes/no):")
    if (flag2=="yes"):
        break
print("Your total score is:",score)
print("Thank you for playing !Have a Good Day")
        
    







