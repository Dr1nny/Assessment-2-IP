import time# A function to create time intervals for a specific amount
import sys# Adds additional function

wallet = float() #variable for the users balance
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

print("You've encountered a wild vending machine!")# the first thing that is displayed on the console
time.sleep(1)# Gives 1 second for a user to read the text before moving on
    
def InsertMoney(): # This function serves as a way to call back on inserting money
    global wallet
    while True:
        try:
            wallet = float(input("\nInsert Cash(1-10 AED allowed): "))
            if wallet < 1 or wallet > 10: # limiting the user to put cash lower than 1 or above 10
                print("The amount you have given is subceeding/exceeding the limit, 1-10 AED Only.")
            else:
                print(f"\n Accepted {wallet} AED")
                time.sleep(1)
                break
        except ValueError: # will deny request taken from non-values
            print("Letters are not taken as cash.")

def Goodbye(): # another function that will help ending the prgram
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

def encounter(option): # the encounter function whether to interact or to run away
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

def vendingProcess(): #The entire process of how the vending machine operates
    global wallet
    InsertMoney() # will ask to insert money
    vendingGuide() # create a display function to show to the user
    print("\nWhat would you like to purchase? Enter with the corresponding number or letter to dispense item.")
    time.sleep(1)
    while True: #creating a loop to ensure if the user makes an error, they can try again
        choice = input("\nCode: ").upper()#askes the user to select the corresponding code from the vending machine
        if choice in vending_machine:
            item = vending_machine[choice] #takes the users input and checks the values stored in the dictionary from the vending machine
            price = item["Price"]# takes the price from the selected dictionary in the vending machine
            #displays item name with the according price with your balance
            print(f"\nYou selected: {item['Name']}")
            print(f"Price: {price} AED")
            print(f"Your balance: {wallet} AED")
            if wallet >= price:
                wallet -= price
                print(f"Remaining amount: {wallet}")
                time.sleep(2)
                continueshopping = input("Would you like to continue shopping? (Y/N): ").upper() 
                if continueshopping == "Y":# If user enters "Y", it will continue to run the vending machine until the user wants to stop.
                    vendingGuide()
                    print(f"Current Amount: {wallet}")# will display the current amount to help user manage cash.
                    continue
                else:
                    Goodbye()#ends the program and dispenses any remaining amount
                break
            else:# If a user has insufficient funds, it will ask to either add more money or not which will end up closing the program.
                time.sleep(1)
                print("\nInsufficient Funds!")
                time.sleep(2)
                print("Would you like to add more money?")
                ans = input("(Y/N): ").upper()
                if ans == "Y":
                    while True:
                        try:
                            additional_cash = float(input("Insert Extra Cash: "))
                            if additional_cash < 1 or additional_cash > 10: #works exactly as how the function InsertMoney() but for additional cash.
                                print("Additional cash must be 1-10 AED only")
                                continue
                            if wallet + additional_cash > 10:
                                print("The added cash has exceeded the limit of the vending machine")
                                continue
                            #Creates a satisfying display of showing the previous amount and simulating inserting cash and adding up the additional cash with the current wallet which asks to choose the same item or choose a new one.
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
                            vendingGuide()#will display the vending machine screen for easier access instead of having to scroll
                            break
                        except ValueError:
                            print("Error! Cash not detected")
                else:#any answer that isnt "Y" will immediately close the program
                    Goodbye()
        else:
            print("Invalid Code, try again")
vendingProcess()
