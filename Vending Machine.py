import time# A function to create time intervals for a specific amount
import sys# Adds additional function

wallet = float()
vending_machine = {
    "1": {"Name":"Water       " , "Price" : 1.5},
    "2": {"Name":"Cola        " , "Price" : 2.5},
    "3": {"Name":"Vimto       " , "Price" : 2.5},
    "4": {"Name":"Chocolate   " , "Price" : 2.5},
    "5": {"Name":"Coffee      " , "Price" : 5},
    "A": {"Name":"Snickers    " , "Price" : 10},
    "B": {"Name":"Kit-Kat     " , "Price" : 10},
    "C": {"Name":"Oreo        " , "Price" : 5},
    "D": {"Name":"Plain Bread " , "Price" : 5},
    "E": {"Name":"Cheese Bread" , "Price" : 6},
}

print("You've encountered a wild vending machine!")
time.sleep(1)# Gives 1 second for a user to read the text before moving on
    
def InsertMoney():
    global wallet
    while True:
        try:
            wallet = float(input("\nInsert Cash(1-10 AED allowed): "))
            if wallet < 1 or wallet > 10:
                print("The amount you have given is subceeding/exceeding the limit, 1-10 AED Only.")
            else:
                print(f"\n Accepted {wallet} AED")
                time.sleep(1)
                break
        except ValueError:
            print("Letters are not taken as cash.")

def Goodbye():
    print("\nThank you for shopping at the Wild Vending Machine! See you next time!")
    if wallet >= 1:
        print(f"Dispensing remaining cash: {wallet} AED")
    else:
        sys.exit()

def vendingGuide(): # creating a define function to display vending machine with their number of code, name, and price.
    print("\n====================================================")
    print("|######        A Wild Vending Machine        ######|")
    print("====================================================")
    for key, key1 in vending_machine.items():
        print(f"| Code: {key} || Name: {key1['Name']} || Price: {key1['Price']} AED")
    print("====================================================")
vendingGuide()

def encounter(option): 
        if option == 1:
            print("You approached the wild vending machine,\n you notice there are items displayed with names and prices,\n how much money will you put in the vending machine?")
            time.sleep(3)
        elif option == 2:
            print("You ran away from the vending machine, you did not get anything.")
            sys.exit()
        
print("\nWhat will you do? (1-APPROACH/2-RUN AWAY)")
time.sleep(1.5)
while True:
    try:
        option = int(input("Input: "))
        if option == 1 or option == 2:
            break
        else:
            print("Please enter numbers between 1-2.")
    except ValueError:
        print("Alphabets are not numbers!")
encounter(option)

def vendingProcess():
    global wallet
    InsertMoney()
    vendingGuide()
    print("\nWhat would you like to purchase? Enter with the corresponding number or letter to dispense item.")
    time.sleep(1)
    while True:
        choice = input("\nCode: ").upper()
        if choice in vending_machine:
            item = vending_machine[choice]
            price = item["Price"]
            
            print(f"\nYou selected: {item['Name']}")
            print(f"Price: {price} AED")
            print(f"Your balance: {wallet} AED")
            if wallet >= price:
                wallet -= price
                print(f"Remaining amount: {wallet}")
                time.sleep(2)
                continueshopping = input("Would you like to continue shopping? (Y/N): ").upper()
                if continueshopping == "Y":
                    vendingGuide()
                    print(f"Current Amount: {wallet}")
                    continue
                else:
                    Goodbye()
                break
            else:
                time.sleep(1)
                print("\nInsufficient Funds!")
                time.sleep(2)
                print("Would you like to add more money?")
                ans = input("(Y/N): ").upper()
                if ans == "Y":
                    while True:
                        try:
                            additional_cash = float(input("Insert Extra Cash: "))
                            if additional_cash < 1 or additional_cash > 10:
                                print("Additional cash must be 1-10 AED only")
                                continue
                            if wallet + additional_cash > 10:
                                print("The added cash has exceeded the limit of the vending machine")
                                continue
                            time.sleep(0.5)
                            print(f"\nPrevious amount: {wallet}")
                            time.sleep(1)
                            print("Inserting cash...")
                            time.sleep(1.5)
                            wallet += additional_cash
                            print(f"Current amount: {wallet}")
                            time.sleep(1)
                            print("\nPlease enter the code again or choose a new item.")
                            time.sleep(1)
                            vendingGuide()
                            break
                        except ValueError:
                            print("Error! Cash not detected")
                else:
                    Goodbye()
        else:
            print("Invalid Code, try again")
vendingProcess()