#python: python is a high level programming language 
#uses of python:
#it is used in web development
#it is used in AI(Artificial inteligennce),ML(machine learning)
#It is used in Game Development
#it is the basic parts of the networking and security Field.
#print() // it is a function that show output

#=============Variable===========T
#variable: Variable is container that is used to store data
# ======types of Variable==========

# 1)locial variable: It is declare inside the function and only call inside that function or within class
# 2)Global variable: the variable which is calls outside the function or class
# 3)constant variable: the. variable which have fixed value then use coonstant variable like (const_PI=3.14)

# ==========wway to declare variable=======
# 1.)the variable is case sensitive  so (name is not equal to Name)
# example:
#    name="Ram"
#    Name="Shyam"

# 2) pre define function and keywords are restricted(not use) to define function(const is defined for constant so we don't use as variable)
# example:
   #float, Srtring

# ======= method to declare variable========
# camelCase :in camelCase the first words start with small letter and second word start with capital letter and other letter is small it is a best case to define variable name.
# collegeName = "NCIT"
# studentName = "Sushil Singh"
# print(collegeName)
# print(studentName)

# pascal Case: pascalcase words first letter start is capital and other is small  
# CollegeName = "NCIT"
# StudentName = "Sushil Singh"
# print(CollegeName)
# print(StudentName)

# Snake case: in snake case between words we use underscore(_) to seprate words. to declare variable.
# college_name = "NCIT"
# STUDENT_NAME = "Sushil Singh"
# print(college_name)
# print(STUDENT_NAME)



# example:
# 
#print("hellow world")
#print("Sushil Singh")
#print("Age=23")

# name="Suhil"
# print("my name is:",name).    #my name is: Suhil


# Age=23
# print("my age is:",Age).      #my age is: 23


# Address="Koteshwor"
# print("my Address is:",Address)       #My address is : Koteshwor

# Data: data is a set of instructions.
# example:
     #woke up, life
#============types of Data===============

# A. =====numeric data types=====
"""
1.)int:it is a numberic form of data that doesn't take decimal values (like 0.1, 0.5 ).
"""
# example:

# A=5
# print("the value of A is: ",A)   #the value of A is: 5 


# Age=26
# print("My age is: ",Age)   #My age is: 26


# price=260
# print("the price is: ",price)    #the price is: 260


"""
2.)Float:
        float is the  approximat value  which is written certain niumber after decimal like(2.465)
   """
   #Example:
        #if exat value of pi=3.14159265, then its approximate value is pi=3.14 

# price=25.5
# print("the marked price:",price)      #the marked price: 25.5

        
# intrest=25.56 
# print("the interest rate is:", interest)        #the intrest rate is: 25.56

"""
========sequence Data types=====
"""

#2.)=======list======
# list is a sequencial data types  which is mutable(changeable), and in ordered
# list can be always  written in [] in python
fruits=["apple","banana","orange","papaya"]
number=[45,1,50.56,65,56,78,98,1,2]
number.append(9)
number.insert(2, "ram")
number.insert(0, 49)
print(fruits)
print(fruits[3:1])
fruits[0]=1   #. index zero ma 1 value rakheko apple ko place ma replace garera
print(fruits)
print(fruits[0], fruits[3]) 
print(fruits[3:1])
print(type(fruits))
print(number)
print(type(number))




