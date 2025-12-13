# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]

# print(len(mylist))

# to access a member of a sequence type, use []
    # index are 0 based
    # positive index starts from begining
    # negative index starts from end

# print(mylist[2])
# print(mylist[-1])
# mylist[0] = 10
# print(mylist)

# add a list to another list
# aList = [6,7,8]
# mylist = mylist + aList
# print(mylist)

# strings are sequences
# strings are also immutable, therefore cannot be changed after being made
# mystr = "This is a string"
# print(mystr[2])
# mystr[2] = "Z"  # this line will cause an error as you cannot change a character within a string


# use slices to get parts of a sequence
# print(mylist[1:4:2])
# slice format: object[<index_start> : <index_end> : <step>]
# mylist[::2] is from index 0 (start), to index <len(mylist)> (end), step 2
# print(mylist[::2])
# this will print the my list at index 1 up to, but not including, index 4 ( ie. [1,4) ). This is done with a step of 2, ie. every other value

# you can use slices to reverse a sequence
# print(mylist[::-1])

# Tuples are like lists, but they are immutable
mytuple = (0,1,2,"three")
# print(mytuple[1])
# often used to hold data that won't change, more memory efficient
# return multiple values from a function

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 2, 4, "hey"}
# print(myset) # returns {1, 2, 3, 4, 'hey'}

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
# in looks for item on left in object on right
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)

mystr = "This is a string"
print("i" in mystr)