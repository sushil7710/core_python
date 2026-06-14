student = {
    "name" : "Sushil",
    1 : "Id1",
    55.55 : "weight",
    "age" : 25,
    "Gender" : "Male",
    "Marks" : [20, 40, 60, 80],

}
"""
1.) keys:
        it gives all the key inside dictionary.
"""
# print(student.keys())       #output: dict_keys(['name', 1, 55.55, 'age', 'Gender', 'Marks'])



"""
2.) values :
            it gives all the values inside the dictionary.
"""
# print(student.values())         #output: dict_values(['Sushil', 'Id1', 'weight', 25, 'Male', [20, 40, 60, 80]])



"""

3.) items :
           it gives the keys_value pairs in a tuple form and srperated with comma(,).
"""
# print(student.items())          #output: ([('name', 'Sushil'), (1, 'Id1'), (55.55, 'weight'), ('age', 25), ('Gender', 'Male'), ('Marks', [20, 40, 60, 80])])



"""
4.) gets :
         it access the key_value using get method (function).
"""
# print(student["age"])       #output: 25 (using without get key)

# print(student.get("age") )      #output: 25  (using with get key)

# print(student["address"])   #output: error  (there is no address keys, so it throw error )

# print(student.get("address"))   #output: None  (there is no address keys, so it throw none )



"""
5.) updates :
            it update the vakue of respected key  if found, if not found then it will add the key and values at the end of dictionary.

           syntax:
                varName.update({key:value}) 
"""
# student["name"] = "saroj"
# print("name: ", student["name"])     #output: name:  saroj


# student.update({"name" : "saroj"})

# print(student)          #output:  {'name': 'saroj', 1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80]}

# # print(student.get("name: ", "name"))


# student.update({"address" : "Koteshwor"})
# print(student)              #output: {'name': 'saroj', 1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80], 'address': 'Koteshwor'}



"""
6.) clear :
         it remove the all key_pair indide the dictionary and make it empty. 
         it cant print in one line it print in only two line.
    syntax:
         varName.clear()
"""
# student.clear()
# print(student)      #outpput: {}



"""
7.) setDefault :            
               if the key is found then it show its defult value , if not found the it add extra key value pair.
               if we only add key then value is shown none.

        syntax:
            varName.setdefault(key , value)
"""
# student.setdefault("name" , "saroj")
# print(student)

# student.setdefault("address" , "none")
# print(student)




"""
8.) POP :
        it remove the key and value with  the reference key
    syntax:
         varName.pop()
"""
# student.pop("name")
# print(student)      #output: {1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80]}


# student.pop(55.55)
# print(student)      #outpput: {'name': 'Sushil', 1: 'Id1', 'age': 25, 'Gender': 'Male', 'Marks': [20, 40, 60, 80]}




"""
9.) popItem :
            it remove the last key_value pair from dictionary.
    syntax:
    varName.popitem()
"""
# student.popitem()
# print(student)          #output: {'name': 'Sushil', 1: 'Id1', 55.55: 'weight', 'age': 25, 'Gender': 'Male'}