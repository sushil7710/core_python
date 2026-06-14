# Data types in Python define the type of value a variable can store. 
# They tell the computer whether the data is a number, text, list, etc.

# Types of Data:
# 1.======Immutable Data Types (Cannot be changed after creation)=========
#int,float,str,tuple and boolean

#example: 1
# name = "saroj"
# print(name.index("s"))
# name[0] = "r"



# 2.=======mutable Data Types(Can be changed after creation)=========
#list,dict,and set



"""
memory interning:
                    it removes the duplication of value and store in single memory location
"""
# #example: 1
# a = 5
# b = 5
# print(id(a)) #140706183087144
# print(id(b))    #140706183087144
# print(a)
# print(b)

#example: 2
# x = 10
# print(id(x))   # memory address :140706221556936

#example:3
# x = 5
# print(id(x)) 



"""
=======string immutability check:==========
"""

# lst = ["saroj", "ram", "hari"]
# print(lst[0])
# lst[0] = "krishna"
# print(lst)


#example:1
# name = ["Sushil"]
# print(name [0])
# name[0] = "k"

# print(name)


#example: 2
# list = ["apple", "mango", "123"]
# list[2] = "banana"



"""
Raw Strings (r''):
                it skips the escape character and prints as it is as normal string
"""
#syntax:
# r"strings with escape character(\)"


#example: 1

# name = "hel\tlo"
# print(name)
# name = r"hel\vlo"
# print(name)

#example: 2

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# result = str1 + " " + str2
# print("Combined String:", result)






# name = "Mr:Skm"
# age = 18
# weight = 55.5
""""
=============formatting string concept========
"""

"""
1)--->%string:
"""
# name = "Sushil singh"
# age = 23
# weight = 60.5
# print("My name is %s, my age is %i and my weight is %.2f kg." %(name,age,weight))

#output: My name is Sushil singh, my age is 23 and my weight is 60.50 kg.

"""
2>)--->.format:
"""
# name = "Sushil singh"
# age = 23
# weight = 60.5
# print("My name is {}, my age is {} and my weight is {} kg.".format(name,age,weight))

#output: My name is Sushil singh, my age is 23 and my weight is 60.5 kg.

""" 
3.)--->f-string: 
"""
# name = "Sushil singh"
# age = 23
# weight = 60.5
# print(f"My name is {name}, my age is {age} and my weight is {weight} kg.")

#output: My name is Sushil singh, my age is 23 and my weight is 60.5 kg.












# a = 5

# b = 5

# print(id(a))

# print(id(b))


# name = "hello\tsushil"
# print(name)

# name = r"hello\tsushil"
# print(name)



# first_name = input("enter your first_name: ")

# last_name = input("enter your last_name: ")

# result =first_name+" "+ last_name

# print(result)
# name = "sushil"