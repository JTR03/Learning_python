import random


def main():
    x = 0
    while (x < 3):

        userChoice = input("choose 'r' rock,'p' paper or 's' scissor\n")
        computerChoice = random.choice(['r', 'p', 's'])

        print(computerChoice)

        if userChoice == computerChoice:
            print("It's a tie")

        elif check_winner(userChoice, computerChoice):
            print('You Loose')

        else:
            print('You win')

        x += 1


def check_winner(player, computer):
        if(player == 'r' and computer == 'p') or \
            (player == 'p' and computer == 's') or (player == 's' and computer == 'r'):
            return True


if __name__ == "__main__":
    main()
