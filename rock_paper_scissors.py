import random


def main():
    y = 0
    z = 0
    x = 0
    while (x < 3):

        userChoice = input("choose 'r' rock,'p' paper or 's' scissor\n")
        computerChoice = random.choice(['r', 'p', 's'])

        print(computerChoice)

        if (userChoice == 'r' or userChoice == 'p' or userChoice == 's'):

            if userChoice == computerChoice:
                z
                y
            elif check_winner(userChoice, computerChoice):
                z += 1

            else:
                y += 1

            x += 1
        else:
            print('enter a valid input')

    if y > z:
        print('player wins')
    elif y < z:
        print('computer wins')
    else:
        print("It's a tie")


def check_winner(player, computer):
    if(player == 'r' and computer == 'p') or \
            (player == 'p' and computer == 's') or (player == 's' and computer == 'r'):
        return True


if __name__ == "__main__":
    main()
