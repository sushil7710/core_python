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
# variablename.title()

# collegename = "NaSa International COLLEGE"
# text = collegename.title()

# print(collegename.title())     #output: Nasa International Colle

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

# output: 1
# address = "savvvetrroojvv"
# print(address.count("v"))
# print(address.count("vv"))
# print(address.count("jk"))



""""
(Qn)
1.) take the words "Encyclopedia" and check "cl", "C", "ed", "de" using the function and write output
# """
# # Qn.1)
# word = "Encyclopedia"
# print(word.find("cl"))
# print(word.find("C"))
# print(word.find("ed"))
# print(word.find("de"))


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


"""Qn related to (Find , index and count) function  ======
 Q1. Search Character Position

Write a Python program that:

Takes a string from the user.
Takes one character from the user.
Uses only string functions:
find()
count()
Print:
First position
Total occurrences
"""
# user = "Sushil Singh"







"""Q4. Email Symbol Checker

Write a Python program that:

Takes an email from the user.
Uses only:
find()
count()
Print:
Position of @
Total number of dots (.)

"""




"""
======== Splitting & joining ==========
"""

#1.) split(): it breaks the strings and convert into list.

# # example: 1
# name = "Singh"
# print(name.split("n"))          #output:['Si', 'gh']


# # example: 2
# name = "Singh"
# print(name.split("S"))     #output:['', 'ingh'] 

# print(name.split("s"))      #output: ['Singh']

# print(name.split("i"))          #output:['S', 'ngh']

# print(name.split("n"))          #output: ['Si', 'gh']

# print(name.split("g"))          #output: ['Sin', 'h']

# print(name.split("h"))          #output: ['Sing', '']


# # example:3
# name = "Siddhartha"
# print(name.split("h"))          #output: ['Sidd', 'art', 'a']


## example:4
# text = "sequenceData"
# print(text.split("e"))          #output: ['s', 'qu', 'nc', 'Data']

# #example: 5
# fruits = "orange apple banana papaya mango"
# print(fruits.split(" "))         #output: ['orange', 'apple', 'banana', 'papaya', 'mango']



# #example: 6
# fruits = "orange,apple,banana,papaya,mango,coconut"  
# print(fruits.split(","))      #output:['orange', 'apple', 'banana', 'papaya', 'mango', 'coconut']



# # example:7 
# address = "kkkkathmmmmanduuuu"

# print(address.split("k"))              #output: ['', '', '', '', 'athmmmmanduuuu']

# print(address.split("m"))              #output: ['kkkkath', '', '', '', 'anduuuu']

# print(address.split("u"))              #output: ['kkkkathmmmmand', '', '', '', '']
# print(address.split("u"))              



#example:8

# name = input(" enter your full name: ")       #input: enter your name: Sushil singh
# result = name.split(" ")

# print(result)       #output: ['sushil', 'singh']

# print("first name: ",result[0])               #output: first name:  sushil
# print("last name: ", result[1])               #output: last name:  singh



# # Example:9         

# name = input("enter your full name: ")       #input: enter your name: Sushil singh

# result = name.split(" ")

# print("first name: ",result[0])               #output: first name: Sushil
# print("last name: ",result[1])                #output:last name: Singh


"""
2.) join():
          it  joining
"""

# list1 = ["saroj", " bardibas"]
# list2 = ["Sushil", "kathmandu"] 

# list = list1 + list2

# result =" ".join(list)

# print(result)           #output: Saroj  bardibas Sushil kathmandu
# print(type(result))      #output: <class 'str'>


"""
==========Qn related to (spilt and join) function  ===========
Q1. Full Name Split Program

Write a Python program that:

Takes full name from user
Uses split()
Prints first name and last name separately

firstName: sushil
LastName : singh
"""

# name  = input("enter your full name: ")       #input: enter your name: Sushil singh
# result = name.split(" ")

# print("first name: ", result[0])              #output: first name:  Sushil 
# print("last name: ",result[1])                #output: last name:  Singh      



# # print with f :
# name = input("enter your full name: ")        #input: enter your name: Sushil singh 
# result = name.split(" ")

# print(f"first name: {result[0]}")             #output: first name:  Sushil  
# print(f"last name: {result[1]}")              #output: last name:  Singh

"""
Q2. Email Analyzer Program

Write a Python program that:

Takes email from user
Uses split("@")
Prints username and domain name separately
"""
# email = input("enter your email_id: ")         #input: enter your email_id: sushilsingh2058@gmail.com  
# result = email.split("@")

# print("user_name: ",result[0])                 #output: domail name:  gmail.com
# print("domail name: ",result[1])               #output: domail name:  gmail.com


