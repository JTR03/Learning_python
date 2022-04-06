# basic function structure
from unittest import result
from winreg import REG_RESOURCE_REQUIREMENTS_LIST


def function1():
    print("I am a function")

# function with arguments
def function2(arg1, arg2):
    print(arg1, " ", arg2)

# function with a return a value
def cube(x):
    return x * x * x

# function with default value for argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

# function with variable number of arguments
# possible to add multiple arguments but *args must be last
def multi_add(*args):
    result = 0

    for x in args:
        result = result + x
    return result

print(power(x=3, num=2))
# python doesn't car about order as long arguments are named correctly

print(multi_add(20,5,5, -3))