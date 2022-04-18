# a guessing game - where user guesses an auto generated number

import random

def main(x):
    num = random.randint(1, x)
    guess = 0
    while (guess != num):
        guess =int( input(f"Guess a number between 1 and {x}\n"))
        if (guess < num):
            print("guess again, to low")
        elif (guess > num):
            print ("Sorry guess again, too high")
    
    print ("congratulations you have guessed right")

if __name__ == "__main__":
    main(20)