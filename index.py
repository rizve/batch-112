# print('Hello world') # This is our First Line Code.
# a = 20
# b = 10.45
# print(a + 40)
# String Type str
# 'Hello' "30" ''' True ''' """ False """
# int float
#  208 23.56 5j
# a = 'bangladesh'
# b = 10
# c = 20
# b = '10'
# z = None
# print(type(b))
# print(c + b)
# print(a + str(z))

# a = int(input('Enter A Number :'))
# b = input('Enter A Number :')

# print(type(b))

# print(a + int(b))

# '' "" """ """ ''''''

# a = 'I Love Bangladesh'

# a = '''My 
# Father'
# s'''
'''This is My multiline String'''
# print(a)

# a = '..............I Love Bangladesh..............'
a = 'i love Bangladesh'

# print(a[0:17])
# print(a[-10:])

# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(len(a))
# print(a.index('b'))
# print(a.find('a'))
# print(a.replace('bangladesh', 'India'))
# print(a.count('a'))
# print(a.swapcase())
# print(a.split("."))
# print(a)
# print(a.strip("."))

# b = a.center(50,".")
# print(len(b))
# print(b)


# a = input('Enter Your Name :')
# b = input('Enter Your Age :')
# c = input('Enter Your Subject :')

# x = 'My Name is {}, I am {} Years Old, I am learning {}'
# print(x.format(a,b,c))
# print(f'My Name is {a}, I am {b} Years Old, I am learning {c}')

# '''My Name is Rhami, I am 18 Years Old, I am learning Python'''
# x = 'My Name is {name}, I am {age} Years Old, I am learning {subject}'
# print(x.format(name=a,age=b,subject=c))
# print(f'My Name is {a}, I am {b} Years Old, I am learning {c}')

# a = 'It\'s Alright'
# a = 'It\\s Alright'
# a = 'It\ns Alright'
# a = 'It\ts Alright'
# a = 'It \bs Alright'
# a = 'It \bs Alright'
# print(a)

# len()

# + - * / % ** //

# a =65

# b = 20

# print(a // b)

# = += -=
# a = 20
# a += 10 
# a = a + 10 Example
# a -= 10 
# a = a - 10 Example
# a *= 10 
# a = a * 10 Example
# a /= 10 
# a = a / 10 Example
# a %= 10 
# a = a / 10 Example

# print(a)

# == != > < >= <=

# a = 10

# b = 10

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# Logical Operator
# and or not

# a = 10
# b = 32
# c = 20

# print(a > b and b > c)
# print(a > b or b > c)
# print(not(a > b and b > c))

# Identity Operators
# is is not

# a = 12

# b = 10

# print(a is not b)

# Membership Operator

# in not in

# a = "I Love Bangladesh"

# print('bangladesh' not in a)

# Bitwise Operator
# & | ^ ~ << >>

# print(7 | 4)

# 0 = 0 0 0 0
# 1 = 0 0 0 1
# 2 = 0 0 1 0
# 3 = 0 0 1 1
# 4 = 0 1 0 0
# 5 = 0 1 0 1
# 6 = 0 1 1 0
# 7 = 0 1 1 1

# 0 1 1 1
# 0 1 0 0
# -------------
#  0 1 1 1

# a = 10

# b = 23

# if a == b or a != b:
#     print(a + b)
# else:
#     print('Not Equal')

# if a == b:
#     print(a + b)
# elif a > b :
#     print(a - b)
# elif a < b :
#     print(f'This is b > a Result : {b - a}')
# else:
#     print('No Match Found')

# if a == b:
#     if a == 10:
#         print(a + b)
#     else:
#         print("a is not 10")
# elif a < b :
#     if a == 11:
#         print(f'This is b > a Result : {b - a}')
#     else:
#         print("a is not Equal 11")
# else:
#     print('No Match Found')


# marks = int(input("Enter The Number :"))

# if marks <= 100 and marks > 0 :
#     if marks >= 80:
#         print("A+")
#     elif marks >= 70:
#         print("A")
#     elif marks >= 60:
#         print("A-")
#     elif marks >= 50:
#         print("B+")
#     elif marks >= 40:
#         print("C")
#     elif marks < 40:
#         print("F")
# else:
#     print("Invalid Input") 

# While For

# a = 1


# print(a < 20)

# while a <= 10:
#     print(a)
#     if a == 5:
#         break
#     a += 1 # a = a + 1

# print('I Love Bangladesh')

# a = 0

# while a <= 10:
#     a += 1 # a = a + 1
#     if a == 5:
#         continue
#     print(a)

# print('I Love Bangladesh')

a = 1

# while a <= 10:
#     print('Bangladesh')
#     if a == 5:
#         print('India')
#     a += 1

# while a <= 10:
#     print('Bangladesh')
#     if a == 5:
#         print('India')
#     a += 1
# else:
#     print('Finsh.')

# a = 'I Love Bangladesh'

# for rahim in a:
#     # print(rahim, end='')
#     print(rahim)

