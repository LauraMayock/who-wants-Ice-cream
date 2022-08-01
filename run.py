"""
Import gspread in order to update google spreadsheet
"""
import gspread
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
from datetime import datetime   # import for timestamp


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("CREDS.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Ice-creams")
receipt = SHEET.worksheet(("receipt"))
flavours = SHEET.worksheet("flavours")
flav_list = flavours.col_values(1)[1:]


order = SHEET.worksheet("receipt")

# create a list of the customers order
customer_order = []
price = []
noScoops = 0
selected_flavour = []




# date and time generated for receipt generated by receipt function
now = datetime.now()
date = now.strftime("%c")


def start_order():
    """
    Function to welcome the customer and ask if they would like to order.
    """
    print("Hi, Welcome to The Inside Scoop")
    print("Would you like to place and order?")
    question1 = input("Please enter yes or no.")
    if question1.lower() == ("yes"):
        place_order()
    elif question1.lower() == ("no"):
        print("Ok, let me know when you have decided.")
        start_order()
    else:
        print("Sorry invalid entry.")
        print("Plese enter yes or no.")
        start_order()


def place_order():
    choice = True
    while True:
        holder = input("What would you like a cup or a cone?").lower()
        if holder in ("cup", "cone"):
            number_scoops()
            break
            
        else:
            holder = input("incorrect input....\n Please select cup or cone").lower()

def number_scoops():
    global noScoops
    scoops = int(input("How many scoops? Enter 1, 2 or 3"))
    if scoops == 1:
        print("Ok, one scoop")
        customer_order.append("One scoop.")
        price.append(2.00)
        noScoops = 1 
        flavour_choice()
    elif scoops == 2:
        print("Ok, two scoops it is.")
        customer_order.append("two scoops")
        price.append(3.00) 
        noScoops = 2
        flavour_choice()
    elif scoops == 3:
        print("ok, Three scoops it is.")
        customer_order.append("Three scoops")
        price.append(4.00)
        noScoops = 3
        flavour_choice()
    else:
        print("Sorry invalid entry.")
        number_scoops()

def flavour_choice():
    print("what flavour would you like?")
    flavour_list = []
    for type in flav_list:
        flavour_list.append(type)
    num = []
    for i in range(1, 7):
        num.append(i)

    flavour_choice.type = dict(zip(num, flavour_list))

    type_table = PrettyTable()
    type_table.field_names = num
    type_table.add_row(flavour_list)
    print(type_table)

def iceCreamFlavours():
    global selected_flavour
    """
    Chose flavours
    """
    while True:
        try:
            flv = list(input("what flavour would you like?"))
            flv.sort()
            selected_flavour = [int(i)for i in flv]
            if len(flv) > noScoops:
                print(f"You have chosen {flv}. Thats too many. You wanted {noScoops} scoops.")
                continue
            if len(flv) < noScoops:
                print(f"You havent chosen enough flavours. You said you wanted {noScoops}")
                continue
            if len(flv) == noScoops:
                print(f"you have chosen {selected_flavour}")
                customer_order.append(selected_flavour)
                sprinkles()
                break
        except ValueError:
            print("Please type a number between 1-7")


def sprinkles():
    if noScoops == 3:
        print("There is an offer on at the moment. Free sprinkles when you get 3 scoops")
        answer = input("yes/no")
        if answer.lower() == ("yes"):
            print("Added sprinkes")
            customer_order.append("Free sprinkles")
        elif answer.lower() == ("no"):
            print("Ok, no sprinkes")
        else:
            print("Sorry invalid entry.")
            print("Plese enter yes or no.")
    else:
        print("Would you like sprinkes with that? It will be and extra 50c")



def print_receipt():
    """
    Print receipt
    """
   
    receipt_table = PrettyTable()
    receipt_table.add_row([f'Date: {date}'])
    receipt_table.add_row([f"Order: {customer_order}"])
    receipt_table.add_row([f"Total: €{price}"])

    
    print(receipt_table)


start_order()  
iceCreamFlavours()
print_receipt()
#print(f"That will be a total of €{price}")


