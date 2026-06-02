# product_name="iphone 13 pro"
# price=155000
# color="Black"

# print("Product Name=",product_name)
# print("Product Price=",price)
# print("product Color=",color)


# Q.2)
# student_name="Rahul"
# Age=21
# course="BCA"

# print("Student NAme=",student_name)
# print("Age=",Age)
# print("Course=",course)


# Q.3)
# laptop_name="Dell XPS 13"
# RAM="16GB"
# price=120000

# print("Laptop Name=",laptop_name)
# print("RAM=",RAM)
# print("Price=",price)


# Qn.4)
# movie_name="Inception"
# rating=9
# year=2010

# print("Movie Name=",movie_name)
# print("Rating=",rating)
# print("Year=",year)

# print("Movie Name=", movie_name, "\nRatng=", rating , "\nYear=", year)


# name=str(input("enter your name : "))
# marks=int(input("enter your marks : "))
# age=int(input("enter your Age : "))
# address=str(input("enter your addresss : "))

# print(name)
# print(marks)
# print(age)
# print(address)

# print("my name is:",name)
# print("my marks is:",marks)
# print("my age is:",age)
# print("my address is:",address)

# print("my name is:",name,"\n my marks is:",marks, "\n my age is:",age, " \n my address is:",address)


"""======================= list practice Qns=========================="""

# )Q.1) Insert 100 at index 0 and 200 at index 2 in the list:

# num_list = [10, 20, 30, 40]
# num_list.insert(0,100)
# num_list.insert(2,200)

# print(num_list)            # [100, 10, 200, 20, 30, 40]  
# print(type(num_list))       #<class 'list'>


"""Q2 Insert 5 at index 1 and 50 at index 3 in the list:"""

# num_list1 = [1, 2, 3, 4]
# num_list1.insert(1,5)
# num_list1.insert(3,50)

# print(num_list1)        #[1, 5, 2, 50, 3, 4]

# print(type(num_list1))   #<class 'list'>



      



# Q.1) WAP to find the area of a parallelogram by taking input from user
# Keynotes:
# Input: base, height
# Formula: area = base * height
# Same as rectangle concept but different shape name
# base=int(input("base of parallelogram:"))
# height=int(input("height o parallelogram:"))
# area=base*height
# print("the area of a parallelogram:",area)
 

# Q.2)⁠ ⁠WAP to find the perimeter of a square by taking input from user
# Keynotes:
# Input: side
# Formula: perimeter = 4 * side
# Single input, multiplication only
# side=int(input("enter the side of square:"))
# perimeter=4*side
# print("perimeter of square=",perimeter)


# Q.3)⁠⁠WAP to find the simple interest by taking input from user
# Keynotes:
# Input: principal, rate, time
# Formula: SI = (P * R * T) / 100
# Watch division carefully
# principle=int(input("enter the Given principle="))
# rate=int(input("enter the given rate="))
# time=int(input("enter the given rate="))
# SI=(principle*time*rate)/100
# print("the Simple interest =",SI)


# Q.4)⁠ ⁠WAP to find the average of 3 numbers by taking input from user
# Keynotes:
# Input: num1, num2, num3
# Formula: avg = (n1 + n2 + n3) / 3
# Addition + division

# n1=int(input("enter the value of n1="))
# n2=int(input("enter the value of n2="))
# n3=int(input("enter the value of n3="))

# average =(n1+n2+n3)/3
# print("the average value is ",average)



#Q.5)⁠ ⁠WAP to convert kilometers to meters by taking input from user
# Keynotes:
# Input: kilometers
# Formula: meters = km * 1000
# Simple unit conversion, multiplication only

# kilometers=float(input("enter the distance in kilometer="))

# meters=kilometers*1000

# print("distance in meter=",meters)


"""
==============Practice Questions for Case Conversion Methods in Strings=================
"""

""" 
Q.1) Write a Python program to convert the string "hello world" into uppercase.
"""
# text = "hello world"

# print(text)                     #output: hello world
#                                         #HELLO WORLD
# print(text.upper())

"""
Q.2)Convert the string "PYTHON PROGRAMMING" into lowercase.
"""

# text= "PYTHON PROGRAMMING"

# print(text)                 #output: PYTHON PROGRAMMING
                                      #python programming
# print(text.lower())

"""
Q.3)will be the output?
    s = "hello python"      #output: Hello Python 
    print(s.title())
"""

"""
 Q5.Write a program to capitalize only the first letter of the string "python is fun".
"""
# text = "python is fun"

# print(text)                     #output: python is fun
#                                         # Python is fun       
# print(text.capitalize())


"""
# Q.6) What will be the output?
        s = "hELLO wORLD"            #output: Hello world 
        print(s.capitalize())
"""


