"""
Create a dictionary with name, age, and city. Add a new key gpa.
"""
# Student = {
#     "name" : "Sushil Singh",
#     "Age" : 23,
#     "City" : "Kathmandu",

# }

# Student["Gpa"] = 3.75
# print(Student)


# # using update function:
# Student.update({"address" : "koteshwar"})

# print(Student)




"""
2. Create a dictionary and update the age from 22 to 23
"""
# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55]
# }
# student.update({"Age" : 23})

# print("Age :",student["Age"])       #output: Age : 23



"""
Remove the city key from a dictionary.
"""

# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55]
# }

# student.pop("city")

# print(student)      # output: {'name': 'Sushil Sngh', 'Age': 22, 'Gender': 'male', 'marks': [45, 65, 76, 80, 55]}



"""
3.) Take a key from the user and display its value using get()
"""

# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55]
# }

# print("name :", student.get("name"))            # output: name : Sushil Sngh

# print("age :", student.get("Age"))              # output: age : 22

# print("City :", student.get("city"))            # output: City : Kathmandu

# print("Gender :", student.get("Gender"))        # output: Gender : male

# print("marks :", student.get("marks"))          # output: marks : [45, 65, 76, 80, 55]



"""
Add multiple new keys (email, phone) using update().
"""
# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55]
# }

# student.update({"phone.no" : 9807710909 })

# student.update({"email" : "sushilsingh2058@gmail.com"})

# print(student)      # output : {'name': 'Sushil Sngh', 'Age': 22, 'city': 'Kathmandu', 'Gender': 'male', 'marks': [45, 65, 76, 80, 55], 'phone.no': 9807710909, 'email': 'sushilsingh2058@gmail.com'}



"""
Remove the last inserted item using popitem()
"""

# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55]
# }

# student.popitem()
# print(student)        # output: {'name': 'Sushil Sngh', 'Age': 22, 'city': 'Kathmandu', 'Gender': 'male'}




"""
7.) Copy a dictionary and add a new key in the copied dictionary
"""
student = {
    "name": "John",
    "age": 20
}
new_student = student.copy()
new_student["grade"] = "A"
print("Original Dictionary:", student)
print("Copied Dictionary:", new_student)




"""
8.) Clear all records from a dictionary.
"""

# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55]
# }

# student.clear()
# print(student)          #output: {}



"""
9.) Create a dictionary using fromkeys() with keys:
"""
# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55]
# }

# method 1
# key = ["name", "Age", "Address", "phone.no"]

# student = dict.fromkeys(key)
# print(student)          #output: {'name': None, 'Age': None, 'Address': None, 'phone.no': None}


# # method 2
# key = ["name", "Age", "Address", "phone.no"]
# student = dict.fromkeys(key)

# student["name"] = "sushil singh"
# student["Age"] = 23
# student["Address"] = "koteshwar"
# student["phone.no"] = 9807710909

# print(student)        # output: {'name': 'sushil singh', 'Age': 23, 'Address': 'koteshwar', 'phone.no': 9807710909}




"""
11.) Add a new student to a nested dictionary.
"""

# student = {
#     "name" : "Sushil Sngh",
#     "Age" : 22,
#     "city" : "Kathmandu",
#     "Gender" : "male",
#     "marks" : [45, 65, 76, 80, 55],
#     "university" : "pokhara",

# }

# student["Department_Computer"]={
#     "Name" : "Aaash Singh", 
#     "rollno" : 221242, 
#     "Sem" : 6, 
#     "total_sub" : 52

# },

# student["department_software"] = {
#     "Name" : "Sushil Singh", 
#     "rollno" : 221243,
#     "Sem" : 8, 
#     "total_sub" : 48,


# }

# print(student)          

"""output: {'name': 'Sushil Sngh', 'Age': 22, 'city': 'Kathmandu', 'Gender': 'male', 'marks': [45, 65, 76, 80, 55], 'university': 'pokhara',
'Department_Computer': ({'Name': 'Aaash Singh', 'rollno': 221242, 'Sem': 6, 'total_sub': 52},),
'department_software': {'Name': 'Sushil Singh', 'rollno': 221243, 'Sem': 8, 'total_sub': 48}}
"""



"""

"""











