def IntInputChecker(value, message="Wrong value, try again..."):
    try:
        value = int(value)
        return value
    except ValueError:
        print(message)
        exit()

def FloatInputChecker(value, message="Wrong value, try again..."):
    try:
        value = float(value)
        return value
    except ValueError:
        print(message)
        exit()

print("Welcome to the tip calculator.")
total_bill = FloatInputChecker(input("What was the total bill?\n--> $"))
people_count = IntInputChecker(input("How many people to split the bill?\n--> "))

while True:
    percentage_tip = FloatInputChecker(input("What percentage tip would you like to give? 10, 12, or 15?\n--> ")) 
    if percentage_tip not in [10, 12, 15]:
        userInput = input(f"Are you sure you want to give ${round(total_bill*(percentage_tip / 100))} tip? (yes/no)\n--> ")
        if userInput.lower() not in ['yes', 'y']:
            continue
    break

payment = (total_bill + (total_bill * (percentage_tip / 100))) / people_count
print(f"Each person should pay: ${round(payment, 2)}")