"""
Q.7) Write a program to take user input as (name,collegeName,address,favouritePlayer,FavouriteGame) and convert it into:
    •	uppercase 
    •	lowercase 
# """
# name = input("enter the user name: ")                           # input: sushil Singh
# college_name = input("enter th user college_name: ")                    #NCIT
# address = input("enter the user address: ")                             #Koteshwor
# favourite_pLayer = input("enter user favourite_player: ")               #Ronaldo
# favourite_game = input("enter user favourite_game: ")                   #Football

# print(name)
# print(name.upper())
# print(name.lower())

"""
output: sushil singh
upper_caase: SUSHIL SINGH
lower_case: sushil singh
"""

# print(college_name)
# print(college_name.upper())
# print(college_name.lower())

"""
output: NCIT
upper_case: NCIT
lower_caase: ncit
"""

# print(address)
# print(address.upper())
# print(address.lower())

"""
output: Koteshwor
uppeer_case: KOTESHWOR
lower_case: koteshwor
"""

# print(favourite_pLayer)
# print(favourite_pLayer.upper())
# print(favourite_pLayer.lower())

"""
output: Ronaldo
upper_case: RONALDO
lower_lower: ronaldo
"""
# print(favourite_game)                     
# print(favourite_game.upper())
# print(favourite_game.lower())

"""
output: Football
upper_case: FOOTBALL
lower_case: football
"""


""" Q.8) What will be the output? """
# s = "123abc"                      #output: 123ABC
# print(s.upper())


"""Q9.Correct the following string using proper case (title case): """
s ="welcome to nepal"

# print(s)                            #output: welcome to nepal                                       
# print(s.title())                    #titlecase: Welcome To Nepal


""". Q.10) Predict the output:  """

# s = "python programming"
# # print(s.capitalize())         #output: Python programming    
# # print(s.title())              #output: Python Programming


# take a the five  name as input and them check its data types and also take age in integer and then  print it in console .
# after that covert name in uppercase,lowercase,capitalize,title.result must print be using f string. 


# name1 = input("enter the 1st actor name: ")
# age1 = int(input("enter the 1st actor age: "))

# print(f"the 1st actor name is: {name1}")
# print(f"his age is {age1}")
# print(type(name1))
# print(type(age1))
# print(name1.upper())
# print(name1.lower())
# print(name1.title())
# print(name1.capitalize())


# name2 = input("enter the 2nd actor name: ")
# age2 = int(input("enter the 2cd actor age: "))

# print(f"the 2nd actor name is: {name2}")
# print(f"his age is {age2}")
# print(type(name2))
# print(type(age2))
# print(name2.upper())
# print(name2.lower())
# print(name2.title())
# print(name2.capitalize())



# name3 = input("enter the 3rd actor name: ")
# age3 = int(input("enter the 3rd actor age: "))
# print(f"the 3rd actor name is: {name3}")
# print(f"his age is {age3}")
# print(type(name3))
# print(type(age3))
# print(name3.upper())
# print(name3.lower())
# print(name3.title())
# print(name3.capitalize())


# name4 = input("enter the 4th actor name: ")
# age4 = int(input("enter the 4th actor age: "))
# print(f"the 4th actor name is: {name4}")
# print(f"his age is {age4}")
# print(type(name4))
# print(type(age4))
# print(name4.upper())
# print(name4.lower())
# print(name4.title())
# print(name4.capitalize())



# name5 = input("enter the 5th actor name: ")
# age5 = int(input("enter the 5th actor age: "))
# print(f"the 5th actor name is: {name4}")
# print(f"his age is {age5}")
# print(type(name5))
# print(type(age5))
# print(name5.upper())
# print(name5.lower())
# print(name5.title())
# print(name5.capitalize())


# print(f" the first actor name is {name1}| his age is {age1} | name1 Type: {type(name1)} | age1 type:{type(age1)} | upper: {name1.upper()} | lower: {name1.lower()} | capitalize: {name1.capitalize()} | Title: {name1.title()}")

# print(f"the 2nd actor namee is{name2}| and his age is{age2}| name2 type: {type(name2)}| age2 type: {type(age2)} | upper: {name2.upper()} |lower: {name2.lower()}| capitalize: {name2.capitalize()}| title: {name2.title}")



""""
==========(Qn) related to (spilt and join) function  ===========

"""

"""
Q1. Full Name Split Program

Write a Python program that:

Takes full name from user
Uses split()
Prints first name and last name separately

firstName: sushil
LastName : singh
"""

# name = input("Enter your full name: ")
# result = name.split(" ")

# print(result)
# print("first name: ", result[0])
# print("last name : ", result[1])

# #print by using f
# print(f"my name is{result}")
# print(f"first name: {result[0]}")
# print(f"last name: {result[1]}")


"""Q2. Email Analyzer Program

Write a Python program that:

Takes email from user
Uses split("@")
Prints username and domain name separately
"""

# email = input("enter your email: ")
# result = email.split("@")

# print(result)
# print("user_name: ", result[0])
# print("domain_name: ", result[1])

