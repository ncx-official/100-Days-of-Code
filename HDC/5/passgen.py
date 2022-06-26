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
    logo = '''
     _____                               
    |  __ \                              
    | |__) |_ _ ___ ___  __ _  ___ _ __  
    |  ___/ _` / __/ __|/ _` |/ _ \ '_ \ 
    | |  | (_| \__ \__ \ (_| |  __/ | | |
    |_|   \__,_|___/___/\__, |\___|_| |_|
                        __/ |           
                        |___/             by Ncx (ver. 2.0)
    '''
    print(logo)
    
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
        exit()  
    return symbCount

def GetSymbolsOption(question):
    options = {
        "uppercase": False,
        "lowercase": False,
        "both": False,
        "numbers": False,
        "special": False
    }

    print(question)
    isLetterCase = input(" - UPPERCASE (input 'u')\n - lowercase (input 'l')\n - BoTh (input 'b')\n--> ").lower()
    if isLetterCase == 'u':
        options["uppercase"] = True    
    elif isLetterCase == 'l':
        options["lowercase"] = True
    elif isLetterCase == 'b':
        options["both"] = True
    ClearScreen()
    
    print(question)
    isNumbers = input(" - numbers 0123..89 (input 'n')\n--> ").lower()
    if isNumbers == 'n':
        options["numbers"] = True
    ClearScreen()

    print(question)
    isSpecialChar = input(" - special symbols ~!@#$%^..?/ (input 's')\n--> ").lower()
    if isSpecialChar == 's':
        options["special"] = True

    return options

def CreateSymbolsString(options):
    symbolsString = ""
    if options["uppercase"]:
        symbolsString += string.ascii_uppercase
    if options["lowercase"]:
        symbolsString += string.ascii_lowercase
    if options["both"]:
        symbolsString += string.ascii_letters
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
    argParser.add_argument("-b", "--bothcase", help="To generate password with uppercase and lowercase characters", action="store_true")
    argParser.add_argument("-n", "--numbers", help="To generate password with numbers", action="store_true")
    argParser.add_argument("-s", "--special_symbols", help="To generate password with special symbols", action="store_true")
    args = argParser.parse_args()
    
    if args.password_length == None:
        return

    options = {
        "uppercase": args.uppercase,
        "lowercase": args.lowercase,
        "both": args.bothcase,
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
        ClearScreen()
        
        symbString = CreateSymbolsString(GetSymbolsOption("Choose your password options: (Leave blank ('') to skip option)"))
        ClearScreen()

        password = GeneratePassword(symbString, symbCount)

        print(f"\nYour new password: {password}\n" + "-------------------------------\n")
        AskToQuit()

if __name__ == "__main__":
    StartUpArgsParse() 
    MenuScreen()    
