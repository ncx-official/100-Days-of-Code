class PlayerStep:
    def __init__(self, question, actions):
        self.question = question
        self.actions = actions

    def AskQuestion(self):
        userInput = input(self.question)
        if userInput in self.actions.keys():      
            if self.actions[userInput][0] == False:
                input(self.actions[userInput][1])
                exit()
            else:
                print(self.actions[userInput][1])
        elif "_" in self.actions.keys():
            print(self.actions['_'])
        else:
            print("Game Over.")
            exit()

if __name__ == "__main__":
    print ("PlayerStep class ver. 1.0")
else:
    pass