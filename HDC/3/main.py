from PlayerStep import PlayerStep
from logo import gameLogo

print(gameLogo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

crossRoad = PlayerStep('Yoy`re at a cross road. Where do you want to go? Type "left" or "right"\n--> ', {'left':[True, 'You come to a lake.'], 'right':[False, 'Fall into a hole. Game Over.']})
island = PlayerStep('There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n--> ', {'wait':[True, 'You arrive at the island unharmed.'], 'swim':[False, 'Attacked by trout. Game Over.']})
house = PlayerStep('There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n--> ', {'yellow':[True, 'You Win!'], 'red':[False, 'Burned by fire. Game Over.'], '_':'Eaten by beasts. Game Over.'})

gameLevels = [crossRoad, island, house]
for levelObj in gameLevels:
    levelObj.AskQuestion()