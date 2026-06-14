""""
# List:
      * collection of data ( element or data item )  which is mutable, order and allow duplicate element. 
      * list is created by [] and element of list are seperated by comma.
# we can create list using list() function if data is in string ,tuple, integer etc


syntax:
list(data_type)

"""


#example: 1
# name = "Sushil Singh"            
# print(list(name))          #output: ['S', 'u', 's', 'h', 'i', 'l', ' ', 'S', 'i', 'n', 'g', 'h'] 

# #example: 1 (for tuple print)
# print(list((1,2,3,4)))          #output: [1, 2, 3, 4]
"""
===========property check============
"""
#===========(1). mutuability check============
# #example:1
# list= ["apple", "orange"]          
# list[0] = "papaya" 

# print(list)         #output: ['papaya', 'orange']    


# #example:2
# list= ["apple", "orange"]                     
# list.insert(0,10)

# print(list)             #output: [10, 'apple', 'orange']


# #example:3
# list= ["apple", "orange"]         
# list[0] = "papaya"             
# list.insert(0,10)            

# print(list)             #output: [10, 'papaya', 'orange']


#===============duplication allow=============
    #example: 1
# list = ["apple", "mango", "orange", "appple", "mango"]
# print(list)

# #example: 2
# list = ["apple", "mango", "ram", "apple", "mango"]
# print(list[2])

# mixing = ["apple", "mango", 1, 55.5, "shyam","hari", "toyta", "Suzuki"]

# print(mixing[3], mixing[4],mixing[6],mixing[0] ) 
# print(mixing[3],"\n",mixing[4], "\n", mixing[6],"\n", mixing[0], sep="")

"""
=====access list element by using indexing======
Syntax:
    var_name[indexing number]
"""