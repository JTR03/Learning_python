# basic data types: numbers,strings, booleans,sequences: list & tuples,dictionaries

myInt = 5
myFloat = 10.5
myStr = "this is a string"
myBool = True
myList = [0,3,"five", 12.5, False]
myTup = (0,1,3)
# requires unique key values
myDict = {"one": 1, "two": 2}

print(myInt)
print(myFloat)
print(myStr)
print(myBool)
print(myList)
print(myTup)
print(myDict)

# redeclaring variable to new data types work

myInt = "string"
print(myInt)

# accessing data in sequences

print(myList[2])
print(myTup[1])

# slicing a set of data from sequences

print(myList[1:3])
print(myList[1:5:2]) 

# reverse with slice
print(myList[::-1])

# retrieving data from dictionaries
print(myDict["one"])

# global vs local variable

def myFunc():
    # defines and change global variable
    global myStr
    myStr = "function"
    print(myStr)

myFunc()
print(myStr)

# delete variables

del myStr
print(myStr)




