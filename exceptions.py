# error handling

try:
    x = 10/0
except:
    print("That's not a valid equation")

# handling a specific error

try:
    answer = input("Type a number to divide 10")
    num = int(answer)
    print(10/num)

except ZeroDivisionError as e:
    print("You cannot divide by zero")

except ValueError as e:
    print("invalid entry")

finally:
    print("this code always runs")