                                      # LIST COMPREHENSION
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print(square)


# square = [i**2 for i in range(1,11)]                 # by list comprehension.
# print(square)

# n = [1,2,3,4,5]
# negative = []
# for i in n:
#     negative.append(-i)
# print(negative)


# n = [1,2,3,4,5]
# negative = [-i for i in n]                           # by list comprehension.
# print(negative)


# names = ['Anubhav', 'Harshit', 'Sunny']
# name2 = []
# for i in names:
#     name2.append(i[0])
# print(name2)


# names = ['Anubhav', 'Harshit', 'Sunny']
# print([i[0] for i in names])                                  # by list comprehension.



                                     # EXERCISE - 1
# def reverse(n):
#     rev_element = []
#     for i in n:
#         rev_element.append(i[::-1])                              # reversing of elements.
#     return rev_element                                           # by normal method.

# name = ["abc","def","ghi"]
# print(reverse(name))


# def reverse(n):
#     return [i[::-1] for i in n]                                     # by list comprehension.
                                                                     
# print(reverse(['abc','def','ghi']))


# def reverse(l):
#     rev_ele = []
#     for i in range(len(l)):
#         poped_item = l.pop()
#         rev_ele.append(poped_item)
#     return rev_ele

# l = list(map(int,input("enter numbers :").split()))
# print(reverse(l))

# by simple method

# l = list(map(int,input("enter numbers :").split()))
# print(l[::-1])

# acending or decending

# l = list(map(int,input("enter numbers : ").split()))
# l1 = list(set(l))
# print(sorted(l1))

# print(l1[::-1])


                             # list comprehension with if statement
# numbers = list(range(1,11))
# num = []
# for i in numbers:                                         # by normal method
#     if i % 2 == 0:                                        # finding even numbers 
#         num.append(i)
# print(num)


# numbers = list(range(1,11))
# print([i for i in numbers if i%2 == 0])                    # by list comprehension.(even no.)
# print([i for i in numbers if i%2 != 0])                    # by list comprehension.(odd no.)
                   # OR
# print([i for i in range(1,11) if i%2 != 0])


                                    # EXERCISE - 2
# def num_to_string(l):
#     return [str(i) for i in l if (type(i) == int or type(i) == float)]    # change num into string.

# print(num_to_string(['anunhav',True,False,1,3,0.5]))                      # by list comprehension.



                          # list comprehension with if else statement
# num = [1,2,3,4,5,6,7,8,9,10]
# new_list = []
# for i in num:
#     if i%2 == 0:                                          # by normal method.
#         new_list.append(i**2)
#     else:
#         new_list.append(-i)
# print(new_list)


# num = [1,2,3,4,5,6,7,8,9,10]
# print([i**2 if i%2 == 0 else -i for i in num])                   # by list comprehension.


                            # list comprehension in nested list
# num = [[1,2,3],[1,2,3],[1,2,3]] # we have to print this.

# new = [[-i for i in range(1,4)] for j in range(3)]                # by list comprehension.
# print(new)



                            # DICTIONARY COMPREHENSION
# def cube_finder(n):
#     cube = {}
#     for i in range(1,n+1):                            # by normal method.
#         cube[i] = i**3
#     return cube

# print(cube_finder(10))


# cube1 = {num : num**3 for num in range(1,11)}                   # by dictionary comprehension.
# print(cube1)

# cube1 = {f"cube of {num}" : num**3 for num in range(1,101)}      # by dictionary comprehension.
# for k,v in cube1.items():
#     print(f"{k} == {v}")
# # print(cube1)                                        

# string = "anubhav"
# new = {char : string.count(char) for char in string}            # counting how many times char present.
# print(new)


                                # DICTIONARY COMPREHENSION WITH IF ELSE 
# odd_even = {i : ("even" if i%2 == 0 else "odd") for i in range(1,11)}
# print(odd_even)
#                            # OR

# odd_even = {f"{i}" : ("even" if i%2 == 0 else "odd") for i in range(1,11)}
# for k,v in odd_even.items():
#     print(f"{k} : {v}")





                               # SET COMPREHENSION
# s = {k**2 for k in range(1,11)}
# print(s)

# l = ['abc','def','ghi']
# s = {name[0] for name in l}
# print(s)



