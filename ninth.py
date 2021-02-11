                                  # all() and any() function

# number1 = [2,4,6,8,10]

# name = []
# for num in number1:
#     name.append(num%2 == 0)

# print(name)                              # ------> [True,True,True,True,True]

                  # OR

# number1 = [2,4,6,8,10]

# print(all([num%2 == 0 for num in number1]))# ------> True

# number1 = [2,4,5,8,10]
# print(any([num%2 == 0 for num in number1]))

                                  
                                    # EXERCISE - 1
# def my_sum(*args):
#     if all((type(arg) == int or type(arg) == float for arg in args)):
#         total = 0
#         for num in args:
#             total += num
#         return total
#     else: 
#         return 'worng input'

# print(my_sum(1,2,3,4,5))
# print(my_sum(1,2,3,4,5,'anubhav',['anubhav']))


                                      # sorted function

# sort func is for list and sorted func is for dict and tuple and sets.

# fruits = ('mango','apple','banana')      # -----> it gives list.
# print(sorted(fruits))
# print(fruits)

# guitars = [
#     {'m1' :' g1', 'price':500},
#     {'m2': 'g2', 'price':150},
#     {'m3': 'g3', 'price':100}
# ]

# print(sorted(guitars,key = lambda d: d['price']))             # -------> it gives list.


                                 # imp things
# some extra function .
# print(sum.__doc__)

# or

# we can write it doc in b/w '''     '''

# help function 
# print(help(len))

                                    # important
                                    # pre decorator intro
# def square(a):
#     return a**2

# s = square
# print(s(2))


                                    # function as argument

# l = [1,2,3,4]

# def square(n):
#     return n**2

# def my_map(func,l):
#     new_list = []
#     for i in l:
#         new_list.append(func(i))
#     return new_list

# # my_map = list(map(square,l))

# print(my_map(square,l))
# # print(my_map)

# def my_map(func,l):
#     return [func(i) for i in l]                              # by list comprehension.

# print(my_map(lambda a:a**3, [1,2,3,4]))



                         # func returning func or closure func or first class func

# def outer_func(msg):
#     def inner_func():
#         print(f'message is {msg}')
#     return inner_func

# variable = outer_func('yo! bro')
# variable()


                                     # EXERCISE - 1
  
# def to_power(x):
#     def calc_power(n):
#         return x**n
#     return calc_power

# cube = to_power(2)
# print(cube(3))

# square = to_power(4)
# print(square(2))

# num = int(input("enter a num : "))
# power = int(input("enter the power : "))

# ss = lambda x,y : x**y
# print(f"answer is = {ss(num,power)}")

