                                 # object oriented programming (OOP)

# class Person:
#     def __init__(self, first_name, last_name, age):               # constructor
#         # instance variables
#         print('int method called')
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age 

# p1 = Person('anubhav','choudhary',20)
# p2 = Person('sunny','choudhary',20)

# print(p1.first_name)
# print(p2.last_name)

                                      # EXERCISE - 1

# class Laptop:
#     def __init__(self, name, model, price):                      # constructor
#         self.lap_name = name
#         self.lap_model = model
#         self.lap_price = price
#         self.laptop1 = name + " " + model + " " + str(price)

# l1 = Laptop('lenovo','ideapad',60000)
# l2 = Laptop('asus','zen_book',50000)


# print(l1.lap_model,l2.lap_name)
# print(l1.lap_price)
# print(l1.laptop1)


                                        # instance method


# class Person:
#     def __init__(self, first_name, last_name, age):               # constructor
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age 

#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
    
#     def is_above_18(self):
#         return self.age>18

# p1 = Person('anubhav','choudhary',20)
# p2 = Person('sunny','choudhary',20)

# print(p1.full_name())
# print(p2.is_above_18())

                                   # EXERCISE - 2
# class Laptop:
#     def __init__(self, name, model, price):                      # constructor
#         self.lap_name = name
#         self.lap_model = model
#         self.lap_price = price

#     def apply_discount(self,num):
#         off_price = (num/100)*self.lap_price
#         return self.lap_price - off_price


# l1 = Laptop('lenovo','ideapad',60000)
# l2 = Laptop('asus','zen_book',50000)

# print(l1.apply_discount(40))                                # by default it gives self argument
                                                                 # first then num


                                 # class variable

# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius

#     def circumference(self):
#         return 2*Circle.pi*self.radius

# c1 = Circle(4)
# c2 = Circle(5)

# print(c1.circumference())
# print(c1.pi)                                         




# class Laptop:
#     discount_percent = 10
#     def __init__(self, name, model, price):                      # constructor
#         self.lap_name = name
#         self.lap_model = model
#         self.lap_price = price

#     def apply_discount(self):
#         off_price = (self.discount_percent/100)*self.lap_price
#         return self.lap_price - off_price

# Laptop.discount_percent = 50                                # here we increase discount.  
# l1 = Laptop('lenovo','ideapad',60000)
# l2 = Laptop('hp','au114tx',63000)                           
# l2.discount_percent = 80                                    # here we increase discount only for l2
# l3 = Laptop('asus','zen_book',50000)

# print(l1.apply_discount())
# print(l2.apply_discount())
# print(l3.apply_discount())
# print(l1.__dict__)                                          # it print all instance variable with 
# print(l2.__dict__)                                               # discount_percent = 80 (only in l2)



# class Person:
#     age = 20                                                     # every person are of same age.
#     count_instance = 0
#     def __init__(self, first_name, last_name,):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name

# p1 = Person('anubhav', 'choudhary')
# p2 = Person('sunny','choudhary')

# print(p1.first_name)
# print(p1.age)
# print(Person.count_instance)


 
                                    # class method (not too much usefull)

# class Person:
#     age = 20                                                     # every person are of same age.
#     count_instance = 0
#     def __init__(self, first_name, last_name,):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name

    # @classmethod                                             # by class method.
    # def count_instances(cls):
    #     return f"You have created {cls.count_instance} instances of {cls.__name__} class"
                                                         
                                                               # by instance method
    # def count_instances(self):                
    #     return f"You have created {Person.count_instance} instances of {Person.__name__} class"
                               
                                                                
# p1 = Person('anubhav', 'choudhary')
# p2 = Person('sunny','choudhary')

# print(p1.first_name)
# print(p1.age)
# print(Person.count_instance)
# print(p2.count_instances())


                                # class constructor

# class Person:
#     def __init__(self, first_name, last_name, age):               # instance constructor
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age 

    # @classmethod                                                  # class instance
    # def from_string(cls,string):
    #     first,last,age = string.split(",")
    #     return cls(first,last,age)

    # @staticmethod                                                 # static function
    # def hello():
    #     return 'hello, static method called'

    # def full_name(self):
    #     return f'{self.first_name} {self.last_name}'
    
    # def is_above_18(self):
    #     return self.age>18

# p1 = Person('anubhav','choudhary',20)
# p2 = Person('sunny','choudhary',20)

# p3 = Person.from_string('harshit,vasisth,24')

# print(p3.full_name())
# print(p3.age)

# print(p1.hello())

# print(p1.full_name())
# print(p2.is_above_18())



                                # inheritance

# class Phone:                                                                # base class
#     def __init__(self,name,model,price):
#         self.name = name
#         self.model = model
#         self.price = max(price,0)

#     def full_name(self):
#         return f'{self.name} {self.model}'

#     def make_a_call(self,num):
#         return f'calling on {num}'

# class Smartphone(Phone):                                                     # derived class
#     def __init__(self,name,model,price,ram,internal_memory,rear_camera):
#         # first way
#         # Phone.__init__(self,name,model,price)                   # uncommon way
#         # second way
#         super().__init__(name,model,price)
#         self.ram = ram
#         self.internal_memory = internal_memory
#         self.rear_camera = rear_camera

# p1 = Phone('nokia','1100',1000)
# print(p1.full_name())

# s1 = Smartphone('honor','8x',11000,'4gb','64gb','22 mp')
# print(s1.full_name() + f'and price is {s1.price}') 


                                  # multilevel inheritance
                                
# class Phone:                                                                # base class
#     def __init__(self,name,model,price):
#         self.name = name
#         self.model = model
#         self.price = max(price,0)

#     def full_name(self):
#         return f'{self.name} {self.model}'

#     def make_a_call(self,num):
#         return f'calling on {num}'

# class Smartphone(Phone):                                                     # derived class
#     def __init__(self,name,model,price,ram,internal_memory,rear_camera):
#         super().__init__(name,model,price)
#         self.ram = ram
#         self.internal_memory = internal_memory
#         self.rear_camera = rear_camera

# class Flagshipphone(Smartphone):
#     def __init__(self,name,model,price,ram,internal_memory,rear_camera,front_camera):
#         super().__init__(name,model,price,ram,internal_memory,rear_camera)
#         self.front_camera = front_camera

# p1 = Phone('nokia','1100',1000)
# print(p1.full_name())

# s1 = Smartphone('honor','8x',11000,'4gb','64gb','22 mp')
# print(s1.full_name() + f'and price is {s1.price}') 

# f1 = Flagshipphone('honor','8x',11000,'4gb','64gb','22 mp','16 mp')
# print(f1.front_camera)
# print(f1.make_a_call(12345))


                                 # method overriding/polymorphism

# In method overriding, let's take the above example.
# In the above example if we make a function having same name (full_name) then when we run our code 
# firstly python check that flagshipphone class have function if it have the python run that function
# if not then it checks in smartphone class and the phone class,if phone class also have full_name 
# function then this function will be overrided by the (full_name) function of flagship class.


                            # isinstance() and issubclass()
# isinstance(object, class name)          it gives True or False that this object belongs to this class

# issubclass(Smartphone, Phone)        it checks that this Smartphone class is derived from Phone class


                            # operator overloading



# class Phone:                                                                # base class
#     def __init__(self,name,model,price):
#         self.name = name
#         self.model = model
#         self.price = max(price,0)

#     def __add__(self, other):                                 # here __add__ is dunder.
#         return self.price + other.price

# p1 = Phone('honor','8x',11000)
# p2 = Phone('honor','8x',13000)
# print(p1 + p2)