# # #print by using f
# print(f"my email_id: {result}")
# print(f"user_name: {result[0]}")
# print(f"domain_name: {result[1]}")




"""
Q3. Website Name Extractor

Write a Python program that:

Takes website URL from user
Uses split(".")
Prints website name only
"""
# URL = input("enter the website URL: ")      #input: www.google.com
# result = URL.split(".")

# print(result)       #output: ['www', 'google', 'com']
# print("website_name: ", result[1])      #output: google

# #print by using f
# print(f"website_name: {result}")
# print(f"website_name: {result[1]}")


"""
Q4. Word Join Program

Write a Python program that:

Takes 3 words from user
Stores them in list
Uses join()
Joins all words with space
"""

# list1 = input("enter the 1st word: ")
# list2 = input("enter the 2nd word: ")
# list3 = input("enter the 3rd word: ")

# list = [list1, list2, list3]

# result =" ".join(list)
# print("join all words with space: ",result)


"""
Q5. CSV Data Split Program

Write a Python program that:

Takes comma-separated values from user
Uses split(",")
Prints each value separately
"""
# Data = input("enter comma separated value: ")           #input: apple,orange,mango,papaya

# result = Data.split(",")

# print("seperate value are", result[0], result[1], result[2], result[3])         #output:  apple orange mango papaya

# print(f"Seprate value are: {result[0]} {result[1]} {result[2]} {result[3]}")         #output:  apple orange mango papaya

# print(f"seperate value are: \n{result[0]}\n{result[1]}\n{result[2]}\n{result[3]}")   #output: apple 
# #                                                                                             orange 
# #                                                                                             mango 
# #                                                                                             papaya     

# print(f"seperate value are: \n{result[0]} \n{result[1]} \n{result[2]} \n{result[3]}")     #output: apple 
# #                                                                                                  orange 
# #                                                                                                  mango 
# #                                                                                                  papaya  



"""
    =============removing space (strip,lstrip,rstrip) related qn============
Q1. Clean Name Input Program (strip)
Write a Python program that:
Takes a name from user with extra spaces
Removes spaces from both sides using strip()
"""
# name = input("enter your name:")            #input:          Sushil   Singh
# result = name.strip()
# print("after removing space: ",result)      #output: Sushil   Singh 



"""
Q2. Remove Left Side Spaces (lstrip)
Write a program that:
Takes input with left spaces
Removes only left side spaces
# """
# name = "          Sushil          "

# result = name.lstrip()

# print("after removing space from left side only:",result)



"""
Q3. Remove Right Side Spaces (rstrip)
Write a program that:
Takes input with right spaces
Removes only right side spaces
"""
# name = "          Sushil          "

# result = name.rstrip()

# print("after removing space from right side: ",result)



"""
Q4. Username Cleaner (strip + length)
Write a program that:
Takes username with extra spaces
Removes spaces using strip()
Prints cleaned username and its length
"""
# user_name = input("enter your user name: ")         #input:        Sushil

# result = user_name.strip()

# print("cleaned user_name :", result)
# print("Length of user_name:",len(user_name),"\n","length of cleaned name:", len(result), sep="")

#output:cleaned user_name : Sushil
#       Length of user_name:12
#       length of cleaned name:6


"""
Q5. Password Space Checker (strip logic)
Write a program that:
Takes password input
Removes spaces using strip()
Checks if password was changed after removing spaces
"""
password = input("enter the password: ")

result = 








"""
=========suffix related qn =============
"""

""""
Q1. Remove prefix from website

Given string: "www.facebook.com"
Apply removeprefix("www.")

Result: facebook.com
"""
# URL= "www.facebook.com"       

# remove_prefix = URL.removeprefix("www.")

# print("after removing prefix:",remove_prefix)       #result: facebook.com



"""
Q2. Remove suffix from domain

Given string: "google.com"
Apply removesuffix(".com")

Result: google
"""
# Website = "google.com"

# remove_suffix = Website.removesuffix(".com")

# print("after remove Suffix:", remove_suffix)        #output: google



"""
Q3. Remove title prefix

Given string: "Mr. Saroj"
Apply removeprefix("Mr. ")

Result: Saroj
"""
# name = "Mr.Saroj"

# remove_prefix = name.removeprefix("Mr.")

# print("after removing title prefix:",remove_prefix)     #outpput: Saroj




"""
Q4. Remove file extension

Given string: "notes.txt"
Apply removesuffix(".txt")

Result: notes
"""
# text = "notes.txt"

# remove_suffix = text.removesuffix(".txt")

# print("after removing suffix:", remove_suffix)      #outpt: notes




"""
Q5. Remove both prefix and suffix

Given string: "www.python.org"
Apply removeprefix("www.") and removesuffix(".org")

Result: python
"""
# URL = "www.python.org"

# result = URL.removeprefix("www.").removesuffix(".org")

# print("after removing prefix and suffix:",result)       #output: python


a = 5

b = 3 




