                                     # LAMBDA EXPRESSION
# def add(a,b):
#     return a+b
# print(add(1,2))


# add = lambda a,b : a+b
# print(add(1,2))

# IMPORTANT IN LAMBDA
# 1. filter
# 2. map
# 3. reduce (functools)
# 4. enumerate                                     # geeks for geeks
# 5. accumulate (itertools)
# 6. operator (operator)
# 7. datetime (datetime)
# 8. zip

               # lambda expression practice 

# def is_even(a):
#     return a%2 == 0                                      # simple

# print(is_even(4))


# is_even2 = lambda a : a%2 == 0                          # by lambda expression
# print(is_even2(2))


# def last_char(s):
#     return s[-1]                                         # simple
# print(last_char('anubhav'))


# last_char = lambda s : s[-1]
# print(last_char('anubhav'))                              # by lambda expression

# l = [1,2,3,4,5,6,7,8,9]

# cube = filter(lambda i : i%3 == 0,l)
# for i in cube:
#     print(i,end = " ")

# lambda expression with if else
# def func(s):                                          
#     if len(s)>5:                                          # def func(s):
#         return True                        # OR                 return len(s)>5          
#     else:                                                 # print(func('anubhav'))
#         return False                                                  

# print(func('anubhav'))


# func = lambda s: True if len(s)>5 else False         # OR      # func = lambda s: len(s)>5
# print(func('anubhav'))                                         # print(func('anubhav'))


# a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]

# filtered = filter (lambda x: x % 2 == 0, a)  
# print(list(filtered))

# maped = map (lambda x: x % 2 == 0, a)  
# print(list(maped))


#Important
# Python program to 
# print current date 
  
# from datetime import date 
  
# # calling the today 
# # function of date class 

# today = date.today() 
  
# print("Today's date is", today) 

# year = lambda x: x.year
# month = lambda x: x.month
  
# print(year(today))
# print(month(today))
# # Printing date's components 
# print("Date components", today.year, today.month, today.day) 

                                # EMUNERATE FUNCTION

# example without enumerate function
# we want to print
# 0 -----> 'abc'
# 1 -----> 'anubhav'

# names = ['abc','abcdef','anubhav']
# pos = 0
# for name in names:
#     print(f"{pos} -----> {name}")
#     pos += 1

# with enumerate function

# names = ['abc','abcdef','anubhav']
# for pos, name in enumerate(names):
#     print(f"{pos} -----> {name}")

                           
                                        # EXERCISE - 1
# def find_pos(l,s):
#     for pos, name in enumerate(l):
#         if name == s:
#             return pos
#     return -1

# list1 = ['abc','abcdef','anubhav']
# print(find_pos(list1,'anubhav'))




                                       # map function
# num = [1,2,3,4]
#     square1 = []
#     for i in num:
#         square1.append(i**2)                               # by simple method
# print(square(num))


# num = [1,2,3,4]
# square = [i**2 for i in num]                               # by list comprehension
# print(square)


# l = [1,2,3,4,5]
# print(list(map(lambda i : i**2,l)))                       # by map and lambda


# num = [1,2,3,4]
# def square(i):
#     return i**2                                            # by map function
# squares = list(map(square, num))
# print(squares)

# square1 = map(square, num)
# for i in square1:
#     print(i)


# num = [1,2,3,4]                                 
# squares = list(map(lambda a : a**2, num))                  # by lambda
# print(squares)


# loop in map function

# names = ['abs','ajddf','sojdjff']
# length = map(len, names)

# for i in length:
#     print(i)


# list1 = list(map(int,input("enter numbers : ").split(",")))

# even = filter(lambda i : i%2 == 0,list1)
# print(even)
# # for i in even:
# #     print(i)
                                      # ZIP FUNCTION
# user_id = ['user1','user2','user3']
# names = ['anubhav','sunny','rohit']
# last_names = ['choudhary','choudhary','sharma']            # it takes zeroth element of all lists
# num = zip(user_id,names,last_names)                           # and put or zip them in a tuple.

# for i in num:
#     print(i)

# print(list(zip(user_id,names,last_names)))
# print(dict(zip(user_id,names)))

# it gives items in tuple


