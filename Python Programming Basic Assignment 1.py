#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to print "Hello Python"?
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


print('Hello Python')


# 2.	Write a Python program to do arithmetical operations addition and division.?
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


import operator

ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv } 

print('Select a Arithmetic Operation:         \n1.Addition(+)        \n2.Division(-)        \n2.Multiplication(*)        \n4.Division(/)        \n3.Stop(0)\n')
   

while True:
    operator = input('Enter a arithmetic operation -> ')
    if operator == '0':
        print("Program Stopped successfully")
        break
    elif operator not in ['+','-','*','/']:
        print("Please enter a valid operator")
    else:
        num_1 = int(input('\nEnter 1st Number: '))
        num_2 = int(input('Enter 2nd Number: '))
        print('{}{}{}={}\n'.format(num_1, operator, num_2, ops[operator](num_1,num_2)))


# 3.	Write a Python program to find the area of a triangle?
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


height = int(input('Enter height of triangle: '))
base = int(input('Enter base of triangle: '))

def areaOfTriangle(height, base):
    print('\nArea of triangle ->', 0.5*height*base)

areaOfTriangle(height,base)


# 4.	Write a Python program to swap two variables?
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

def swapNumbers(a,b):
    temp = a
    a = b
    b = temp
    return a,b

print('Before swapping -> ',num_1, num_2)
num_1, num_2 = swapNumbers(num_1, num_2)
print('After swapping -> ',num_1,num_2)


# 5.	Write a Python program to generate a random number?
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


from random import randint

def generateRandomNumber(start=0, end=100000):
    print('Random number -> ',randint(start,end))

# Generating random numbers without arguments    
generateRandomNumber()

# Generating random numbers with arguments    
generateRandomNumber(0,100)

