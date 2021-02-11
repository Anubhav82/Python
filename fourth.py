                                            # LIST
# data structure
# List = ordered collection of items

# you can store anything in lists like int, float, string

# nums = list(range(1,11))
# print(nums)

# number=[1,2,3,4,5]
# print(number)
# print(number[1])

# words = ["word1", "word2", "word3"]
# print(words)
# print(words[:2])

# mixed=[1,2,0.4,'anubhav']
# mixed[1] = "one"
# print(mixed)
# mixed[1:] = "two"
# print(mixed)
# mixed[1:]= ["two", "three","four"]
# print(mixed)

                              # HOW TO ADD ITEMS IN OUR LIST (append)
# fruits = ["mango", "banana"]
# fruits.append("grapes")
# print(fruits)

# fruits = []
# fruits.append("apple")
# fruits.append("orange")
# print(fruits)

                                       # insert method
# fruit1=["orange","banana"]
# fruit1.insert(1, "apple")
# print(fruit1)

                                  # how to join two lists
# fruit1=["orange","banana"]
# fruit2 = ["mango", "banana"]
# fruits = fruit1+fruit2
# print(fruits)

                                       # extend method
# fruit1=["orange","banana"]
# fruit2 = ["mango", "banana"]
# fruit1.extend(fruit2)
# print(fruit1)
# fruit1.append(fruit2)                                  # it gives list inside another list.
# print(fruit1)

                                       # pop method
# fruits=["orange","banana","mango","kiwi","apple"]
#  fruits.pop()
#  print(fruits)

# fruits.pop(2)
# print(fruits)

                                        # DELETE METHOD
# fruits=["orange","banana","mango","kiwi","apple"]
# del fruits[2]
# print(fruits)

                                        # REMOVE METHOD
# fruits=["orange","banana","kiwi","mango","kiwi","apple"]
# fruits.remove("kiwi")
# print(fruits)

                                        # HOW TO CHECK
# fruits=["orange","banana","kiwi","mango","kiwi","apple"]
# if "kiwi" in fruits:
#     print("yes")

# count
# sort method
# sorted function
# reverse
# clear
# copy

# fruits=["orange","apple","watermellon","banana","kiwi","mango","kiwi","apple"]
# print(fruits.count("apple"))
# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)
# print(sorted(fruits))
# fruits_copy = fruits.copy()
# print(fruits_copy)
# fruits.clear()
# print(fruits)

                                        # SPLIT METHOD
# convert string into list.
# user_info = "anubhav, 20, 33".split(",")
# print(user_info)

                                        # JOIN METHOD
# convert list into string.
# user_info = ["anubhav, 20, 33"]
# print(",".join(user_info))

                                        # list inside another list
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for sublist in matrix:
#     for i in sublist:
#         print(i)

# matrix = [[1 ,2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix [2] [0])

                                       # making list negative
# number = [1,2,3,4,5,6,7,8,9,10]
# def negative_num(l):
#     negative = []
#     for i in l:
#         negative.append(-i)
#     return negative

# print(negative_num(number))

                                      # making list by range
# num = list(range(1,11))
# print(num)

                                      # EXERCISE - 1
# number = input("Enter your list : ").split(",")
# # number = list(range(1,11))
# def square_num(num):
#     square = []
#     for i in num:
#         square.append(i**2)
#     return square

# print(square_num(number))

                                       # EXERCISE - 2
# def reverse(n):
#     rev_num = []
#     for i in range(len(n)):
#         popped_item = n.pop()
#         rev_num.append(popped_item)                             # reversing of list.
#     return rev_num
# number=[1,2,3,4]
# print(reverse(number))

                                      # EXERCISE - 3
# def reverse(n):
#     rev_element = []
#     for i in n:
#         rev_element.append(i[::-1])                              # reversing of elements.
#     return rev_element

# name = ["abc","def","ghi"]
# print(reverse(name))

                                      # EXERCISE - 4
# def odd_even(l):
#     even_list = []
#     odd_list = []
#     for i in l:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)                               # it seperates the odd and even and put them in two different lists
#     output = [even_list, odd_list]                             # and put these lists in a single list.
#     return output

# num = [1,2,3,4,5,6,7,8,9]
# print(odd_even(num))

                                      # EXERCISE - 5
# def common(l1,l2):
#     same = []
#     for i in l1:
#         if i in l2:
#             same.append(i)                               # it gives same elements in lists.
#     return same

# num1 = [1,2,3,4,5]
# num2 = [1,2,6,7,8]
# print(common(num1,num2))

                                      # EXERCISE - 6
# def sublists(l):
#     count = 0
#     for i in l:
#         if type(i) == list:
#             count += 1                                    # it gives no. of lists present in a list.
#     return count

# list1 = [1,2,3,[1,2],[3,4,5]]
# print(sublists(list1))

                                    # min,max,and type functions
# num = [1,34,6]
# print(max(num))
# print(max(num)-min(num))

# list unpacking
# num = [1,34,6]
# a,b,c = num
# print(a,b)

# num =[1,2,3,4,[1,2],4.76]
# for i in num:
#     print(type(i)) 

    

                                                       # TUPLES
# example = ('orange','apple')
# num = (1,2,3,4)
# num = (1) this is not tuple.
# num = (1,) this is tuple.((,) is mandatory)

# tuple without parenthesis
# word = 'word1','word2','word3' (this is tuple.)

# tuple unpacking
# bts = ('jimmy','j-hope','rm')
# name1,name2,name3 = bts
# print(name2)

# no append, no insert, no pop, no reverse 
# tuples are faster and immutable

# we can use (count, index, len, min, max, sum)functions and slicing also. 

# list inside tuple
# favorites = ('save me',['boy with love','dope','fake love'])
# favorites[1].pop()
# favorites[1].append('DNA')                                                # we can use all function in the list inside a Tuple.
# print(favorites)


                                            # function returning two values
# def func(int1, int2):
#     add = int1 + int2
#     multiply = int1 * int2
#     return add, multiply

# print(func(2,3))                                                         # NOTE it will return tuple.
# add, multiply = func(2,3)                                                # we can store the returned value in different variables.
# print(add)
# print(multiply)


# nums = (1,2,3,4,5,6,7,8,9)
                                                                         # by this we can easly convert tuple into list and string.
# nums = list((1,2,3,4,5,6,7,8,9))
# print(nums)

# nums = str((1,2,3,4,5,6,7,8,9))
# print(nums)
# print(type(nums))
# print(nums[0])



                                                                                                          




                              


