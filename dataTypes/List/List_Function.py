"""
# (1.)  append: 
#             it adds the list element to the end of the list.
"""

# #example: 1 ( with out creating variable) 
# lst = ["apple", "orange", "car", "tyota"]
# lst.append("apple")
# print(lst)          #output: ['apple', 'orange', 'car', 'tyota', 'apple']


# #example: 2 (creating variable) 
# list = ["apple", "orange", "car", "tyota"]
# text =list.append("apple")
# print(list)           # output: ['apple', 'orange', 'car', 'tyota', 'apple']


# #example: 3 (with using insert function)
# list = ["apple", "orange", "car", "tyota"]
# list.insert(4,"apple")
# print(list)            #output: ['apple', 'orange', 'car', 'tyota', 'apple']


"""
Q.1) print hari and shyam in console  and add using append elephant,sunflower["apple", "banana","ram",1, "shyam",55.5, "hari"]
"""
# list = ["apple", "banana","ram",1, "shyam",55.5, "hari"]

# print(list[6], list[4])

# list.append("elephant, sunflower")
# print(list)

# #(Q.2)  print: [1,2,3,5,6,7]
# list1 = [1,2,3]
# list2 = [5,6,7]

# list1.extend(list2)      #extend --->la agadi agadi haleko list ma extend use gare rr paxadi vako list valu agadi ko list ma halne kam garxa
# print(list1)          #output: [1, 2, 3, 5, 6, 7]



# animals = ["cow" ,"goat" , "cat"]
# plants = ["herbs", "herbs"]

# plants.extend(animals)
# print(plants)       #output: ['herbs', 'herbs', 'cow', 'goat', 'cat']