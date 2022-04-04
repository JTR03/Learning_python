from unittest import result


def conditionals():
    x,y = 100, 1000
# if, elif and else combinations
    if x > y:
        result = "x is greater then y"
    elif x == y:
        result = "x is equal to y"
    else: 
        result = "y is greater then x"

    print(result)

# a if c else b
    result = "x is less then y" if x < y else "X is greater or equal to y"

# match_case to compare multiple value...only available in 3.10

value = "one"
match value:
    case "one":
        result = 1
    
    case "two":
        result = 2

    case "three" | "four":
        result = (3,4)

    case _:
        result = -1

print(result)

conditionals()