# print(len(a))

# for i in range(len(a)):
#     print(i , a[i])

# a = 'Bangladesh'

# for i in a:
#     print(i)


# for i in range(1,11):
#     print(i)
#     if i == 5:
#         break

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)

# x = int(input('Enter A Number :'))

# for i in range(1,11):
#     print(f'{x} X {i} = {x * i}')

# a = 1

# while a <= 10:
#     print(f'{x} X {a} = {a * x}')
#     a += 1

# while True:
#     x = int(input('Enter A Number :'))
#     if x == 0:
#         print('Thank You For Using This Application.')
#         break
#     for i in range(1,11):
#         print(f'{x} X {i} = {x * i}')


# a = input('Enter A Text :')

# print(a.lower())

# a = [54,56,'Bangladesh',True,56.34]
# 1. alu
# 2.pato

# print(a[2])

# for i in a:
#     print(i)

# print(len(a))

# for i in range(len(a)):
#     print(i,a[i])

# a = [54,56,'Bangladesh',True,56.34,True]
# a.append('India')
# print(a.index('Bangladesh'))
# a.insert(2,'india')
# a.remove(56.34)
# a.pop(2)
# print(a.count(True))
# b = a.copy()
# b.pop(2)
# b.clear()
# print(a)
# print(b)

# a = [4,6,3,4,1,2]
# a = ['a','b','d','c']
# a = [54,56,'Bangladesh',True,56.34,True]
# a.sort()
# a.reverse()
# b = [34,56,678]
# a.extend(b)
# print(a)
# print(type(b))
# a = (54,56,'Bangladesh',True,56.34,True)
# print(type(a))

# print(a.index('Bangladesh'))
# print(a.count(True))

# b = list(a)
# print(type(b))
# b.pop(2)
# a = tuple(b)
# print(b)
# print(a)

# a = {54,56,'Bangladesh',True,56.34,True}
# b  = {5,2,3}
# print(type(a))

# print(a)
# b = a.copy()
# a.add('apple')
# print(b)
# a.clear()
# a.discard('Bangladesh')
# a.remove('Bangladesh')
# a.pop()
# a.update(b)
# print(a)

# a = {2,3,4,5}
# b = {5,6,3,2}

# c = a.difference(b)
# c = b.difference(a)
# c = a.intersection(b)
# c = a.union(b)
# print(c)

# a = { 'name':'Rahim','age':23,'Roll':56 }

# print(type(a))

# print(a['age'])

# print(a.keys())
# print(a.values())
# a.clear()
# b = a.copy()
# print(b)
# a.update({'subject':'Python'})
# a.pop('name')
# print(a)

# for i in a:
#     print(i,':',a[i])

# b = a.get('name')
# print(b)
# b = a.items()

# print(b)

# a = {
#     'name': 'Rahim',
#     'age' : 23,
#     'roll' : 45
# }
# print(a)

# for key, value in a.items():
#     print(key,value)



# a = [5,3,6,8,9]
# a.sort() # a = a.sort()
# print(a)
    
# def rahim():
#     print(5 +2)

# rahim()

# def addition(a=5,b=4):
#     print(a + b)

# # addition(5,4)
# addition(23)

# def addition(*a):
#     # return sum(a)
#     print(sum(a))

# num = []

# for i in range(3):
#     num1 = float(input(f'Enter A Number {i + 1} :'))
#     num.append(num1)
# while True:

#     num1 = float(input(f'Enter A Number :'))
#     if num1 != 0:
#         num.append(num1)
#     if num1 == 0:
#         break

# print(num)

# addition(*num)
# result = addition(*num)

# # print(result)
# print(addition(*num))

# def addition(*a):
#     print(sum(a)) 

# addition(23,22,56,89)

# x = (3,5,6)

# print(sum(x))


# def factorial(n):
#     if n == 0 or n == 1:
#     # if n >= 1 :
#         return 1
#     else:
#         return n * factorial(n-1)
    

# result = factorial(5)
 # 5 * 4 * 3 *  2 * 1
# a = int(input("Enter A Number : "))
# print(factorial(a))

# def addition(a):
#     # print(a +10)
#     return a +10

# result = addition(23)

# print(result)

# result = lambda a: a + 10

# print(result(12))

# a = (12,34,[56,58,2])
# a[2].append(4)
# print(a)

# age = 17

# status = 'Adult' if age >= 18 else 'Minor'

# print(status)

# a = [i for i in range(5)]

# print(a)

# x =  lambda *a: sum(a)

# print(x(12,34,56,56,56,56))


# a = open('My_file.txt', 'r')

# print(a.read())

# a = open('My_file.txt', 'w')
# a = open('My_file.txt', 'x')
# b = '''Lorem Ipsum is simply dummy text of the 
# printing and typesetting industry. Lorem Ipsum has been 
# the industry's standard dummy text ever since the 1500s,
#  when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

