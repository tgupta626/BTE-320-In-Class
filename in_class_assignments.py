# -*- coding: utf-8 -*-
"""In Class Assignments

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_KDEM77zZAskH4f_4vhk90Pp1kiOUp44

Shape Area Calculator
"""

pi=3.14
h=10
r=3


Area= 2*pi*r**2 + 2*pi*r*h
print(Area)

"""Rock paper scissor(while loop)"""

i= input('Do you want to play rock,paper, scissors? yes or no?')
while i== 'yes':
  p1= input('player 1 enter your move(r->rock,p-> paper, or s->scissors)')
  p2= input('player 2 enter your move(r->rock,p-> paper, or s->scissors)')


  if p1==p2:
    print ('draw')

  elif p1== 'r' and p2== 's':
    print ('p1 wins')

  elif p1== 's' and p2== 'p':
    print ('p1 wins')

  elif p1== 'p' and p2== 'r':
    print ('p1 wins')

  else:
    print ('p2 wins')

  i=input('do you want to play yes or no:')

"""Numerical Calculator"""

n1= float(input('enter first number:'))
n2= float(input('enter second number:'))
symbol= input('operation(+,-,*,/,**):')

if symbol == '+':
  print(n1+n2)
elif symbol == '-':
  print(n1-n2)
elif symbol == '*':
  print(n1*n2)
elif symbol == '/':
  print(n1/n2)
else:
  print(n1 ** n2)

"""Parking Garage"""

# a parking garage charges $5 plus 2.5 for each hour parked. the minimum fee is 10 dollars and the maximu is 20
# write a program that generates a table with hours parked and the corresponding fee from 1-8 hours
flatRate= 5
hourlyRate= 2.50

for h in range (1,9,1):
  charge= flatRate + hourlyRate * h
  if charge < 10:
    charge = 10
  elif charge > 20:
    charge = 20
  print(h,charge )

#write a program where a parking garage charges $5 plus $2.5 for each hours parked- prompts for number of hours parked and calculates/displa
#if you see a none when you make a function make sure you use the return! prolly just means you didnt add that line
def calcFee(hours):
  fee = 5 + hours * 2.5
  return fee
h=float(input('enter number of hours : '))
fee=calcFee(h)
print(fee)

"""Movie Theater"""

#each ticket is 10 without advertising 20 people attend additional attendees if advertising = 2x(sqroot addollars) fixed costs = 200 write a
# for different advertising amounts and profits

ticketPrice=10
fixedCost= 200
fixedAttendees= 20

for ad in range (0, 201, 25):
  additionalAttendes= 2*round(ad**.5)
  profit= (fixedAttendees + additionalAttendes)*ticketPrice- ad- 200
  print(ad,profit)

"""Months to Numbers"""

#populate a dictionary where the key comes from the list of numbers and the value is from the namesor i in range(len(names)):
months= {}
names= ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
numbers= [1,2,3,4,5,6,7,8,9,10,11,12]
for idx in numbers:
   months[idx]=names[idx-1]
print(months)

"""Fee Calculation and Display Functions"""

#not make a refined program to have the fee to have 2 decimals
flatRate= 5
hourlyRate= 2.50

def calcFee(hours, decimals=2):
  fee= 5 + hours * 2.5
  fee= round (fee,decimals)
  return fee

def displayFee(fee):
  print(fee)

h=int(input('enter number of hours:'))
fee= calcFee(h, decimals=0)
displayFee(fee)

"""Reverse Function Recursion"""

# we want to design a recurstion function that reverses the string, the string is Hello, you want it to return olleh
def reverse(s):
  if len(s) == 1:
    return s
  else:
    return s[-1]+reverse(s[:-1])
reverse('hello')

"""Student Class"""

### define a class named student, student has 2 attributes name and number create two student objetcs out of this class
class Student:
  def __init__ (self,name,number,courses):
    self. __name= name
    self.number= number
    self.__courses=[]

  def enroll (self, newCourse ):
    if newCourse not in self.__courses:
      self.__courses.append (newCourse)
    else:
      print(f' You have already enrolled in {new}')

  def get_courses (self):
    return self.__courses

s=Student('bob','12345',[1,3,4])