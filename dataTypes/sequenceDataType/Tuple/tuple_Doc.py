
"""tuple:
    collection of data (elements or data items) which is immutable, ordered and allows duplicate element.
    Tuple is generally created by small bracket () but it is opitional, and elements of tuple are seperated by comma.

    for example: 1
    subject: ("english", "maths", "Science", "physics", "chemistry")

    example: 2
    a=5,

    we can store different data type together in a tuple.

    for example
    details=(1,"saroj",26,"60.55","kathamandu",True)
    """




"""
1.) immutability check :
"""
# details = (1, "Sushil", 23, "55.56", "kathmandu", True)

# details[2] = "Saroj"
# print(details)       # we cannot change the vslue in tuple. it throw 'tuplte' object  doesnot support item assignment'error



"""
===========Tuple_properties===============
"""

"""
1.) concatination(+) property: 
"""

# fruits = ("apple", "banana", "mango", "papaya")

# colors = ("red", "blue", "green", "yellow")

# print(fruits +  colors)      #output: ('apple', 'banana', 'mango', 'papaya', 'red', 'blue', 'green', 'yellow')

# result = fruits +  colors
# print(result)       #output: ('apple', 'banana', 'mango', 'papaya', 'red', 'blue', 'green', 'yellow')


"""
Access value of tupple by using indexing
"""
# print(fruits[2])    #output: mango




"""
2.) Sciling:

    syntax:
        Var_Name[statr_index : end_index : step]
"""

'''========slicing with (-) Negative indexing=========''' 
# comboo = ("apple", "orange", "pineapple", "red", "orange", "yellow", "ram", "gita")

# print(comboo [-4 : -1])         #output: ('orange', 'yellow', 'ram')

# print(comboo [-2 : -1])         #output:('ram',)

"""
============ Method (function) in tuple ===============
"""

"""
1.) count ():
"""
#example: 1

# comboo = ("apple", "orange", "pineapple", "red", "orange", "yellow", "ram", "gita")

# print(comboo.count("orange"))       #output: 2


"""
2.) Indexing(): 
            it give the  index 
"""

# comboo = ("apple", "orange", "pineapple", "red", "orange", "yellow", "ram", "gita")

# print(comboo.index("orange"))        #output: 1



# student = {
#     "name":"Saroj",
#     "age":26,
#     "address":"Mahendranagar, Nepal",
#     "weight":68.5,
#     "subjects":("English","Math","Science","Biology"),
#     "marks":(90,40,50,80,90,100),
#     "favPlayers":["Messi","Ronaldo","Neymar"]       

# }

# method:1
# text=list(student.get("marks"))
# print(text)

# result = text.append(23)
# print(text)

# student ["marks"] =tuple(text)
# print(student)

# print(student.get("marks"))



# #method: 2
# text=(student.get("marks"))
# print(text)

# lst = list(text)
# print(lst)

# result = lst.append(23)
# print(lst)

# student["marks"] = tuple(lst)
# print(student)

# print(student.get("marks"))


