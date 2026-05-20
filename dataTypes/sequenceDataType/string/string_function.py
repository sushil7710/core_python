# name = "sushil singh"
# print(name.upper())

# print(type(name))

# upper(),lower(),capitzile(),title()
# print(name.lower())

# name.capitalize().     capitalize ma suruko letter matra capital hunxa 
# print(name.capitalize())

# print(name.title())

"""========string function========"""

# string function is a tool or method that help to mainuplate , modify,or analyze text 

""" 1.) ======case conversion :(upper, lower,title,capitalize)======"""

"""
a.)upper case conversion:

"""
# syntax:
# variablename.upper()

# name="sushil"
# text=name.upper()

# print(name.upper())      #output: SUSHIL

# print(text)           #output: SUSHIL  

# print(name)    # output:sushil 


"""
b.)lowercase:
             it converts word all letterrs into lowercase (small alphabet form)
"""
# syntax:
# variablename.lower()

# #example:
# collegename = "NASA International ColleGe"
# text = collegename.lower()
# print(collegename.lower())
# print(text)

"""
c)title():
        it convert every words inside the string first letter cappital and others  in smalll 
"""
#syntax:
#variablename.title()

# collegename = "NaSa International COLLEGE"
# text = collegename.title()

# print(collegename.title())     #output: collegename.title()

# print(text)      #output: Nasa International College


"""
d.)>capitalize():  
                it convert first letter capital and other litter remain in lowercase.
"""
# collegename = "NaSa International COLLEGE"
# text = collegename.capitalize()

# print(collegename.capitalize())      #otput: Nasa international college

# print(text)         #output: Nasa international college


"""
Qn.) write a program to capitalize only the first litter of the string "python is fun" 
"""
# text = "python is fun"
# print(text.capitalize()).  #output: Python is fun 


""""
Qn.2) take a username from the user as input then cheak their case . if they hit uppercase then convert it into lowercase.
      if hit lowercase then convert into uppercase.
 """
"""====type 1)===="""

# user_name = input("enter your user_name: ")

# if (user_name.islower()):
#     print("user_name:",user_name,"-->",user_name.islower())

# elif (user_name.isupper()):
#     print("user_name: ",user_name,"-->",user_name.isupper())

# else:
#      print("false")


"""====type (2)===="""

# user_name = input("enter your user_name: ")

# if (user_name.islower()):
#     print("user_name:",user_name,"-->",user_name.islower(),"  #(lowercase)")
#     print("user_name convert into lowercase:",user_name.swapcase())

# elif (user_name.isupper()):
#     print("user_name:",user_name,"-->",user_name.isupper())
#     print("user_name convert into uppercase:",user_name.swapcase())

# else:
#     print("usser_name:",user_name,"-->",False,"  # other case()")
#     print(user_name.swapcase(), )


# user_name = input("enter your user name: ")
# print("user_name: ",user_name.islower())
# print("user_name after convert: ",user_name.swapcase())

# user_name = input("enter your user_name: ")














"""
 2.)======cheaking method (Return true/False): isalpha(), isdigit(), isalnum(), ispace(), islower(), isupper()======
 """
#  In cheaking methid  we cheak  the real string types like it may be is isalpha(), isdigit(), isalnum(){numner+alphabet--->combo0}  ,ispace(), islower(), isupper()
#  if match the output is True other wise False.


"""
a) isalpha():
            isalpha cheak the string in alphabetic from if alphabetic then active true otherwise false.
"""


# text = "hello world"        #ouput: False   [ reason-->is alpha doesnt take space ]
# print(text.isalpha())

# text = "helloworld"        #ouput: True
# print(text.isalpha())

# id_number="1234"
# print(id_number.isalpha())  #output: False


# symbol="@#$%"
# print(symbol.isalpha())    #output: False

"""
b.) isdigit():
            it check the numberical data .if data is numberical then active(true) otherwise false.
"""
# num = "123.56"
# print(num.isdigit())        #output: False [because there is float value]


# num = "1234"
# print(num.isdigit())         #output: True


# num="-12345"
# print(num.isdigit())         #output: False. [because there is -value]

"""
c.) isalnnum: 
            it cheak both number, alphabetic or combination of both  the it give True otherwise False.       
"""
# example: 1
# text ="123abd"
# print(text.isalnum())      #output: True

