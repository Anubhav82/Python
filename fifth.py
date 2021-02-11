                                                   # dictionaries
# we use dictionaries because of limitations of lists, lists are not enough to represent real data.

# example
# user = {'name' : 'anubhav', 'age' : 20}
# print(user)
# print(type(user))

# user_info = dict(name = 'anubhav', age = 20)
# print(user_info)

# Creating a Dictionary 
# with each item as a Pair 
# Dict = dict([(1, 'Geeks'), (2, 'For')]) 
# print("\nDictionary with each item as a pair: ") 
# print(Dict) 

# Creating a Nested Dictionary  
# as shown in the below image 
# Dict = {1: 'Geeks', 2: 'For',  
#         3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}} 
  
# print(Dict)  

# how to access dictionaries data.
# there is no indexing.

# user_info2 = {'name' : 'anubhav',
#               'age' : 20,
#               'fav_movie' : ['kimi no na wa', 'spirited away'],                       # list inside dictionaries.
#               'fav_song' : ['eryday', 'intentions']
# }
# print(user_info2)
# print(user_info2['name'])
# print(user_info2['fav_song'])

                        # OR

# print(user_info2.get('name'))
# print(user_info2.get('names'))             # it gives None.
# print(user_info2.get('city', 'not found!'))

# how to add keys and values in our dictionary.
# user_info3 = {}
# user_info3['name'] = 'anubhav'
# user_info3['age'] = 20
# print(user_info3)


# In keyword and iterations in dictionary.
# user_info = {'name' : 'anubhav',
#               'age' : 20,
#               'fav_movie' : ['kimi no na wa', 'spirited away'],                      
#               'fav_song' : ['eryday', 'intentions']
# }


# check if key exist in dictionary

# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')



# check if value exist in dictionary

# if 'anubhav' in user_info.values():
#     print('present')
# else:
#     print('not present')



# loops in dictionaries.

# for i in user_info:
    # print(i)

# printing valuses.
# for i in user_info:
#     print(user_info[i])
                
                # OR

# for i in user_info.values():
#     print(i)


                        # values method

# user_info_values = user_info.values()                            # type dict_values.
# print(user_info_values)

                        # keys method

# user_info_keys = user_info.keys()                                # type dict_keys.
# print(user_info_keys)
# print(type(user_info_keys))


# user_info_keys = user_info.keys()
# print(list(user_info_keys))


                        # item method
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))


# for key, values in user_info.items():
    # print(f"key is {key} and value is {values}")


# user_info = {'name' : 'anubhav',
#               'age' : 20,
#               'fav_movie' : ['kimi no na wa', 'spirited away'],                      
#               'fav_song' : ['eryday', 'intentions']
# }

                                               # pop method
# popped_item = user_info.pop('fav_song')
# print(popped_item)
# print(type(popped_item))                                                 # it will return popped item in list.
# print(user_info)

                                               # popitem method
# popped_item = user_info.popitem()
# print(popped_item)
# print(type(popped_item))                                                 # it will return popped item in tuple.
# print(user_info)


                                               # update method
# more_item = {'name' : 'anubhav choudhary','state' : 'm.p'}
# user_info.update(more_item)
# print(user_info)


                                            # clear method
# d = {'name':'anubhav','age':20}
# d.clear()
# print(d)


                                            # copy method
# d = {'name':'anubhav','age':20}
# d1 = d.copy()
# print(d1)


                                         # EXERCISE - 1
# num = int(input("enter the number : "))

# def cube_finder(n):
#     cube = {}
#     for i in range(1,n+1):
#         cube[i] = i**3
#     return cube

# def cube_finder(num):
#     return {i : i**3 for i in range(1,num+1)}

# print(cube_finder(num))

                                      # WORD COUNTER
# def word_counter(s):
#     count = {}
#     for char in s:
#         count[char] = s.count(char)
#     return count

# print(word_counter('anubhav'))

# def char_count(s):
#     count = {}
#     for i in s:
#         count[i] = s.lower().count(i)
#     return count


# name = input("Enter a name : ")
# print(char_count(name))
                                      # EXERCISE - 2
# name = input("What is your name? ")
# age = input("What is your age? ")
# fav_movies = input("your favorite movies seperated by comma ")
# fav_songs = input("your favorite songs seperated by comma ")      

# user = {}
# user['name']=name
# user['age']=age
# user['fav_movies']=fav_movies
# user['fav_songs']=fav_songs

# print(user)
# for key, value in user.items():
#     print(f"{key} : {value}")

                                

                                 # SETS
# set data type
# unorderd collection of unique items

# s = {1,2,3,2,5,5,5,7,3,6,9,8,1,4}
# print(s)

# l = [1,2,3,4,5,6,7,8,9]
# s = set(l)
# s = set('anubhav')
# s = set({})
# print(s)

# s = set(l)
# print(s)
# s.add(10)
# print(s)
# s.remove(4)
# print(s)
# s.discard(777)
# print(s)
# s.clear()
# s1 = s.copy()
# print(s1)

# s1 = [1,2,3,4]
# s2 = [3,4,5,6]

# s3 = set(s1)
# s4 = set(s2)

# print(list(s3&s4))

# union = s1|s2
# print(union)

# intersection = s1 & s2
# print(intersection)

# l = [1,2,3,4,5,5,5,5]
# l1 = list(set(l))
# l1.remove(max(l1))
# print(l1)

                                    #  converting a string in a dictionary
# test_str = "Gfg = 1, Good = 2, CS = 3, Portal = 4"
# res = {key : int(value) for key,value in (item.split("=") for item in test_str.split(","))}
# print(res)

                                     # converting a list string to dict.
# test_string = '[Nikhil:1, Akshat:2, Akash:3]'
# print("The original string : " + str(test_string))  
# res = {sub.split(":")[0]: sub.split(":")[1] for sub in test_string[1:-1].split(", ")} 
# print("The dictionary after extraction is : " + str(res)) 

