


def main():
    answer = input("Type to check if palindrome or exit to exit: ").lower()

    while(answer != "exit"):
    

        check = answer[::-1]
        if (answer == "exit"):
            break
    
        if (answer == check):
            print("It's a palindrome")
            break
        else:
            print("It's not a palindrome")
            break

main()