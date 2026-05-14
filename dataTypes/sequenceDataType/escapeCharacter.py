# #Escape character: in python escape character is a special type of character which have their own special function.
# # ======1.\n=================
# #\n: it breaks the line and switch to next.
# # it only work for string.
# #example:
# print("College\nname ") 
# """ backslash n switch to next line(Output)
# College 
# name 
# """
# print(5,"\n", 3, sep="")  # sep="" it removes extra space
# """Output:print in one line vertically {
#             5              
#             3             
                            
# }"""
# print(5,6,8,sep="+") #Output:5+6+8

# a = 5
# b = 4
# c = 3
# print(a,b,c)   #output=5 4 3

# print(a,"\n",b,"\n",c)           
# """ output=
# 5 
#  4 
#  3
#  """

# print(a,"\n",b,"\n",c, sep="")   
# """output= seperater removes the extra space from vertical line
# 5
# 4
# 3
# """


# print(a,"\n",b,"\n",c, sep="*")     #it seperated the data by using asterik(*)
# """
# output=
# 5*
# *4*
# *3
# """
# print(a,b,c, sep="*")   #output=5*4*3. #it seperated the data by using asterik(*)

# #=========== 2. carriage retun (\r)==========
# #Carriage return: It moves the cursor to the beginning of the same line without moving to the next line.

# print("Hel\ro")  #oel
# print("stud\rent") #entd
# print("College\rName") #Nameege
# print("abcd\r123")  #123d

# print("Develop\rment") # mentlop

# print("12589\rram")
# print("sajha\rTech")
# print("lap\rtop")
# print("univer\rsity")


# ===3. \t (tab): it provides four in single line.
# print("hel\t o")
# print("12589\tram")
# print("sajha\tTech")
# print("lap\ttop")
# print("univer\tsity")

# ====4.\v vertical space: it provides vertical space.
print("He\vllo")
# print("12589\vram")
# print("sajha\vTech")              
# print("lap\vtop")
# print("univer\vsity")