                                         # ERROR

# types of error 

# 1.syntax error
# def func:
    # pass

# name = 'anubhav'*

# indentation error
# def func():
    # print('hello')
#   print('word')

# name error
# print(func())         # func() is not defined.

# type error
# print(5 + 'anubhav')

# index error
# l = [1,2,3]
# print(l[4])

# value error
# s = 'abc'
# print(int(s))

# attribute ERROR
# l=[1,2,3]
# l.push('12')

# key error
# d = {'name':'anubhav'}
# print(d['age'])

                                     # raise error

# def add(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a + b
#     raise TypeError('oops you are passing wrong data type to function')

# print(add(2,'3'))

                                    # NotImplementedError/abstract method

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def sound(self):
#         raise NotImplementedError('you have to define sound() in subclass')

# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return 'bhow bhow'

# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return 'meow meow'

# doggy = Dog('boony','pug')
# print(doggy.sound())
# caty = Cat('rem','pursian')
# print(caty.sound())


                                      # Exception handling

# while True:
#     try:
#         age = int(input('enter your age : '))
#         break
#     except ValueError:
#         print('maybe you enter string instead integer try again.')
#     except:
#         print('unexpected error..')

# if age<18:
#     print('you can\'t play this game.')
# else:
#     print('you can play this game.')               


                                    # else and finally clause

# while True:
#     try:
#         num = int(input('enter a number : '))
#     except ValueError:
#         print('enter an integer !')
#     except:
#         print('unexpected error !')
#     else:
#         print(f'user input = {num}')
#         break
#     finally:
#         print('finally blocks.....')


                                         # EXERCISE - 1

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print('you cannot divide a number by zero !')
#     except TypeError:
#         print('number should be int or float')
#     else:
#         print('unexpected error')
# print(divide(10,'2'))


                                        # Custum exceptions
# class NameTooShortError(ValueError):
#     pass
# def validate(name):
#     if len(name) < 8:
#         raise NameTooShortError('name is too short')
#     else:
#         print(f'hello {naam}')

# naam = input('enter your name : ')
# validate(naam)


                                        # Debugging

# import pdb

# pdb.set_trace()
# name = input('enter your name : ')
# age = input('enter your age : ')
# print(f'{name} your age is {age}.')
# age2 = int(age) + 5
# print(f'{name} your age will be {age2} after 5 years.')


# l = to check which line is executing.
# n = to execute next line.
# c = to continue




