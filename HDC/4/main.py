from random import choice
from Weapon import Weapon
from rpcPresets import rock_txt, paper_txt, scissors_txt, gun_txt

def CheckInput(value, actions):
    try:
        value = int(value)
        if value not in [i.id for i in actions]:
            raise ValueError
        return value
    except ValueError:
        print("Wrong input. Try again!")
        exit()

actions = [
    Weapon(0, "Rock", rock_txt, [2, 3], [0], [1]),
    Weapon(1, "Paper", paper_txt, [0], [1], [2, 3]),
    Weapon(2, "Scissors", scissors_txt, [1], [2], [0, 3]),
    Weapon(3, "Gun", gun_txt, [1, 2], [3], [0]),
]

print("__<Welcome to Rock Paper Scissors extended edition>__")
userChoice = CheckInput(input("What do you choose? Type:\n " + ''.join([f"| {action.id} | for {action.name} |\n " for action in actions]) + "\n--> "), actions)
userAction = next(action for action in actions if action.id == userChoice)
userActionPreset = userAction.getPreset()

print("\nComputer chose:")
computerChoice = choice([action.id for action in actions]) 
computerAction = next(action for action in actions if action.id == computerChoice)
computerActionPreset = computerAction.getPreset()

match(userAction.compareAction(computerAction)):
    case True:
        print("You Win!")
    case False:
        print("You Lose!")
    case _:
        print("It`s a Draw. Try again!")
