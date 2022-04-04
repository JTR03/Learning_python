

def main():
# indentations indicate being part of function and must have equal indents
    print("Hello World!")
    name = input("What is your name?")
    print("Nice to meet you", name)

# __name__ variable is executed as a main program
# can be ran as a program or as a reusable module
if __name__ == "__main__":
    main()

# python does not look for a soecific function
# before running like traditional languages