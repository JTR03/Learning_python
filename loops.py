def main():
    x = 0
# while loop execute while condition is true
    while (x < 5):
        print(x)
        x += 1

# for loops - in range interates from first num to but not inclusive of last num

    for x in range(5,10):
        print (x)

    days = ["Mon", "Tue", "Wed", "thur","Fri","Sat", "Sun"]

    for d in days:
        print(d)


# break - stops program when condition is true
    for x in range(3,10):
        if x == 7:
            break
        print(x)

# continue - skips over when condition is true
    for x in range(3,10):
        if x % 2 == 0:
            continue
        print(x)

# enumerate helps get index num of variable
    days = ["Mon", "Tue", "Wed", "thur","Fri","Sat", "Sun"]

    for i,d in enumerate(days):
        print(i,d)


main()