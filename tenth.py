                                    # decorators
# enhance the functionality of other function 

# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awesome')
#         any_function()
#     return wrapper_function

# @decorator_function                                         # easy way.
# def func():
#     print('this is function')

# func()


                                # or


# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awesome')
#         any_function()
#     return wrapper_function

                                 
# def func():
#     print('this is function')

# func1 = decorator_function(func)                                # long way.
# func1()



# def decorator_function(any_function):
#     def wrapper_function(*args, **kwargs):
#         print('this is awesome')
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function                                       
# def func(a):
#     print(f'this is function {a}')                             # func returning something.

# func(5)

# @decorator_function
# def add(a, b):
#     return a + b

# print(add(2,3))


# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         ''' this is wrapper function '''
#         print('this is awesome')
#         return any_function(*args, **kwargs)                     # for doc tools.
#     return wrapper_function

# @decorator_function
# def add(a, b):
#     ''' this is add function '''
#     return a + b

# print(add.__doc__)
# print(add.__name__)


                                   # important example

# from functools import wraps
# def print_function_data(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         print(f'you are calling {add.__name__}')
#         print(add.__doc__)
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @print_function_data
# def add(a,b):
#     '''this add two numbers'''
#     return a+b

# print(add(3,4))


                                    # very important EXERCISE 

# from functools import wraps                                    
# import time
# def calculate_time(function):
#     @wraps(function)
#     def wrapper_function(*args):
#         print(f'executing {function.__name__}')                      # ***imp***
#         t1 = time.time()
#         returned_value = function(*args)
#         t2 = time.time()
#         total_time = t2-t1
#         print(f'it took {total_time} in executing')
#         return returned_value
#     return wrapper_function

# @calculate_time
# def func(n):
#     return [i**2 for i in range(1,n+1)]

# print(func(10))
    


                                      # important EXAMPLE
# from functools import wraps
# def only_int_allow(function):
#     def wrapper_function(*args, **kwargs):
#         data_type = []
#         for arg in args:                                    
#             data_type.append(type(arg) == int)
#         if all(data_type):
#             return function(*args, **kwargs)
#         else:
#             return 'invalid argument'
#     return wrapper_function

# @only_int_allow
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_all(1,2,3,4,5))

        
                                # above example by another way

# from functools import wraps
# def only_int_allow(function):
#     def wrapper_function(*args, **kwargs):
#         if all([type(arg) == int for arg in args]):
#             return function(*args,**kwargs)
#         return 'invalid argument'
#     return wrapper_function

# @only_int_allow
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add_all(1,2,3,4,5))


                                # decorators with argument important

# from functools import wraps
# def only_data_type_allow(data_type):
#     def decorator_function(function):
#         @wraps(function)
#         def wrapper_function(*args,**kwargs):
#             if all([type(arg) == data_type for arg in args]):
#                 return function(*args,**kwargs)
#             return 'invalid argument'
#         return wrapper_function
#     return decorator_function


# @only_data_type_allow(str)
# def string_join(*args):
#     string = ''
#     for i in args:
#         string += i
#     return string

# print(string_join('anubhav','choudhary'))

