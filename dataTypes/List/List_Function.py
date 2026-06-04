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


"""
Q.1) print hari and shyam in console  and add using append elephant,sunflower["apple", "banana","ram",1, "shyam",55.5, "hari"]
"""
# list = ["apple", "banana","ram",1, "shyam",55.5, "hari"]

# print(list[6], list[4])

# list.append("elephant, sunflower")
# print(list)



"""
2.) Remove():
            it remove the element (value) from the list.

    syntax:
        numVariable.remove(value)
"""
# #example: 1
# num_list = [10, 50, 60, 80, 90, 50, 20, 30,]
# num_list.remove((10))

# print(num_list)        #output: [50, 60, 80, 90, 50, 20, 30]



# #examle: 2
# num_list = [10, 50, 60, 80, 90, 50, 20, 30,]
# num_list.remove((90))

# print(num_list)          #output: [10, 50, 60, 80, 50, 20, 30]


"""
3.) Pop:
        it remove the value by using index number.

    syntax:
        numVariable.pop(index_Number)
"""
# #example: 1
# num_list = [10, 50, 60, 80, 90, 50, 20, 30,]
# num_list.pop(2)

# print(num_list)         #output: [10, 50, 80, 90, 50, 20, 30]



"""
4.) Extend():


"""

# #(Q.2)  print: [1,2,3,5,6,7]
# list1 = [1,2,3]
# list2 = [5,6,7]

# list1.extend(list2)      #extend --->la agadi agadi haleko list ma extend use gare rr paxadi vako list valu agadi ko list ma halne kam garxa
# print(list1)          #output: [1, 2, 3, 5, 6, 7]



# animals = ["cow" ,"goat" , "cat"]
# plants = ["herbs", "herbs"]

# plants.extend(animals)
# print(plants)       #output: ['herbs', 'herbs', 'cow', 'goat', 'cat']

"""
5.) Clear():
            IT clear the list all elements (value.)
    sybtax:
        VariableName.clear()
        
"""
##example: 1
# num_list = [10, 50, 60, 80, 90, 50, 20, 30,]
# num_list.clear()

# print(num_list)         #output: []


# #example: 2
# fruits =["apple", "mango", "papaya", "orange", "banana"]
# fruits.clear()

# print(fruits)           #output: []

"""
6.) count():
            it count the  total number of search value  which is in the list.

"""

# #example: 1
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]

# print(num_list)         #output: [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# print(num_list.count(20))            #output: 4

# print(num_list.count(50))           #outpiut: 2








"""
7.) insert():
            it keep value in providing  index number.
    syntax:
        varName.insert(index_number, value)

"""

# #example: 3 (with using insert function)
# list = ["apple", "orange", "car", "tyota"]
# list.insert(4,"apple")
# print(list)            #output: ['apple', 'orange', 'car', 'tyota', 'apple']


# #example: 1
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num_list.insert(1,40)

# print(num_list)             #Output: [10, 40, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]



# #example: 2
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num_list.insert(5,99)

# print(num_list)             #output: [10, 50, 60, 80, 90, 99, 50, 20, 30, 20, 20, 30, 20]


"""
8.) Sort():

"""
# #example:1.  (in accending orser)
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num_list.sort()

# print(num_list)            #output: [10, 20, 20, 20, 20, 30, 30, 50, 50, 60, 80, 90]





# #example: 2 (in decending order with  print in accending order)
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num_list.sort()
# num_list.sort(reverse = True)

# print(num_list)      #output: [90, 80, 60, 50, 50, 30, 30, 20, 20, 20, 20, 10]





# # #example: (first print in accending order then print in decending order using reverse function )
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num_list.sort()

# print(num_list)         #output:[10, 20, 20, 20, 20, 30, 30, 50, 50, 60, 80, 90]

# num = num_list.sort(reverse = True)
# print(num_list)         #output: [90, 80, 60, 50, 50, 30, 30, 20, 20, 20, 20, 10]





# #example: (ptiny in decending order with  out using sort function)
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num = num_list.sort(reverse = True)

# print(num_list)         #output: [90, 80, 60, 50, 50, 30, 30, 20, 20, 20, 20, 10]


"""
9.) Reverse():
            it reverde the list element (value)


"""
# #example: 1
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num_list.reverse()
# print(num_list)             #output: [20, 30, 20, 20, 30, 20, 50, 90, 80, 60, 50, 10]




"""
10.) Copy():
            it duplicates the given list.

"""
# #example: 1
# num_list = [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]
# num_list.copy()
# print(num_list)             #output: [10, 50, 60, 80, 90, 50, 20, 30, 20, 20, 30, 20]



"""
Q.2) write a program  to add your  3 favourite player in a list  using append () function.
# note: take 3 favourite player as input from user

"""
# #method: 1
# player_name1 =input("enter the player_name1: ")
# player_name2 =input("enter the player_name2: ")
# player_name3 =input("enter the player_name3: ")

# player_names = player_name1 +" "+ player_name2 +" "+ player_name3

# txt = player_names.split()
# print("favourite player name: ",txt)
# txt.append("ssggggs")
# print(txt)



# # method: 2
# players = [input("enter first player of element of list")]
# player1 = input("enter the 1st player name: ")
# player2 = input("enter the 2nd player name: ")
# player3 = input("enter the 3rd player name: ")

# players.append(player1)
# players.append(player2)
# players.append(player3)

# print(players)




# # method 3

# players = [input("enter the first player name: ")]

# players.append(input("enter the 2nd plsyer name: "))
# players.append(input("enter the 3rd player name: "))

# print("players list: ",players)



"""
11) min():
"""
numlist =  [10, 50, 60, 80, 90 ,50, 20, 30, 20,20, 20, 30]

print(min(numlist))


"""
12) max():
"""
numlist =  [10, 50, 60, 80, 90 ,50, 20, 30, 20,20, 20, 30]

txt =max(numlist)
print(txt)







