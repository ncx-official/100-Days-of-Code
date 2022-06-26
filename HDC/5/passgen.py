from os import system, name as systemName
import random
import argparse
import re

import asciiArts
from SymbolOption import SymbolOption

def ClearScreen():
    if systemName == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def AboutProgram():
    print(asciiArts.passgen_logo)
    
def AskToQuit():
    userInput = input("Input 'q' to exit or press enter to continue\n--> ")
    if userInput.lower() == 'q':
        ClearScreen()
        exit(1)

def GetSymbolsCount():
    try:
        userInput = input("Enter number of password length: ")
        if userInput == 'q':
            exit()

        symbCount = int(userInput)
        if symbCount <= 0:
            raise ValueError
    except ValueError:
        input("\nBad value, please try again...\n")
        return -1  
    return symbCount

def SetSymbolsOption():
    print(asciiArts.dice)
    print("\nChoose your password options: ")
    print(" input 'u' - UPPERCASE (ABC..XVZ)")
    print(" input 'l' - lowercase (abc..xyz)")
    print(" input 'n' - numbers (012..789)")
    print(" input 's' - special symbols (!@#..^?/)")
    optionsInput = input("--> ").lower()
    
    if optionsInput == '' or re.search('[^ulns ,]', optionsInput):
        input("Wrong input! Try again...\n")
        return -1

    for option in SymbolOption:
        if option.name[0] in optionsInput:
            option.value[0] = True

def CreateSymbolsString():
    symbolsString = ""
    for option in SymbolOption:
        if option.value[0] == True:
            symbolsString += option.value[1]
    return symbolsString

def GeneratePassword(symbolsString, symbolsCount):
    generatedPass = ""
    for symb in range(symbolsCount):
        generatedPass += random.choice(symbolsString)
    return generatedPass

def StartUpArgsParse():
    argParser = argparse.ArgumentParser(description='Password generator version 2.0')
    argParser.add_argument("-pl", "--password_length", help="Input count of password characters", type=int)
    argParser.add_argument("-u", "--uppercase", help="To generate password with uppercase characters", action="store_true")
    argParser.add_argument("-l", "--lowercase", help="To generate password with lowercase characters", action="store_true")
    argParser.add_argument("-n", "--numbers", help="To generate password with numbers", action="store_true")
    argParser.add_argument("-s", "--special_symbols", help="To generate password with special symbols", action="store_true")
    args = argParser.parse_args()
    
    if args.password_length == None:
        return

    options = {
        "uppercase": args.uppercase,
        "lowercase": args.lowercase,
        "numbers": args.numbers,
        "special": args.special_symbols
    }
    input(f"Password: {GeneratePassword(CreateSymbolsString(options), args.password_length)}\n")
    ClearScreen()
    exit()

def MenuScreen():
    while True:
        ClearScreen()
        AboutProgram()

        symbCount = GetSymbolsCount()
        if symbCount == -1: continue
        ClearScreen()
        
        a = SetSymbolsOption() 
        if  a == -1: continue     
        symbString = CreateSymbolsString()
        ClearScreen()

        password = GeneratePassword(symbString, symbCount)
        print(f"\nYour new password: {password}\n" + "-------------------------------\n")
        AskToQuit()

if __name__ == "__main__":
    StartUpArgsParse() 
    MenuScreen()    