# a.write(b)
# a = open('My_file.txt', 'r')
# print(a.read())

# while True:
    
#     try:
#         x = int(input('Enter A Number : '))
#         if x == 0:
#             break
#         for i in range(1,11):
#             print(f'{x} X {i} = {x * i}')
#     except Exception as e:
#         # print('Invalid Input Try Again')
#         print(e)


# a = open('E:/Universal IT/My_file.txt', 'r')
# print(a.read())

# try:
#     a = open('E:/Universal IT/My_file.txt', 'x')
#     try :
#         a.write('I Love Dhaka')
#     except:
#         print('Not Done')
#     finally:
#         a = open('E:/Universal IT/My_file.txt', 'r')
#         print(a.read())
#         a.close()
# except Exception as e:
#     print(e)


# def calculator():
#     print('Simple Calculator')
#     print('Operators : + - * /')

#     num1 = float(input('Enter A Number :'))
#     operator = input('Enter A Operator :')
#     num2 = float(input('Enter A Number :'))

#     if operator == '+':
#         print(f'Result : {num1 + num2}')
#     elif operator == '-':
#         print(f'Result : {num1 - num2}')

# while True:
#     calculator()
#     user_input = input("Do You Want To continue 'Yes' or 'No' :").lower()
#     if user_input == 'yes':
#         continue
#     elif user_input == 'no':
#         break
#     else:
#         print('Invalid Input Try again')


# def A(name):
#     def B():
#         print(f'Hello {name}')
#     B()


# A('Rahim')

import datetime
import os
import turtle
import newforlder
# import newforlder.index_2

from newforlder import *
import newforlder.main
# a = datetime.datetime.now()
# print(a)
# print(a.strftime('%A'))
# print(a.strftime('%d'))
# print(a.strftime('%b'))
# print(a.strftime('%B'))
# print(a.strftime('%y'))
# print(a.strftime('%Y'))
# print(a.strftime('%X'))
# print(a.strftime('%x'))
# print(a.strftime('%C'))

# os.mkdir('ABCD')

# os.rmdir('ABCD')

# a = os.listdir('.')
# os.rename('New Text Document.txt','new_name.txt')

# print(a)

# print(os.path.exists('new_name.txt'))

# screen = turtle.Screen()

# t = turtle.Turtle()

# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# screen.mainloop()

# t.circle(100)

# screen.mainloop()

# x = newforlder.index_2.a

# print(x)

# t = turtle.Turtle()

# t.hideturtle()

# t.penup()
# t.goto(0,0)
# t.color('red')

# t.write('Hello, Turtle!', align='center', font=("Arial",24,'bold'))

# turtle.done()

# t.penup()
# t.goto(-100,100)
# t.pendown()
# t.goto(100,-100)
# turtle.done()

# t.penup()
# t.goto(-50,50)
# t.pendown()
# t.circle(100)

# t.penup()
# t.goto(80,-130)
# t.pendown()
# t.circle(100)
# turtle.done()


# class MyClass:
#     a = 10

    # def myfunc(self):
    #     print('Hello')


# x = MyClass()

# print(x.a)

# x.myfunc()

# class Studnet:
#     def __init__(self,name,age):
#         self.x = name
#         self.y = age
#         # print(self.x,self.y)
# student = Studnet('Rahim',45)

# print(student.x)
# print(student.y)


# class Namta:
#     def __init__(self,num):
#         for i in range(1,11):
#             print(f"{num} X {i} = {num* i}")

# num2 = int(input('Enter A Number :'))
# namta = Namta(num2)
# Namta(num2)


# class Parent:
#     a = 10
#     b = 15
#     def myfunc(self):
#         print('Hello')

# class Child(Parent):
#     x = 34
#     y = 4554
#     def myfun_2(self):
#         print('World')


# parent = Parent()

# child = Child()

# child.myfunc()

# class Dog:
#     def speak(self):
#         return "Woof!"
    
# class Cat:
#     def speak(self):
#         return "Meow!"

# class Cow:
#     def speak(self):
#         return "Moo!"

# animal = [Dog(),Cat(),Cow()]

# for i in animal:
#     print(i.speak())

# dog = Dog()
# cat = Cat()
# cow = Cow()

# def animal_sound(animal):
#     print(animal.speak())

# animal_sound(dog)
# animal_sound(cat)
# animal_sound(cow)

# class Student:
#     def __init__(self,name):
#         self.x = name
#         print(f"{self.x} has been Created")
    
#     def __del__(self):
#         print(f"{self.x} has been Destroyed")

# student = Student('Rahim')

class Logger:
    def __init__(self,filename):
        self.file = open(filename,'w')
        self.file.write("This is Our Test Case.")
        print("Write Started")
    
    def log(self,masssage):
        self.file.write(masssage + '\n')
    
    def __del__(self):
        self.file.write('End' + '\n')
        self.file.close()
        print('File Has Been Closed')

loger = Logger('new_name.txt')
# loger.log('This is The Masages')
# del loger