# #print with f :
# email = input("enter youur email_id: ")        #input: enter your email_id: sushilsingh2058@gmail.com 
# result = email.split("@")

# print(f"user name: {result[0]}")                #user_name:   domail name:  gmail.com
# print(f"domain name: {result[1]}")              #domail name:  gmail.com

"""
Q3. Website Name Extractor

Write a Python program that:

Takes website URL from user
Uses split(".")
Prints website name only
"""
# url = input("enter website url: ")       #input: http://www.youtube.org 
# result = url.split(".")

# print(f"website name: {result[0]}")      #output:  http://www

"""
Q4. Word Join Program

Write a Python program that:

Takes 3 words from user
Stores them in list
Uses join()
Joins all words with space
"""
# word1 = input("enter the words1: ")
# word2 = input("enter the words2: ")
# word3 = input("enter the word3: ")

# list = word1 + word2 + word3

# print(list)
# result =" " .join(list)

# print(result)





# word1 = input("enter the words1: ")

# list = word1 

# print(list)
# result ="" .join(list)

# print(result)








"""
Q5. CSV Data Split Program

Write a Python program that:

Takes comma-separated values from user
Uses split(",")
Prints each value separately
"""
# Data = input("comma srperate values: ")
# result = Data.split(",")

# print(f"saperate value are: {result[0]}\n{result[1]}\n{result[2]}\n{result[3]}", sep="")






"""
5.========== removing space===========
it remove the unwanted space in string.
"""


"""
a.) strip():
           it remove the unwanted  space from both left to right side of the string
           
"""
# name = "    sushil    "

# print(name.lstrip())

"""
b.) rstrip():
             it removes the left sides unwanted space from string.   
"""
# name = "    sushil    "
# print(name.rstrip())


"""
c.) lstrip():
            it removes the right sides unwanted space from string.
"""

# name = "    sushil    "
# print(name.lstrip())



"""
6.==========Alignment function============
"""


"""
a.)=======center (width)===========
it provide the equal spaces inside both sides of the string . example: if center (20) then it it provides 10 (wodth)
from left and 10 (width) from right

"""
# fruit = "apple"
# text = fruit.center(20)
# print(text, "is my favorite fruits")



"""
a.)=======ljust (width)===========
  * it provide the 20 spaces from right sides of the string .

 """
# fruit = "apple"
# text = fruit.ljust(20)

# print(len(text))
# print(len(fruit))
# print(text, "is my favorite fruits")



"""
a.)=======rjust (width)===========
---> it provide the 20 spaces from left sides of the string .
  
"""
# fruit = "apple"
# text = fruit.rjust(20)

# print(len(text))
# print(len(fruit))
# print(text, "is my favorite fruits")



 
 









"""
7.)================ starts & Ends===================
*it cheaks the string starting character . if match then gives true otherwise false.

"""

""""
a.)startswith():

"""
# name = "Sushil"

# print(name.startswith("S"))
# print(name.startswith("i"))
# print(name.startswith("l"))



"""
b.)endswith():

"""
# name = "Sushil"

# print(name.endswith("i"))
# print(name.endswith("l"))
# print(name.endswith("S"))



"""
===================removing  space(strip,lstrip,rstrip)=========================
Q1.)clean Name Input program (strip)
write a python program that:  takes a name from user with extra spaces removes spaces from both sides using strip()
"""
# name = input("enter your name: ")





"""
8.length():
          it finds the actual length of string. 

"""
# fruit = "banana"
# print(len(fruit))         #output: 6



"""
9.) =============Remove: prefix/suffix==========
"""

# #example: 1
# email = "admin.@gmail.com.sushil"

# print("after removing prefix (admin.): ",email.removeprefix("admin."))      #output: @gmail.com.sushil
# print("after removing suffix (.com): ",email.removesuffix(".com"))          #output: admin.@gmail.com.sushil (the can't remove from center)



# #example:2
# email = "admin.@gmail.com.sushil"

# print("after removing prefix (admin.): ",email.removeprefix("admin."))         #output: @gmail.com.sushil
# print("after removing suffix (.com): ",email.removesuffix(".com.sushil"))      #output: admin.@gmail



# #example:2
# email = "admin.@gmail.com.sushil"       

# print("after removing prefix (admin.): ",email.removeprefix("admin."))   #output: @gmail.com.sushil
# print("after removing suffix (sushil): ",email.removesuffix("sushil"))   #output: admin.@gmail.com.

""""
10.) replace() function: 
                        it replace the each and every character of the string  or as a whole string.
"""

# #example:
# name = "Sushil"
# result=name.replace("s","T")
# print(result)               #output: SuThil


# name = "Sushil"
# result = name.replace("Sushil", "Saroj")

# print(result)         #output: Saroj























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

