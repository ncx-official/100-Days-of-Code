from random import choice
from rpcPresets import rock, paper, scissors

def checkInput(value):
    if value not in ['0', '1', '2']:
        print("Wrong input. Try again!")
        exit()
    return value

gameActions = [rock, paper, scissors]

userChoice = checkInput(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n--> "))
match(userChoice):
    case '0':
        print(rock)
    case '1':
        print(paper)
    case '2':
        print(scissors)

computerChoice = choice(['0', '1', '2'])
print("Computer chose: ")
match(computerChoice):
    case '0':
        print(rock)
    case '1':
        print(paper)
    case '2':
        print(scissors)

if (userChoice == '0' and computerChoice == '2') or (userChoice == '1' and computerChoice == '0') or (userChoice == '2' and computerChoice == '1'):
    print("You Win!")
elif userChoice == computerChoice:
    print("It`s a Draw. Try again!")
else:
    print("You Lose!")

