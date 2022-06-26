from os import system, name as systemName
import random
import string
import argparse

def ClearScreen():
    if systemName == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def AboutProgram():
    print("________<PasswordMaker>________   ver. 2.0\n")

def AskToQuit():
    userInput = input("Input 'q' to exit or press enter to continue\n--> ")
    if userInput.lower() == 'q':
        ClearScreen()
        exit(1)

def GetSymbolsCount(question):
    try:
        symbCount = int(input(question))
        if symbCount <= 0:
            raise ValueError
    except ValueError:
        input("\nBad value, please try again...")
        return None   
    return symbCount

def GetSymbolsString(question):
    symbolsString = ""

    print(question)
    isLetterCase = input(" - UPPERCASE (input 'u')\n - lowercase (input 'l')\n - BoTh (input 'b')\n--> ")
    ClearScreen()
    
    print(question)
    isNumbers = input(" - numbers 0123..89 (input 'n')\n--> ")
    ClearScreen()

    print(question)
    isSpecialChar = input(" - special symbols ~!@#$%^..?/ (input 's')\n--> ")
    
    isLetterCase = isLetterCase.lower()
    if isLetterCase == 'u':
        symbolsString += string.ascii_uppercase
    elif isLetterCase == 'l':
        symbolsString += string.ascii_lowercase
    elif isLetterCase == 'b':
        symbolsString += string.ascii_letters
    
    isNumbers = isNumbers.lower()
    if isNumbers == 'n':
        symbolsString += string.digits
    
    isSpecialChar = isSpecialChar.lower()
    if isSpecialChar == 's':
        symbolsString += string.punctuation
    return symbolsString

def GeneratePassword(symbolsString, symbolsCount):
    if symbolsString == "":
        return "None"

    generatedPass = ""
    for symb in range(symbolsCount):
        generatedPass += random.choice(symbolsString)
    return generatedPass

def MenuScreen():
    while True:
        ClearScreen()
        AboutProgram()

        symbCount = GetSymbolsCount("Enter number of password length: ")
        ClearScreen()
        
        symbString = GetSymbolsString("Choose your password options: (Leave blank ('') to skip option)")
        ClearScreen()

        password = GeneratePassword(symbString, symbCount)

        print(f"\nYour new password: {password}\n" + "-------------------------------\n")
        AskToQuit()

if __name__ == "__main__": 
    MenuScreen()    
