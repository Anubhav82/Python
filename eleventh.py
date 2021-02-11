                                     # generators
# generator function.
# def nums(n):
#     for i in range(1,n+1):
#         yield i

# print(nums(10))

# number = nums(10)
# for num in number:
#     print(num)


# memory (list) - [...........................]      list create all element in list thus it takes
#                                                                  more memory.

# memory (generator) - (1)       it takes 1 then when it calls again it delete 1 and take 2 in 
# memory (generator) - (2)            memory,generator takes less memory and time.
# memory (generator) - (3)


                                    # EXERCISE - 1

# def even_numbers(n):                                        # def even_numbers(n):   
#     for i in range(1,n+1):         #or                      #     for i in range(2,n+1,2):
#         if i%2 == 0:                                        #             yield(i)
#             yield(i)

# print(even_numbers(10))

# for num in even_numbers(10):                     # but if we did 
#     print(num , end=" ")                            # number = even_numbers(10):
#                                                     # for num in even_numbers(10):
# for num in even_numbers(10):                           # print(num , end=" ")
# print(num , end=" ")                            # we can call it only one time.                        



                                # generator comprehension

# it is just like list comprehension only we have to replace this [] with ().

# square =[i**2 for i in range(1,11)]   --------------> list (iterable)

# square = (i**2 for i in range(1,11))    # --------------> generator (iterator)
# print(square)

# for num in square:
#     print(num)