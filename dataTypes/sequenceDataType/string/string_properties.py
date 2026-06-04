"""
=========string property=========
"""

"""
1.) concatination property(+):
                                it join the two string.
"""
#Syntax:
    # var1+ var2
#in above syntax there  is a two variable and it is concatenated (join) with (+)symbol


# #example:
# var1 = "car"
# var2 = "tyota"
# result = var1+ var2
# print(result)

# print("car"," ","tyota")

# print("car","tyota",sep=" ")


# num = "1"
# num = "2"
# result = "num1" + "num2"

# print(result)


"""
2.)=======id():
                it  gives the memory  address where the data (value)is located.
"""

# name = "sushil"
# rollNo = 5
# weight = 55.5
# print(id(name))
# print(id(rollNo))
# print(id(weight))

"""3. indexing:it acess the string character by using index value. """
#example:
# name = "saroj"
# name[0]

# num = "12345"
# print(num[3]) # 4

# num = "12345"
# print(num[2]) #3
# print(num[8])  # error


#4. len():
# name = "saroj"
# print(len(name)) #5

#5. input():

#6.slicing():

# name = "Saroj"
# print(name[2])

# print(name.index("r"))
# print(len(name))


"""
6)==============slicing============

Slicing: 
        process of acessing the parts(protion) of sequence data type(string, list, tuple,etc)

        Syntax: 
        var_name[start_index:end_index]

        Note:
        *end index value is not includeed.
        *bydefult, step =1
"""

"""
1) (+ve) positive_indexing
"""

#example: 1
# name = 'Sushil'

# address = "Bhaktapur"

# text = name[0:3]      #output: Sus
# print(text)


# name = 'Sushil'

# address = "Bhaktapur"
# text =name[0:3]
# text = name[0::3]       #output: Sh [hamila double:: halyooo vane tespaxi jati number rakhyoo vne tesko 1 kam jump hanxa print ko lagi ]
# print(text)

# print(address[3:6])     #output: kta


# book = "encyclopedia"  #print: "ncy", "ope", "ncyclop"

# print(book[1:4])        #output: ncy
# print(book[6:9])        #output: ope
# print(book[1:8])        #output: ncyclop


"""
2) (-ve) Negative_indexing:
"""
# #example: 1
# name = "saroj"
# address = "bhaktapur"
# print(name[-3::])       #output: roj
# print(name[-3:-1])      #output: ro


#example: 2
# book = "encyclopedia" #print: "nyc", "ope", "nclo"

# print(book[-11:-8])
# print(book[-6:-3])
# print(book[-11:-4:-2])

# #Q.2)
# address = input("enter your address: ")         #input: Dhangadhi
# print(address[2:7])
# print(address[-5::])

# Q.1) .Write a program to take a string from the user and print the first character, second character, and last character using indexing.

# address = input("enter your address: ")           #input: Dhangadhi

# print("the ist character of your Address is: ",address[0:1])       #output: D
# print("the 2nd  character of your Address is: ",address[1:2])       #output:h
# print("the last character of your Address is: ",address[8:])        #output:i


# 2.Write a program to take a string from the user and print the first 4 characters and last 4 characters using slicing.

# Capital_city = input("enter your Capital city:")        #input: Kathmandu

# print(Capital_city[0:4])            #output: Kath
# print(Capital_city[5::])            #output: andu



# # 3.Write a program to take a string from the user and print the string in reverse order using negative slicing.

# address = input("enter your adddress: ")            #input: Koteshwar
# print(address[-9::])


# 4.Write a program to take a string from the user and print every second character from the string.

# name = input("enter your name: ")           #input: Sushil Singh

# print(name[0:12:2])