# l = [(1,2),(3,4),(5,6),(7,8)]
# # * operator with zip                        # * operator unzip the ziped item.

# l1, l2 = zip(*l)
# print(list(l1))
# print(l2)

                                     # EXERCISE - 1

# l1 = [1,3,5,1]
# l2 = [2,4,6,8]
# new_list = [] 

# for pair in zip(l1,l2):
#     new_list.append(max(pair))

# print(new_list)


                                     # Advance example
# return average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3

# def average_finder(l1,l2):
#     average = []
#     for pair in zip(l1,l2):
#         average.append(sum(pair)/len(pair))
#     return average

# print(average_finder([1,2,3],[4,5,6]))
                            
                             # OR

# make it for any number of list.

# def average_finder(*args):
#     average = []
#     for pair in zip(*args):                       # here if we use args it takes all in tuple
#         average.append(sum(pair)/len(pair))       # so we use * args to take as seperate element.
#     return average

# print(average_finder([1,2,3],[4,5,6],[7,8,9]))
                          
                             # OR

# average_finder = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
# print(average_finder([1,2,3],[4,5,6],[7,8,9]))


# python code to demonstrate working of reduce() 
  
# # importing functools for reduce() 
# import functools 
  
# # initializing list 
# lis = [ 1 , 3, 5, 6, 2, ] 
  
# # using reduce to compute sum of list 
# print ("The sum of the list elements is : ",end="") 
# print (functools.reduce(lambda a,b : a+b,lis)) 
  
# # using reduce to compute maximum element from list 
# print ("The maximum element of the list is : ",end="") 
# print (functools.reduce(lambda a,b : a if a > b else b,lis)) 



# python code to demonstrate working of reduce() 
# using operator functions 
  
# # importing functools for reduce() 
# import functools 
  
# # importing operator for operator functions 
# import operator 
  
# # initializing list 
# lis = [ 1 , 3, 5, 6, 2, ] 
  
# # using reduce to compute sum of list 
# # using operator functions 
# print ("The sum of the list elements is : ",end="") 
# print (functools.reduce(operator.add,lis)) 
  
# # using reduce to compute product 
# # using operator functions 
# print ("The product of list elements is : ",end="") 
# print (functools.reduce(operator.mul,lis)) 
  
# # using reduce to concatenate string 
# print ("The concatenated product is : ",end="") 
# print (functools.reduce(operator.add,["geeks","for","geeks"])) 



# # python code to demonstrate summation  
# # using reduce() and accumulate() 
  
# # importing itertools for accumulate() 
# import itertools 
  
# # importing functools for reduce() 
# import functools 
  
# # initializing list  
# lis = [ 1, 3, 4, 10, 4 ] 
  
# # priting summation using accumulate() 
# print ("The summation of list using accumulate is :",end="") 
# print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
  
# # priting summation using reduce() 
# print ("The summation of list using reduce is :",end="") 
# print (functools.reduce(lambda x,y:x+y,lis)) 



# if __name__ == '__main__':
#     n = int(input("e :"))
#     for _ in range(n):
#         name = [a,b,c,d]
#         score = [1,2,3,3]
#         a = zip(name,score)
#         score.remove(min(score))
#         for i in a:
#             if i[1] == min(score):
#                 print(i[0])
        
# n = int(input())
# l = [int(i) for i in range(1,n+1)]
# p = 1
# for i in l:
# 	p *= i

# print(p)

# l = list(map(int,input().split()))             # it works*******
# l = [int(input()) for i in range(4)]
# print(l)

# practice****************

# L = int(input())
# N = int(input())
# for i in range(N):
#     W,H = input().split() 

#     if int(W)==int(H) and int(W)>=L and int(H)>=L:
#         print("ACCEPTED")
#     elif int(W)<L or int(H)<L:
#         print("UPLOAD ANOTHER")
#     elif int(W)>=L or int(H)>=L:
#         print("CROP IT")

# 180
# 5
# 640 480
# 120 300
# 180 180
# 400 400
# 200 180

# n = int(input())
# for i in range(n):
#     SH,SM,EH,EM = input().split()
#     difh = int(EH)-int(SH)
#     difm = int(EM)-int(SM)
    

#     print(str(difh)+" "+str(difm))