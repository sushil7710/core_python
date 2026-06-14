"""
1.) add() 
"""

# my_set = {1, 55.5, "ram", "sita"}
# my_set1 = {"orange", "apple"}

# my_set.add("Shyam")
# print(my_set)

# my_set1.add(5)
# print(my_set1)


"""
2.) update():
            it update the set value by providing another set.
"""

#method;1
# my_set = {1, 55.5, "ram", "sita"}
# my_set.update({"shyam"})

# print(my_set)



#method: 2          [ dutai tai set lai merge gare ko ho ]
# my_set = {1, 55.5, "ram", "sita"}
# my_set1 = {"orange", "apple"}

# my_set.update(my_set1)

# print(my_set)


"""
3.) remove():
            it removes the element inside the set.
"""

#method: 1
# my_set = {1, 55.5, "ram", "sita"}

# my_set.remove("ram")

# print(my_set)


# # method :2
# my_set = {1, 55.5, "ram", "sita"}

# my_set.remove("Sushil")

# print(my_set)       #ourput: [ error falxa set ma na vako value remove garna lagyoo vane]




"""
4.) Discard ():
            it also remove the element but it doesn't throw error while element not found inside the set.
"""

# #method: 1
# my_set = {1, 55.5, "ram", "sita"}
# my_set1 = {"orange", "apple"}

# my_set.discard("sushil")         

# print(my_set)       #output: {1, 'sita', 'ram', 55.5}  --->[set ma vako value xainn vane jasta ko teatai aauxa]

# #method:2           
# my_set = {1, 55.5, "ram", "sita"}
# my_set1 = {"orange", "apple"}

# my_set.discard("ram")
# my_set1.discard("orange")

# print(my_set)        #output:{1, 'sita', 55.5}. --->[set ma vako value xa vane set gare ko discard value remove hunxa]

# print(my_set1)      #output: {'apple'}


"""
5.) pop(): 
        it remove any element randomly from  the set
"""
# my_set = {1, 55.5, "ram", "sita"}
# my_set1 = {"orange", "apple"}

# my_set.pop()
# print(my_set)       #output: {1, 'sita', 55.5}. --->[set ma vako jun value pani pop garnu sakxa randomly (1st, mid, last) jun sukai pani]



"""
6.) clear(): 
            it remove all the element from both set (set 1 and set 2)
            
"""
# my_set = {1, 55.5, "ram", "sita"}
# my_set1 = {"orange", "apple"}

# my_set.clear()
# print(my_set)       #outpput: set(). ----> [clear set la total data remove gara rr empty banau xa]



"""
7.) union():
            it contains all the element inside two sets.
"""

# my_set = {1, 55.5, "ram", "sita"}
# my_set1 = {"orange", "apple"}

# #print method :1
# print(my_set.union(my_set1))        #output: {'ram', 1, 'sita', 'orange', 55.5, 'apple'}

# #print method :2.  [using (|) OR operator]
# print(my_set | my_set1)             #output: {'ram', 1, 'sita', 'orange', 55.5, 'apple'}



"""
8.) intersection():
                it contains all the commom element inside two sets.
"""

# my_set = {1, 55.5, "ram", "sita", "sushil"}
# my_set1 = {"orange", "apple", 1, "sushil" }

# #print method :1
# print(my_set.intersection(my_set1))        #output: {1, 'sushil'}

# #print method :2.   [using (&) AND operator]
# print(my_set & my_set1)             #output: {1, 'sushil'}



"""
9.) Difference():
                if two set are given then first difference from other(second).so it take only first set value but don't take first and second intersection value or the value of second set.  
"""
#A difference B
my_set = {1, 55.5, "ram", "sita", "sushil"}
my_set1 = {"orange", "apple", 1, "sushil" }

#print method :1
print(my_set.difference(my_set1))       #output: {'sita', 'ram', 55.5}     

#print method :2 [using (-) minus operator]
print(my_set - my_set1)                 #output: {'sita', 'ram', 55.5} 



# method : B difference A
my_set = {1, 55.5, "ram", "sita", "sushil"}
my_set1 = {"orange", "apple", 1, "sushil" }

#print method :1
print(my_set1.difference(my_set))       #output: {'orange', 'apple'}

#print method :2    [using (-)minus operat
print(my_set1 - my_set)                 #output: {'orange', 'apple'}