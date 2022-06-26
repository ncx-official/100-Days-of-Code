from os import system, name as systemName
import random
import string
import argparse
import re

import asciiArts

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

def GetSymbolsCount(question):
    try:
        symbCount = int(input(question))
        if symbCount <= 0:
            raise ValueError
    except ValueError:
        input("\nBad value, please try again...\n")
        return  
    return symbCount

def GetSymbolsOption():
    options = {
        "uppercase": False,
        "lowercase": False,
        "numbers": False,
        "special": False
    }

    print(asciiArts.dice)
    print("\nChoose your password options: (To use all the options type 'ulns')")
    print(" - UPPERCASE (input 'u')")
    print(" - lowercase (input 'l')")
    print(" - numbers 0123..89 (input 'n')")
    print(" - special symbols ~!@#$%^..?/ (input 's')")
    optionsInput = input("--> ").lower()
    
    if optionsInput == '' or re.search('[^ulns]', optionsInput):
        input("Wrong input! Try again...\n")
        return

    if 'u' in optionsInput:
        options["uppercase"] = True    
    
    if 'l' in optionsInput:
        options["lowercase"] = True
    
    if 'n' in optionsInput:
        options["numbers"] = True

    if 's' in optionsInput:
        options["special"] = True

    return options

def CreateSymbolsString(options):
    symbolsString = ""
    if options["uppercase"]:
        symbolsString += string.ascii_uppercase
    if options["lowercase"]:
        symbolsString += string.ascii_lowercase
    if options["numbers"]:
        symbolsString += string.digits
    if options["special"]:
        symbolsString += string.punctuation

    return symbolsString

def GeneratePassword(symbolsString, symbolsCount):
    if symbolsString == "":
        return "None"

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

        symbCount = GetSymbolsCount("Enter number of password length: ")
        if symbCount == None: continue
        ClearScreen()
        
        options = GetSymbolsOption()
        if options == None: continue
        symbString = CreateSymbolsString(options)
        ClearScreen()

        password = GeneratePassword(symbString, symbCount)
        print(f"\nYour new password: {password}\n" + "-------------------------------\n")
        AskToQuit()

if __name__ == "__main__":
    StartUpArgsParse() 
    MenuScreen()    
