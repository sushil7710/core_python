"""
        Dictionary:A dictionary is a built-in data type in Python that stores a collection of data in key-value pairs. 
        Each key is unique and is used to access its corresponding value.
         #It is mutable, ordered, and do not allow duplicate keys.

         #Dictionary is created by curly bracket "{}" and data(key-value pair) is seperated
         by comma. ",".

         syntax:
         dict_var = {
         
                    key1:value1,
                    key2:value2,
                    key3:value2,
         }
         Note:
            key must be unique and immutable data type.

"""

#while writtting key  and value name then use double or single quotent.

# student = {
#     "name" : "Sushil",
#     1 : "Id1",
#     55.55 : "weight",
#     "age" : 25,
#     "Gender" : "Male",
#     "Marks" : [20, 40, 60, 80],
# }


#it access all key value  pair inside the dictonary.
# print(student)          #output: {'name': 'Sushil', 1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80]}


"""
it access name(key) value only.
    syntax:
       var_name["key"]
"""

# print("name: ",student["name"])         #output: name:  Sushil 


# print("1: ",student[1])             #ourput:1:  Id1

# print("55.55: ", student[55.55])            #ourput: 55.55:  weight

# print("age: ", student["age"])          #ourput: age:  25

# print("Gender: ", student["Gender"])        #ourput: Gender:  Male

# print("Marks: ", student["Marks"])          #ourput: Marks:  [20, 40, 60, 80]

# print(student["Marks"][2])            #output: 60

# #Type function is used  to check tyhe data types
# print(type(student))    #output: <class 'dict'>


# student["name"] = "Saroj"
# print(student)

# student["Marks"].append(50)
# print(student)

# student["Marks"][2]=90
# print(student)              #output:{'name': 'Sushil', 1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 90, 80]}


# student[55.55]="tree_weight"
# print(student)          #output: {'name': 'Sushil', 1: 'Id1', 55.55: 'tree_weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80]}

"""
del() function.
"""
#method: 1
# del(student["name"])
# print(student)          #output: {1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80]}

#method:2
# delstudent["name"]
# print(student)          #output: {1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80]}


# del(student["Marks"][2])
# print(student)         #output:  "Marks" : [20, 40, 80],


"""
details = {
    "name":"Saroj",
    "age":26,
    "address":"Mahendranagar,Nepal",
    "weight":68.5,
    "subjects":("English","Math","Science","Biology"),
    "marks":[90,40,50,80,90,100],
    "favPlayers":["Messi","Ronaldo","Neymar"]       

}

Print the following output

Output:
Deepak
D
["Messi","Ronaldo","Neymar"]       

"""
# details = {
#     "name":"Saroj",
#     "age":26,
#     "address":"Mahendranagar,Nepal",
#     "weight":68.5,
#     "subjects":("English","Math","Science","Biology"),
#     "marks":[90,40,50,80,90,100,[2,4,6]],
#     "favPlayers":["Messi","Ronaldo","Neymar"]       
# }


# print("name: ", details["name"])

# # details["name"] = "Deepak" 
# # print("name: ", details["name"])


# # print("subjects: ", details["subjects"])


# # print("favPlayers: ", details["favPlayers"])

# text = details["marks"][6][2]
# print(text)

# print(details["marks"][6][2])


