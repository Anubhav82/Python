                                       # IF STATEMENT
# age = 23
# if (age < 50):                                             # or if age < 50:
#  print("less")

# PASS
# x = 45
# if x<55:
#     pass                                                   # It gives no error.

                                      # IF ELSE STATEMENT
# age = int(input("Enter your age :"))
# if age<=14:
#     print("sorry you can't play")
# else:
#     print("continue")

                                    #  *************** while else statement**************

# i = 0                                      
# while i<4:
#     i += 1
#     print(i)
    
# else:
#     print('while_else')
  
                                      # EXERCISE - 1
# x = 5
# num = int(input("Enter a no. : "))
# if x == num:
#     print("you won!")
# else:
#     if num < 5:
#         print("Too low")
#     if num > 5:
#         print("Too high")

                                    # AND 
# name, age = "abc", 20
# if name == "abc" and age == 20:
#     print("true")
# else:
#     print("false")
         
                                    # OR
# name, age = "abc", 20
# if name == "abc" or age == 30:
#     print("true")
# else:
#     print("false")

                                     # EXERCISE - 2
# age = int(input("Enter your age : "))                                     
# name = input("Enter your name : ")
# if age>=10 and (name[0] == "a" or "A"):
#     print("Yes!")
# else:
#     print("No!")

                                    # IF_ELIF_ELSE
# age = int(input("Enter your age : "))
# if age <=0:
#     print("can't")
# elif 0<age<=3:
#     print("Fee = free")
# elif 3<age<=10:
#     print("Fee = 50")
# elif 10<age<=60:
#     print("Fee = 100")
# else:
#     print("Fee = 200")

                                    # IN KEYWORD
# name = "Anubhav"
# if "a" in name:
#     print("yes")
# else:
#     print('no')

                                   # CHECK EMPTY OR NOT
                                   # IMPORTANT

# while 1:
#     name = input("Enter your name : ")
#     if name:
#         print(f"your name is {name}")
#         break
#     else:
#         print("you didn't write anything.")

                                  # WHILE LOOP
# i = 1
# count = 0
# while i<=10:
#     print("hello world")
#     i = i + 1
#     count += 1
# print(count)

# i =1 
# total = 0
# while i <= 10:
#     total += i
#     i += 1
# print(total)

                                 # EXERCISE - 3
# num = int(input("Enter a natural no."))
# total = 0
# i=1
# while i<=num:
#     total += i
#     i += 1
# print(total) 

                                # EXERCISE - 4
# num = input("Enter numbers seperated by comma : ").split(",")
# total = 0
# i = 0
# while i< len(num):
#     total += int(num[i])
#     i += 1
# print(total)

                                # EXERCISE - 5
# name = input("Enter your name : ")
# i =0
# temp_var = ""
# while i < len(name):
#     if name[i] not in temp_var:
#         temp_var += name[i]
#         print(f"{name[i]}: {name.count(name[i])}")
#     else:
#         pass
#         i += 1
        

                                # FOR LOOP
# for i in range(0 , 11):
#     print(f"hello world : {i}")

# total = 0
# n = int(input("Enter a number : "))
# for i in range(1 , n+1):
#     total +=i
# print(total)

# name = input("Enter your name : ")
# temp = ""
# for i in range(0 , len(name)):
#     if name[i] not in temp:
#         temp += name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
        

                                        # BREAK AND CONTINUE 
# for i in range(1 , 11):
#     if i == 5:                                           # It gives 1 2 3 4
#         break 
#     print(i)


# for i in range(1 , 11):
#     if i == 5:                                           # It gives 1 2 3 4 6 7 8 9 10
#         continue
#     print(i)

                                        ###  GAME  ###

# import random
# num = int(input("Guess a number between 1 to 100 : "))
# winning_number = random.randint(1 , 100)
# guess = 1
# # game_over = False
# while True:
#     if num < winning_number:
#         print("too low")
#     elif num > winning_number:
#         print("too high")
#     else:
#         print(f"You won! and you guess this number in {guess} guesses")
#         # game_over =True
#         break
#     guess += 1
#     num = int(input("guess again : "))

                                           # STEP IN RANGE
# for i in range(1 ,30 ,2):
#     print(i)

# EVEN NUMBER
# for i in range(0,21,2):
#     print(i)
      
                                           # FOR LOOP STRING
# name = "anubhav"
# for i in range(len(name)):
#     print(name[i])

                        # OR

# name = "anubhav"
# for i in name:                         # OR        for i in "anubhav"
#     print(i)                                          print(i)

# total = 0
# i = 0
# num = input("Enter a number : ")
# while i<(len(num)):
#     total += int(num[i])
#     i += 1
# print(total)
                             
                            # OR
# total = 0
# num = input("Enter a number : ")             # OR             # total = 0
# for i in num:                                                 # num = input("Enter a number : ")
#     total += int(i)                                           # for i in range(len(num)):
# print(total)                                                       # total += int(num[i])
                                                               # print(total)
