# #  example: 2
# num = "1234"
# print(num.isalnum())        #output: True

# # example: 3
# word = "hello"
# print(word.isalnum())       #output: True

# # example: 4
# word = "hello world"
# print(word.isalnum())        #output: False

# # example: 5
# name = "SuhilSingh"
# print(name.isalnum())        #output: True 

# # example: 6
# name = "Sushil Singh"
# print(name.isalnum())        #output: False


"""
d) isspace(): 
            isspace check only space inside string. 
"""
# # example: 1
# a =""
# print(a.isspace())         #output: False


# # example: 2
# a = " "
# print(a.isspace())         #output: True

# # example:3
# name = "Sushil Singh"
# print(name.isspace())        #output: False


# # example:4
# name = "SushilSingh"
# print(name.isspace())        #output: False


# # example:5
# num = "1234"
# print(num.isspace())       #output: False


# # example:4
# test = "Sushi9097"
# print(test.isspace())      #output: False

"""
f) isupper():
            it check all character inside the string is in uppercase. if yes the it give True otherwise False.
"""
# # example:1
# name = "Sushil"
# print(name.isupper())     #output: False


# # example:2
# name = "SUSHIL"
# print(name.isupper())       #output: True


# # example:3
# name = "sushil"
# print(name.isupper())     #output: False


"""
3)=========Searchin method():========
#1) searching meathod searching character location using index value.
#2) indexing value : index value is always start with zero(0).

"""

# a)Index()
# b)Find()
# c)Count()

"""
a) find():
        it gives the character location in indexing form.
"""
# # example: 1
# fruit = "apple"
# path = fruit.find("p")     #output: 1
# print(path)


# # example: 2
# fruit = "aooopple"
# path = fruit.find("p")     #output: 4
# print(path)


# example: 3
# fruit = "apple"
# print(fruit.find("pt"))      #output: 3

# # example: 4
# fruit = "apple, banana"
# print(fruit.find("banana"))       #output: 7

# # example: 5
# fruit = "apple"
# print(fruit.find("pt"))           #output: -1


# # example: 4
# fruit = "apple, banana, orange"
# print(fruit.find("ra"))



"""
b) Index():
          
"""
# # example: 1
# address = "kathmandu"
# print(address.index("h"))

# #output: 2
# city = "pokhara"
# print(city.index("kt"))         #output: Error

# #output: 3
# town = "Lahan"
# print(town.index("n"))


"""
c) count():
          it count the total number of searched character inside the string.
"""

#output: 1
# address = "savvvetrroojvv"
# print(address.count("v"))
# print(address.count("vv"))
# print(address.count("jk"))



""""
(Qn)
1.) take the words "Encyclopedia" and check "cl", "C", "ed", "de" using the function and write output
# """
# Qn.1)
word = "Encyclopedia"
print(word.find("cl"))
print(word.find("C"))
print(word.find("ed"))
print(word.find("de"))


"""
Q.2) Take the word "Encyclopedia" and check "cl", "C", "ed", "de" using the function and write output.
"""
# word = "Encyclopedia"
# print(word.index("cl"))
# print(word.index("C"))
# print(word.index("ed"))
# print(word.index("de"))


"""
Q.3) mssg = "Hello This is Deepak From Mahendranager" 
# count: a, e, m, t ,o

"""

# mssg = "Hello This is Deepak From Mahendranager"
# print(mssg.count("a"))
# print(mssg.count("e"))
# print(mssg.count("m"))
# print(mssg.count("t"))
# print(mssg.count("o"))





















#Q5. Data Type Analyzer
"""
Take input from user and check:
If input is only digits → print "Number"
If input is only alphabets → print "Text"
If input contains both → print "Alphanumeric"
If input is only spaces → print "Blank input"
Use: isalpha(),
"""

# user = input("enter your choice: ")
# print("number :",user.isdigit())        #output: True

# user1 = input("enter your choice:  ")
# print("TEXT: ",user1.isalpha())         #

# user2 = input("enter your chouce: ")
# print("Alphanumeric: ",user2.isalnum())

# user3 = input("enter your choice: ")
# print("space: ", user3.isspace())


# user_name = input("enter your user name: ")
# if (user_name.isupper()):
#     print("username: ",user_name.isupper())
# elif(user_name.islower()):
#     print("username: ",user_name.islower())
# else:
#     print("false")

