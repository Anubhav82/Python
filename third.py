                                           # FUNCTION
# name = "anubhav"
# print(len(name))

# def add(a , b):                                         # here a,b are parameter and x,y are argument.
#     return a+b
# x = int(input("first no. : "))
# y = int(input("second no. : "))
# print(add(x , y))                                           

# def add(a , b):
#     return a+b
# x = input("first name : ")
# y = input("Last name : ")
# print(f"sum is : {add(x , y)}")

   # Example
# def last_char(name):
#     return name[-1]

# Name = input("Enter your name : ")
# print(last_char(Name))

   # Example
# def even_odd(num):
#     if num%2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# num = int(input("Enter a num : "))
# number = even_odd(num)
# print(number)

                 # OR

# def is_even(num):
#     return num%2 == 0
                                                             # it checks equality and give true or false
# print(is_even(8))     

# Example
# def song():
#     return "happier"                                       # without any parameter and argument.

# print(song())

                                        # EXERCISE - 1
# def bigger(num1,num2):
#     if num1 < num2:
#         return num2
#     else:
#         return num1

# num1,num2 = input("Enter two numbers which are seperated by (,) : ").split(",")
# print(f"bigger number between them : {bigger(int(num1),int(num2))}")

# IN 3 NUMBERS

# def bigger(num1,num2,num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3

# num1,num2,num3 = input("Enter three numbers which are seperated by (,) : ").split(",")
# print(f"bigger number between them : {bigger(int(num1),int(num2),int(num3))}")


                                    # EXERCISE - 2
# def is_palindrom(word):
#     word2 = word[::-1]                                        # palindrom means string = reverse string.
#     if word2 == word:
#        return "This word is palindrom."
#     else:
#         return "This word is not palindrom."

# word1 = input("Enter a word : ")
# print(is_palindrom(word1))

                                     # FIBONACCI SERIES
# 0 1 1 2 3 5 8 13 21 34

# def fibonacci(num):
#    a = 0
#    b = 1
#    if num == 1:
#       return a
#    elif num == 2:
#       print(a, b)
#    else:
#       print(a,b, end = " ")
#       for i in range(num-2):
#           c = a + b         #c= 1
#           a = b             #a= 1
#           b = c             #b= 1
#           print(b, end= " ")

# print(fibonacci(10))

                                    # DEFAULT PARAMETERS
# def num(x , y , z =6 ):                           #(x = 1, y , z = 3 )we can't do this
#    print(x,y,z)

# num(5,6)

# name = "anubhav"
# for i in name:
#    print(i)

# num = "23451"
# total = 0
# for i in num:
#    total += int(i)
# print(total)

# number = [1,2,33,45,6]
# print(number[::-1])

# num = input("enter numbers : ").split()                      # OR                        # num = input("enter numbers : ").split()   
# list1 = []                                                                               # print(list(map(int,num)))
# for i in num:
#    list1.append(int(i))
#    print(list1)


# num = [1,2,3,4,5,5,5]
# a = num.pop(max(num))
# print(a)
# num1 = set(num)
# num1.remove(max(num1))
# print(max(num1))


# l1 = ["anubhav","aaa"]
# l1.sort()
# print(l1)


# fruits=["orange","apple","watermellon","banana","kiwi","mango","kiwi","apple"]
# fruits.sort()
# print(fruits)