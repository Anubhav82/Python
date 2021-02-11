                                      # *args
# def add(a,b):
#     return a+b

# def new_add(*args):
#     total = 0                                     # When we use *args it stores the value in tuple.
#     for i in args:
#         total += i
#     return total
# print(new_add(1,2,3,3,44,5,))

# when we give argument in list and tuple
# simply we have to do this
# l =[1,2,3,4]
# print(new_add(*l)) # to unpacking the list.


# def cube(n,l):
#     if l:
#         return [i**n for i in l]
#     else:
#         return "pass"

# list1= [1,2,3]
# num = 3  
# print(cube(num,list1))


#                                     # **kwargs
# def func(**kwargs):
#     for k,v in kwargs.items():                   # When we use *kwargs it stores the value in dictionary.
#         print(f"{k} : {v}")

# func(first_name = 'anubhav', last_name = 'choudhary')


#PADK

# parameters
# *args
# default parameters
# **kwargs

# def func(name, *args, last_name = 'unknowm', **kwargs):
#     print(name)
#     print(*args)
#     print(last_name)
#     print(**kwargs)

# func('anubhav', 1,2,3, a= 2,b=3)


                                      # EXERCISE - 1
# def func(l,**kwargs):
#     if kwargs.get('reverse_str') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]
# print(func(['anubhav', 'choudhary'],reverse_str = True))

