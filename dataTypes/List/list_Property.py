"""
1.) concatination property(+) :
                                it join the two lists.
                            
"""
# #example: 1
# list1 = [10, 50 ,60]
# list2 = ["saroj", "rabi", "krishna", "Sushil"]

# result = list1 + list2
# print(result)





"""
indexing: 
        it access the list element by using index number.
"""
# #example: 1
# list1 = [10, 50 , 60] 
# print(list1[1])         #output: 50


"""
3.) Slicing:
            process of accessing the parts (option) of sequence  data type(string,list,tuple,etc)
    syntax:
        varName[start_index:end_endex:sttep]

    note:
        * end_endex value is not included.
        * by defult,step = 1

"""

"""
1.) (+) Positive Indexing:
"""
# #example: 1
# list1 = [10, 50 , 60 ,"saroj", 55.5] 

# print(list1[1:4])       #output: [50, 60, 'saroj']


"""
2.) (-)negative indexing:
"""
# #example:1
# list1 = [10, 50 , 60 ,"saroj", 55.5]            

# print(list1[-2:])          #output: ['saroj', 55.5]



"""
nested list:
           the list inside list is known as nested list.
"""
#example: 1
# list1 = [10, 50 , 60 ,"saroj", 55.5] 
# list2 = ["A", "B"]
# list1.append(list2)

# print(list1)


# #example: 2
# list1 = [10, 50 , 60 ,"saroj", 55.5] 
# list2 = ["A", "B"]
# list = list1 + [list2]

# print(list)