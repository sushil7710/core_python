
"""
String:
    String is a in sequence data type.(inbuilt data type)
    String is created by single quote(' ') or double quote(" ") or triple single qoute(''' ''') or triple double quote(""" """).

    String is immutable, means we cannot change the character(content) of string but we can see its content
    using index number.
    
    anything that we write inside quotes that is string, that may be letter,symbol,word,sentence,special character.
    
"""
# #example
# name = "ram"
# print(name)
# print(type(name))

# age = """21"""
# print(age)
# print(type(age))


# college = ' xavvr'
# print(college)
# print(type(college))

# symbol = "@#$"
# print(symbol)
# print(type(symbol))

#take any numeric data from user in string format and convert it into integer like age, price , account_no:

# name="sushil" 
# print(name)
# print(name,type(name))

"""
WAP a to print the name , age ,address, weight, department of the  user given by the user and print the typeds of the data
    #note use  f string formate. to print the data

"""
name = input("enter your name: ")

age = int(input("enter your age: "))

address = input("enter your address: ")

weight = float(input("enter your weight: "))

department = input("enter your department: ")

print(f"My name is {name}, My age is {age}, My address is {address}, My weight is {weight}, My department is {department}")

print(name,type(name), age,type(age), address,type(address), weight,type(weight), department,type(department))


