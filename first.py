                             # PRINT and calculation
# print('hello "hi" world')
#print("hey 'hello'")
#print('I \'m Anubhav')
# print('line a\n   line a')  
# print("hello \\")
# print("hi \\n hey")
#print("\U0001F618")
#print(3+5*5)
#print(5//2)
# print(5/2)
# print(3**3)
# print(round(2**0.5,3))

                             # VARIABLES AND STRING AND CONCATINATION
# _name = 'Anubhav'
# print(_name)
# print('anubhav choudhary')
# First_name ="Anubhav "
# Last_name ="Choudhary"
# print (First_name +" "+ Last_name)
# print (First_name + Last_name)
# print (First_name + "34")

                            # USER INPUT
# input function
# name = input("type your name")
# print ("your name is " + name)
# age = input("your age")
# print ("your age is " + age)
                            # MORE THAN ONE INPUT IN ONE LINE
# name, age = input("enter your name and age ").split()        #or we can change space() with (,) by split(",")
# print(name)
# print(age)

                            # int(),float(),str() FUNCTION
# number_one = int(input("enter first number"))
# number_two = int(input("enter second number"))
# total = number_one + number_two
# print(total)
# str
# 4---->"4"
# int
# "4"---->4
# float
# "4"---->4.0
# num = 34
# n = num *2
# print(float(n))

                            # MORE VARIABLES
# name, age = "Anubhav,", "20"
# print("hello " + name +" "+ "your age is "+ age)
# x=y=z=1
# print(x+y+z)

                             # STRING FORMATTING
# name = "Anubhav"
# age = 20
# print("hello " + name + " your age is " + str(age) + ".")                  # python 2
# print("hello {} your age is {}.".format(name, age))                        # python 3
# print(f"hello {name} your age is {age}.")                                  # python 3.6(best)

                            # EXERCISE - 1 -Average
# one, two, three = input("Enter 3 numbers ").split()
# print(f"average of 3 numbers : {(int(one) + int(two) + int(three)) / 3}")

# a,b,c = input("num : ").split()
# print(int(a)+int(b))
                            # STRING INDEXING AND SLICING
# language = "python"
# p = 0 , -6
# y = 1 , -5
# t = 2 , -4 
# h = 3 , -3
# o = 4 , -2
# n = 5 , -1
# print(language [2])
# print(language [0:4])
# print(language [::-1])                           # Step Argument (by this we can reverse the string.)

                             # STRING AND STRIP METHODS
# name = "AnUbHaV cHoUdHaRy"
# length = len(name)
# 1.
# print(length)                len() function

# 2.
# print(name.lower())          lower() method

# 3.
# print(name.upper())          upper() method

# 4.
# print(name.title())          title() method

# 5.
# print(name.lower().count("a"))       #count() method


#IPMORTANT$$$$$$$$$$$$$$$$$$$$$
# s = "anubhav"
# for i in s:
#     print(ord(i))
#     print(ord(i)-96)

# Example
# s = input()
# sum = 0
# for i in s:
#     sum+= ord(i)-96
# print(sum)

# STRIP
# name.lstrip() # method                        #To remove left spaces.
# name.rstrip() # method                        #To remove right spaces.
# name.strip() # method                         #To remove both sides spaces.
# name.replace(" ", "",)                      #To remove spaces between the name or string.

# convert string into list.
# user_info = "anubhav, 20, 33".split(",")
# print(user_info)

# JOIN
# convert list into string.
# user_info = ["anubhav, 20, 33"]
# print(",".join(user_info))

# IMPORTANT
# s = "AnUbHaV 56"
# print("".join([i.lower() if i.isupper() else i.upper() for i in s ]))

# simple method
# s = "AnUBhaV"
# print(s.swapcase())

                                        #  EXERCISE - 2 - STRING METHOD
# name, char = input("Enter your name and one charcter ").split(",")               # **Strings are immutable means if they created they can never be replaced.
# print(len(name.strip()))
# print(f"character count : {name.strip().lower().count(char.strip().lower())}")

# REPLACE METHOD Eg:-
# string = "She is beautiful and she is a good dancer"
# print(string.replace("is","was",2))                            # for both is.[It replaces is by was]

# FIND METHOD Eg:-
# string = "She is beautiful and she is a good dancer"
# is_pos1 = string.find("is")                                     # is_pos1----> number
# is_pos2 = string.find("is", is_pos1 + 1)                        # It gives the position of 2nd is 
# print(is_pos2)
# print(is_pos1)

                                       # CENTER METHOD
# name = "Anubhav"
# print(name.center(11,"$"))
# naam = input("Enter your name : ")                               
# print(name.center(len(name) + 20,"*"))                         # For making heading or printing something at center.

# NOTE
# name = "Anubha"
# name = name + "v"
# print(name)
# age = 20
# age += 1
# print(age)

# arr = list(input('enter : ').split())
# print(arr)
# r = max(arr)
# while r == max(arr):
#     arr.remove(max(arr))
# print(max(arr))


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     for name,scores in student_marks.items():
#         if query_name == name:
#             percent = round(sum(scores)/3,3)
#             print(percent)


# def fun1(a,b,c):
#     print(a,b,c)

# def fun2(*args):
#     fun1(args)

# fun2(1,2,3)


# A sample program to demonstrate unpacking of 
# dictionary items using ** 
# def fun(a, b, c): 
# 	print(a, b, c) 

# A call with unpacking of dictionary 
# d = {'a':2, 'b':4, 'c':10} 
# fun(**d) 


# name = "ANuBhav    cHoUdHaRy"
# age = int(input("enter age : "))
# print(name.lower().title().center(len(name)+ 200," "))
# print(str(age) + "g")
# print(name.replace("H"," "))
# print(len(name))
# print(len(name.strip())).

# naam = input("Enter name : ")
# name = naam.lower()
# while 1:
#     char = input("Enter a char : ")
#     if char in name:
#         print(f"{char} = {name.count(char)}")

#     else:
#         print("not found")

l = [1.0,0,0,0,0]
if 0 in l:
    l.remove(0)
print(l)
